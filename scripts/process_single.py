#!/usr/bin/env python3
# ==============================================================================
# Single MP3 Transcription with Multi-Provider Pipeline
# ==============================================================================
# Minimal orchestration script - calls Python scripts for all heavy lifting
# ==============================================================================

import argparse
import os
import sys
import time
import subprocess
import glob
from pathlib import Path

def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def main():
    parser = argparse.ArgumentParser(description="Single MP3 Transcription with Multi-Provider Pipeline")
    parser.add_argument("audio_file", help="Path to MP3 audio file")
    parser.add_argument("--transcribers", required=True,
                       help="Comma-separated transcription services (whisperx, whisperx-cloud, deepgram, assemblyai)")
    parser.add_argument("--processors", required=True,
                       help="Comma-separated AI post-processors (sonnet, chatgpt, gemini, llama, qwen)")
    parser.add_argument("--batch-size", type=int, help="Batch size for WhisperX (default: 16 GPU, 8 CPU)")
    parser.add_argument("--force-cpu", action="store_true", help="Force CPU mode for WhisperX (fixes torchvision issues)")

    args = parser.parse_args()

    audio_file = args.audio_file
    transcribers = args.transcribers
    processors = args.processors
    batch_size = args.batch_size
    force_cpu = args.force_cpu

    # Validate audio file
    if not os.path.isfile(audio_file):
        print(f"Error: Audio file not found: {audio_file}")
        sys.exit(1)

    # Start overall timing
    pipeline_start = time.time()

    # Show what we're doing
    base_name = Path(audio_file).stem
    transcriber_array = [t.strip() for t in transcribers.split(',')]
    processor_array = [p.strip() for p in processors.split(',')]
    total_combinations = len(transcriber_array) * len(processor_array)

    print("========================================================================")
    print("Multi-Transcriber × Multi-Processor Pipeline")
    print("========================================================================")
    print(f"Audio: {audio_file}")
    print(f"Transcribers: {transcribers} ({len(transcriber_array)} services)")
    print(f"Processors: {processors} ({len(processor_array)} services)")
    print(f"Total combinations: {total_combinations}")
    print("========================================================================")
    print()

    # PHASE 1: Transcription (Python handles all transcribers internally)
    print("PHASE 1: Transcription")
    print("========================================================================")

    phase1_start = time.time()

    transcribe_cmd = [
        "python3", "scripts/process_single_transcribe_and_diarize.py",
        audio_file, "--transcribers", transcribers
    ]
    if batch_size:
        transcribe_cmd.extend(["--batch-size", str(batch_size)])
    if force_cpu:
        transcribe_cmd.append("--force-cpu")

    result = subprocess.run(transcribe_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("✗ Transcription phase failed")
        print(result.stderr)
        sys.exit(1)

    phase1_end = time.time()
    phase1_duration = int(phase1_end - phase1_start)

    print()
    print(f"Phase 1 complete: {format_duration(phase1_duration)}")
    print()

    # Find generated transcript files (no _raw suffix)
    transcript_files = []
    for transcriber in transcriber_array:
        transcript_file = f"intermediates/{base_name}_{transcriber}.txt"
        if os.path.isfile(transcript_file):
            transcript_files.append(transcript_file)

    if not transcript_files:
        print("Error: No transcript files were generated")
        sys.exit(1)

    # PHASE 2: Post-Processing (Python handles all processors internally)
    print("PHASE 2: Post-Processing")
    print("========================================================================")

    phase2_start = time.time()

    # Pass transcript files with proper quoting to handle spaces
    post_process_cmd = [
        "python3", "scripts/process_single_post_process.py",
        "--processors", processors
    ]
    post_process_cmd.extend(transcript_files)

    result = subprocess.run(post_process_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("✗ Post-processing phase failed")
        print(result.stderr)
        sys.exit(1)

    phase2_end = time.time()
    phase2_duration = int(phase2_end - phase2_start)

    print()
    print(f"Phase 2 complete: {format_duration(phase2_duration)}")
    print()

    # Overall timing
    pipeline_end = time.time()
    pipeline_duration = int(pipeline_end - pipeline_start)

    print("========================================================================")
    print("✓ PIPELINE COMPLETE!")
    print("========================================================================")
    print()
    print("Timing Summary:")
    print(f"  Phase 1 (Transcription):   {format_duration(phase1_duration)}")
    print(f"  Phase 2 (Post-Processing): {format_duration(phase2_duration)}")
    print(f"  Total Pipeline Time:       {format_duration(pipeline_duration)}")
    print()
    print("Output files:")
    print("  Transcripts: ./intermediates/")
    print("  Corrected:   ./outputs/")
    print("========================================================================")

if __name__ == "__main__":
    main()
