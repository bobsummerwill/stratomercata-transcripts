#!/usr/bin/env python3
# ==============================================================================
# Batch Process All MP3 Files in Project Root with Multi-Provider AI Pipeline
# ==============================================================================
# - Loops through all MP3 files in project root directory
# - Calls process_single.py for each file
# - Outputs to ./outputs directory
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
    # Defaults: WhisperX (local/FREE) + Claude Sonnet 4.5 (highest quality)
    DEFAULT_TRANSCRIBERS = "whisperx"
    DEFAULT_PROCESSORS = "sonnet"

    parser = argparse.ArgumentParser(description="Batch Process All MP3 Files in Project Root with Multi-Provider AI Pipeline")
    parser.add_argument("--transcribers", default=DEFAULT_TRANSCRIBERS,
                       help="Comma-separated transcription services (whisperx, whisperx-cloud, deepgram, assemblyai). Default: whisperx")
    parser.add_argument("--processors", default=DEFAULT_PROCESSORS,
                       help="Comma-separated AI post-processors (sonnet, chatgpt, gemini, llama, qwen-cloud, qwen). Default: sonnet (Claude Sonnet 4.5)")

    args = parser.parse_args()

    transcribers = args.transcribers
    processors = args.processors

    # Directories
    project_dir = os.getcwd()
    intermediates_dir = os.path.join(project_dir, "intermediates")
    output_dir = os.path.join(project_dir, "outputs")

    # Ensure directories exist
    os.makedirs(intermediates_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    print("="*72)
    print("Batch MP3 Processing with AI Pipeline")
    print("="*72)
    print(f"Transcribers: {transcribers}")
    print(f"Processors: {processors}")
    print()

    # Find all MP3 files
    mp3_files = glob.glob("*.mp3")
    total = len(mp3_files)

    if total == 0:
        print("No MP3 files found in project root directory")
        sys.exit(1)

    print(f"Found {total} MP3 files to process")
    print()

    # Overall timing
    batch_start = time.time()

    # Timing arrays
    file_names = []
    process_times = []

    # Process each file
    count = 0
    processed = 0
    failed = 0

    for mp3_file in mp3_files:
        count += 1
        basename = Path(mp3_file).stem
        
        print("="*72)
        print(f"[{count}/{total}] Processing: {basename}")
        print("="*72)
        
        file_start = time.time()
        
        # Call process_single.py
        cmd = [
            "python3", "scripts/process_single.py", mp3_file,
            "--transcribers", transcribers, "--processors", processors
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            file_end = time.time()
            file_duration = int(file_end - file_start)
            
            print(f"✓ Pipeline complete for {basename}")
            print(f"  Time: {format_duration(file_duration)}")
            
            # Store timing data
            file_names.append(basename)
            process_times.append(file_duration)
            
            processed += 1
        else:
            print(f"✗ Pipeline failed for {basename}")
            print(result.stderr)
            failed += 1
        
        print()

    batch_end = time.time()
    batch_duration = int(batch_end - batch_start)

    # Summary report
    print("="*72)
    print("✓ Batch Processing Complete!")
    print("="*72)
    print()
    print("Summary:")
    print(f"  Total files found: {total}")
    print(f"  Processed successfully: {processed}")
    print(f"  Failed: {failed}")
    print(f"  Intermediates: {intermediates_dir}")
    print(f"  Final output: {output_dir}")
    print()

    if processed > 0:
        print("Timing Details:")
        print()
        
        # Calculate total
        total_file_time = sum(process_times)
        
        # Print per-file timing
        for i, name in enumerate(file_names):
            print(f"{name}")
            print(f"  Pipeline time: {format_duration(process_times[i])}")
            print()
        
        print("="*72)
        print("Totals:")
        print(f"  Total processing time:    {format_duration(total_file_time)}")
        print(f"  Batch overhead:           {format_duration(batch_duration - total_file_time)}")
        print(f"  Overall batch time:       {format_duration(batch_duration)}")
        print()

    # Show output file patterns
    transcriber_array = [t.strip() for t in transcribers.split(',')]
    processor_array = [p.strip() for p in processors.split(',')]

    print("Files created per MP3:")
    print("  Intermediates (./intermediates/):")
    for transcriber in transcriber_array:
        if transcriber == "whisperx":
            print("    - *_transcript_with_speakers.txt (whisperx)")
        else:
            print(f"    - *_{transcriber}_transcript_with_speakers.txt")
    print("  Final Output (./outputs/):")
    for transcriber in transcriber_array:
        for processor in processor_array:
            if transcriber == "whisperx":
                print(f"    - *_{processor}_corrected.txt")
            else:
                print(f"    - *_{transcriber}_{processor}_corrected.txt")
    print()
    print("Customize settings:")
    print(f"  Defaults: --transcribers {DEFAULT_TRANSCRIBERS} --processors {DEFAULT_PROCESSORS}")
    print(f"  Example: python3 scripts/process_all.py --transcribers deepgram --processors chatgpt,gemini")
    print()

if __name__ == "__main__":
    main()
