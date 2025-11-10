#!/usr/bin/env python3
"""
Reformat Deepgram transcripts to group consecutive speaker turns

Deepgram outputs each line with inline speaker labels:
  [150.8s] SPEAKER_00: What's going on, everybody?
  [152.7s] SPEAKER_01: Alex, I sent you invite to speak
  [156.6s] SPEAKER_01: and cohost.

This script reformats to group consecutive turns from same speaker:
  SPEAKER_00:
  [150.8s] What's going on, everybody?
  
  SPEAKER_01:
  [152.7s] Alex, I sent you invite to speak
  [156.6s] and cohost.

Matches WhisperX output format for consistency.
"""

import sys
import re
from pathlib import Path

def reformat_transcript(input_path, output_path=None):
    """Reformat Deepgram transcript to group consecutive speaker turns"""
    
    # Read input file
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse and group by speaker
    current_speaker = None
    output_lines = []
    
    for line in lines:
        line = line.rstrip()
        if not line:
            continue
            
        # Match pattern: [timestamp] SPEAKER_XX: text
        match = re.match(r'\[(\d+\.\d+)s\]\s+(SPEAKER_\d+):\s*(.+)', line)
        
        if match:
            timestamp, speaker, text = match.groups()
            
            # New speaker - add header
            if speaker != current_speaker:
                if output_lines:  # Add blank line before new speaker (except first)
                    output_lines.append('')
                output_lines.append(f'{speaker}:')
                current_speaker = speaker
            
            # Add timestamped text
            output_lines.append(f'[{timestamp}s] {text}')
        else:
            # Line doesn't match expected format - preserve as-is
            output_lines.append(line)
    
    # Write output
    if output_path is None:
        output_path = input_path  # Overwrite original
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
        f.write('\n')  # Final newline
    
    return output_path

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Reformat Deepgram transcript to group consecutive speaker turns',
        epilog='''
Example:
  python3 scripts/reformat_deepgram_transcript.py intermediates/interview_deepgram_transcript_with_speakers.txt
  
This will overwrite the original file with the reformatted version that matches
WhisperX output format (speaker headers followed by grouped timestamped lines).
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input', help='Input Deepgram transcript file')
    parser.add_argument('-o', '--output', help='Output file (default: overwrite input)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f'Error: Input file not found: {input_path}')
        sys.exit(1)
    
    output_path = Path(args.output) if args.output else None
    
    try:
        result_path = reformat_transcript(input_path, output_path)
        print(f'✓ Reformatted transcript saved to: {result_path}')
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
