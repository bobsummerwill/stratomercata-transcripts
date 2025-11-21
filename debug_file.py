def transcribe_whisperx_cloud(audio_path, output_dir):
    """WhisperX cloud transcription via Replicate with speaker diarization"""
    import replicate
    import time
    import json
    from pathlib import Path

    api_token = os.environ.get('REPLICATE_API_TOKEN')
    if not api_token:
        raise ValueError("REPLICATE_API_TOKEN environment variable not set")

    audio_path_obj = Path(audio_path)

    print(f"  Uploading and transcribing via Replicate...")
    print(f"  Model: WhisperX Large-v3")

    start_time = time.time()

    try:
        # Run WhisperX on Replicate - matches local large-v3 settings with Pyannote diarization
        prediction = replicate.run(
            "m1guelpf/audio-speaker-to-text:2f9072ca3a8b89f4fcc3b8db05708cb2e6049cdce35126a5ecab8228228",
            input={
                "audio_file": open(audio_path, "rb"),  # File object - Replicate handles upload
                "batch_size": 8  # Match local optimal
            }
        )

        elapsed = time.time() - start_time
        print(f"  Transcribed in {elapsed:.1f}s")

        # Parse the output
        segments = []

        # Assuming prediction is a dict with 'segments' list
        pred_segments = prediction.get('segments', [])

        if pred_segments:
            for seg in pred_segments:
                start = float(seg.get('start', 0))
                end = float(seg.get('end', 0))
                speaker = seg.get('speaker', 'SPEAKER_00')
                if speaker and not speaker.startswith('SPEAKER_'):
                    speaker = f'SPEAKER_{int(speaker):02d}'
                text = seg.get('text', '').strip()

                segments.append({
                    'start': start,
                    'end': end,
                    'speaker': speaker,
                    'text': text
                })

        if not segments:
            raise ValueError("No transcription segments returned from Replicate")

        # Count speakers
        speakers = set(seg['speaker'] for seg in segments if seg['speaker'].startswith('SPEAKER_'))
        print(f"  Detected {len(speakers)} speakers")

        # Save using utility function (same format as local whisperx)
        output_path = save_transcript_files(
            output_dir,
            audio_path_obj.stem,
            "whisperx-cloud",
            segments
        )

        return output_path

    except Exception as e:
        raise RuntimeError(f"WhisperX Cloud transcription failed: {e}")

# Test the function briefly
# import os
