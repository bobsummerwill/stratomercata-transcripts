#!/usr/bin/env python3
"""
SpeechBrain Compatibility Patch for torchaudio 2.9.0

This script applies patches to SpeechBrain to make it compatible with
torchaudio 2.9.0, which removed the list_audio_backends() function.
"""

import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <speechbrain_backend_file>")
        sys.exit(1)

    speechbrain_backend = sys.argv[1]

    # Read the file
    try:
        with open(speechbrain_backend, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: SpeechBrain backend file not found: {speechbrain_backend}")
        sys.exit(1)

    # Check if already patched
    if 'hasattr(torchaudio, "list_audio_backends")' in content:
        print("Already patched")
        sys.exit(0)

    # Apply the patch
    original = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        available_backends = torchaudio.list_audio_backends()

        if len(available_backends) == 0:
            logger.warning(
                "SpeechBrain could not find any working torchaudio backend. Audio files may fail to load. Follow this link for instructions and troubleshooting: https://speechbrain.readthedocs.io/en/latest/audioloading.html"
            )"""

    replacement = """    elif torchaudio_major >= 2 and torchaudio_minor >= 1:
        # list_audio_backends() is not available in torchaudio 2.9.0
        if hasattr(torchaudio, "list_audio_backends"):
            available_backends = torchaudio.list_audio_backends()
            if len(available_backends) == 0:
                logger.warning(
                    "SpeechBrain could not find any working torchaudio backend. Audio files may fail to load. Follow this link for instructions and troubleshooting: https://speechbrain.readthedocs.io/en/latest/audioloading.html"
                )
        else:
            # Newer torchaudio versions don't have list_audio_backends()
            logger.info("Using torchaudio with default audio backend")"""

    if original in content:
        content = content.replace(original, replacement)
        try:
            with open(speechbrain_backend, 'w') as f:
                f.write(content)
            print("Patch applied successfully")
        except PermissionError:
            print(f"ERROR: Permission denied writing to {speechbrain_backend}")
            sys.exit(1)
    else:
        print("ERROR: Could not find pattern to patch")
        sys.exit(1)

if __name__ == "__main__":
    main()
