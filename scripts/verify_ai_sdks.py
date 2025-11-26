#!/usr/bin/env python3
"""
AI SDK Verification Script for WhisperX Installation

Tests import of AI provider SDKs required for WhisperX transcription.
Used by install_packages_and_venv.py to verify successful SDK installation.

Usage: python scripts/verify_ai_sdks.py
"""

import sys

def test_sdk(name, import_name=None):
    """Test importing an SDK and return result"""
    if import_name is None:
        import_name = name

    try:
        __import__(import_name)
        print(f"✓ {name}")
        return True
    except ImportError as e:
        print(f"❌ {name}: FAILED - {e}", file=sys.stderr)
        return False

def main():
    print("Verifying AI provider SDK installations...")

    # AI SDKs to test
    sdks = [
        ("assemblyai", "assemblyai"),
        ("deepgram-sdk", "deepgram"),
        ("openai", "openai"),
        ("anthropic", "anthropic"),
        ("google-generativeai", "google.generativeai"),
        ("requests", "requests"),
    ]

    failed_sdks = []

    for sdk_name, import_name in sdks:
        if not test_sdk(sdk_name, import_name):
            failed_sdks.append(sdk_name)

    if failed_sdks:
        print(f"FAILED_SDKS: {','.join(failed_sdks)}", file=sys.stderr)
        sys.exit(1)
    else:
        print("✓ All AI provider SDKs verified")
        print("VERIFICATION_SUCCESS")
        sys.exit(0)

if __name__ == "__main__":
    main()
