#!/usr/bin/env python3
"""
Complete WhisperX transcription pipeline with speaker diarization
"""

import sys
import os
import time
import subprocess
import tempfile
from pathlib import Path
import pandas as pd
import whisperx
import torch
from pyannote.audio import Pipeline

# Configure TF32 (suppresses PyTorch 2.9 deprecation warnings)
# Keep the old API settings - they still work, just show warnings
torch.backends.cudnn.allow_tf32 = True
torch.backends.cuda.matmul.allow_tf32 = True

def transcribe_audio(audio_path, device, compute_type="float16", high_accuracy=False, model_name="large-v2", initial_prompt=None):
    """Run WhisperX transcription - hardcoded to English
    
    Args:
        audio_path: Path to audio file
        device: Device to use (cuda/cpu)
        compute_type: Compute precision (float16/int8/float32)
        high_accuracy: Enable high-accuracy mode (slower, more thorough)
        model_name: Model to use (large-v2, large-v3, turbo, distil-large-v3)
        initial_prompt: Optional prompt text to guide transcription (max 224 tokens)
    """
    print("\n" + "="*60)
    print("Step 1: Transcribing audio with WhisperX...")
    print("="*60)
    
    # Display quality mode
    quality_mode = "HIGH QUALITY" if high_accuracy else "LOW QUALITY"
    device_type = "GPU" if device == "cuda" else "CPU"
    print(f"Mode: {quality_mode}, {device_type}")
    print(f"Model: {model_name}")
    print(f"Compute type: {compute_type}")
    print("Language: en (hardcoded)")
    if initial_prompt:
        prompt_preview = initial_prompt[:100] + "..." if len(initial_prompt) > 100 else initial_prompt
        print(f"Initial prompt: {prompt_preview}")
    
    start = time.time()
    
    # Load model with English language hardcoded
    model = whisperx.load_model(model_name, device, compute_type=compute_type, language="en")
    
    # Transcribe with explicit English language to prevent drift
    audio = whisperx.load_audio(audio_path)
    
    if high_accuracy:
        # HIGH QUALITY settings - smaller batches allow more GPU memory per sample
        # Combined with float32 compute type for maximum precision
        batch_size = 4 if device == "cuda" else 2
        
        print(f"Settings: batch_size={batch_size} (high-accuracy mode with float32)")
        result = model.transcribe(audio, 
                                 batch_size=batch_size, 
                                 language="en",
                                 initial_prompt=initial_prompt)
    else:
        # LOW QUALITY (FAST) settings - standard batch processing
        batch_size = 16 if device == "cuda" else 8
        print(f"Settings: batch_size={batch_size} (standard fast mode)")
        result = model.transcribe(audio, 
                                 batch_size=batch_size, 
                                 language="en",
                                 initial_prompt=initial_prompt)
    
    # Align whisper output using English
    model_a, metadata = whisperx.load_align_model(language_code="en", device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
    
    elapsed = time.time() - start
    print(f"✓ Transcription complete in {elapsed:.1f}s ({elapsed/60:.1f} min)")
    
    return result

def diarize_audio(audio_path, hf_token, device):
    """Run speaker diarization"""
    print("\n" + "="*60)
    print("Step 2: Running speaker diarization...")
    print("="*60)
    
    start = time.time()
    
    # Check if input is MP3 - if so, convert to WAV to avoid sample count issues
    audio_path_obj = Path(audio_path)
    temp_wav = None
    diarize_path = audio_path
    
    if audio_path_obj.suffix.lower() == '.mp3':
        print("Converting MP3 to WAV for diarization (avoids sample count mismatch)...")
        temp_wav = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_wav.close()
        
        # Convert MP3 to WAV using ffmpeg
        cmd = [
            'ffmpeg', '-i', audio_path,
            '-ar', '16000',  # 16kHz sample rate (standard for speech)
            '-ac', '1',       # Mono audio
            '-y',             # Overwrite output file
            temp_wav.name
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            diarize_path = temp_wav.name
            print(f"✓ Converted to WAV: {temp_wav.name}")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to convert MP3 to WAV: {e}")
            print("Attempting diarization with original MP3...")
            if temp_wav:
                os.unlink(temp_wav.name)
            temp_wav = None
            diarize_path = audio_path
    
    try:
        # Load diarization pipeline from pyannote.audio
        diarize_model = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            token=hf_token
        ).to(torch.device(device))
        
        # Run diarization
        diarize_segments = diarize_model(diarize_path)
        
        elapsed = time.time() - start
        print(f"✓ Diarization complete in {elapsed:.1f}s ({elapsed/60:.1f} min)")
        
        return diarize_segments
        
    finally:
        # Clean up temporary WAV file
        if temp_wav and os.path.exists(temp_wav.name):
            os.unlink(temp_wav.name)
            print("Cleaned up temporary WAV file")

def assign_speakers(result, diarize_segments):
    """Assign speakers to transcript segments"""
    print("\n" + "="*60)
    print("Step 3: Assigning speakers to transcript...")
    print("="*60)
    
    # pyannote.audio 4.0 returns a DiarizeOutput dataclass with speaker_diarization attribute
    # Extract the Annotation object and convert to pandas DataFrame (required by WhisperX)
    annotation = diarize_segments.speaker_diarization
    
    diarize_list = []
    for segment, _, speaker in annotation.itertracks(yield_label=True):
        diarize_list.append({
            'start': segment.start,
            'end': segment.end,
            'speaker': speaker
        })
    
    # Create DataFrame with required columns
    diarize_df = pd.DataFrame(diarize_list)
    
    result_with_speakers = whisperx.assign_word_speakers(diarize_df, result)
    
    # Count speakers
    speakers = set()
    for segment in result_with_speakers["segments"]:
        if "speaker" in segment:
            speakers.add(segment["speaker"])
    
    print(f"✓ Detected {len(speakers)} speakers: {sorted(speakers)}")
    
    return result_with_speakers

def save_transcript(result, output_path):
    """Save formatted transcript as both .txt and .md"""
    print("\n" + "="*60)
    print("Step 4: Saving transcripts...")
    print("="*60)
    
    # Save .txt file
    with open(output_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in result["segments"]:
            speaker = segment.get("speaker", "UNKNOWN")
            
            if speaker != current_speaker:
                f.write(f"\n{speaker}:\n")
                current_speaker = speaker
            
            start_time = segment["start"]
            text = segment["text"].strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    print(f"✓ Text saved to: {output_path}")
    
    # Save .md file
    md_path = output_path.parent / f"{output_path.stem.replace('_transcript_with_speakers', '_transcript')}.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        current_speaker = None
        for segment in result["segments"]:
            speaker = segment.get("speaker", "UNKNOWN")
            
            if speaker != current_speaker:
                f.write(f"\n**{speaker}:**\n")
                current_speaker = speaker
            
            start_time = segment["start"]
            text = segment["text"].strip()
            f.write(f"[{start_time:.1f}s] {text}\n")
    
    print(f"✓ Markdown saved to: {md_path}")
    
    # Print statistics
    speakers = {}
    for segment in result["segments"]:
        speaker = segment.get("speaker", "UNKNOWN")
        speakers[speaker] = speakers.get(speaker, 0) + 1
    
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    for speaker in sorted(speakers.keys()):
        print(f"  {speaker}: {speakers[speaker]} segments")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Complete WhisperX transcription with speaker diarization (English only)",
        epilog="""
Quality modes:
  --high-quality: Enable thorough processing (slower, more accurate)
  --low-quality:  Fast processing (default, good accuracy)
  
Device modes:
  Auto-detect GPU (default)
  --force-cpu:    Force CPU even if GPU available
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("audio_file", help="Audio file path")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--token", help="HuggingFace token (overrides HF_TOKEN env var)")
    parser.add_argument("--high-quality", action="store_true", 
                       help="Enable high-quality mode (5-10x slower, more accurate)")
    parser.add_argument("--low-quality", action="store_true",
                       help="Force low-quality/fast mode (overrides default)")
    parser.add_argument("--force-cpu", action="store_true",
                       help="Force CPU processing even if GPU available")
    parser.add_argument("--model", default="large-v2",
                       choices=["large-v2", "large-v3", "turbo", "distil-large-v3"],
                       help="Whisper model to use (default: large-v2)")
    parser.add_argument("--initial-prompt",
                       help="Initial prompt text or path to prompt file (guides transcription, max 224 tokens)")
    parser.add_argument("--auto-prompt", action="store_true",
                       help="Use built-in Ethereum terminology prompt automatically")
    
    args = parser.parse_args()
    
    # Validate conflicting options
    if args.high_quality and args.low_quality:
        print("Error: Cannot specify both --high-quality and --low-quality")
        sys.exit(1)
    
    # Get token
    hf_token = args.token or os.environ.get('HF_TOKEN')
    if not hf_token:
        print("Error: HuggingFace token not provided.")
        print("Set HF_TOKEN environment variable or use --token argument")
        sys.exit(1)
    
    # Check audio file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: Audio file not found: {audio_path}")
        sys.exit(1)
    
    # Determine quality mode (default is low-quality/fast unless high-quality specified)
    high_quality_mode = args.high_quality
    
    # Handle initial prompt
    initial_prompt = None
    if args.auto_prompt:
        # Load built-in Ethereum prompt
        prompt_file = Path(__file__).parent / "ethereum_initial_prompt.txt"
        if prompt_file.exists():
            with open(prompt_file, 'r', encoding='utf-8') as f:
                initial_prompt = f.read().strip()
            print(f"Using built-in Ethereum prompt from: {prompt_file}")
        else:
            print(f"Warning: ethereum_initial_prompt.txt not found at {prompt_file}")
    elif args.initial_prompt:
        # Check if it's a file path or direct text
        prompt_path = Path(args.initial_prompt)
        if prompt_path.exists():
            with open(prompt_path, 'r', encoding='utf-8') as f:
                initial_prompt = f.read().strip()
            print(f"Using prompt from file: {prompt_path}")
        else:
            # Treat as direct text
            initial_prompt = args.initial_prompt
            print("Using provided prompt text")
    
    # Set output path with settings info for comparison
    if args.output:
        output_path = Path(args.output)
    else:
        # Build descriptive filename with settings
        model_short = args.model.replace("distil-", "d").replace("large-", "l")
        quality = "hq" if high_quality_mode else "lq"
        output_path = audio_path.parent / f"{audio_path.stem}_{model_short}_{quality}_transcript_with_speakers.txt"
    
    # Setup device based on flags
    if args.force_cpu:
        device = "cpu"
    else:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Setup compute type based on device and quality
    if high_quality_mode:
        # High quality: use float32 for maximum precision
        compute_type = "float32"
    else:
        # Low quality (fast): use appropriate default for device
        compute_type = "float16" if device == "cuda" else "int8"
    
    print("="*60)
    print("WhisperX Transcription Pipeline with Diarization")
    print("="*60)
    print(f"Audio file: {audio_path}")
    print(f"Output file: {output_path}")
    print(f"Device: {device}" + (" (forced)" if args.force_cpu else ""))
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Quality mode: {'HIGH' if high_quality_mode else 'LOW (FAST)'}")
    print(f"Compute type: {compute_type}")
    print("="*60)
    
    # Start total timer
    total_start = time.time()
    
    # Run pipeline
    try:
        # Step 1: Transcribe (English hardcoded)
        result = transcribe_audio(str(audio_path), device, compute_type, 
                                 high_accuracy=high_quality_mode,
                                 model_name=args.model,
                                 initial_prompt=initial_prompt)
        
        # Step 2: Diarize
        diarize_segments = diarize_audio(str(audio_path), hf_token, device)
        
        # Step 3: Assign speakers
        result_with_speakers = assign_speakers(result, diarize_segments)
        
        # Step 4: Save
        save_transcript(result_with_speakers, output_path)
        
        # Total time
        total_elapsed = time.time() - total_start
        print("\n" + "="*60)
        print(f"✓ COMPLETE! Total time: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
