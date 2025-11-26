#!/usr/bin/env python3
"""
Package Verification Script for WhisperX Installation

Tests import of core packages required for WhisperX transcription.
Used by install_packages_and_venv.py to verify successful package installation.

Usage: python scripts/verify_packages.py
"""

import sys

def test_package(name, import_name=None):
    """Test importing a package and return result"""
    if import_name is None:
        import_name = name

    try:
        __import__(import_name)
        print(f"{name}: OK")
        return True
    except ImportError as e:
        print(f"{name}: FAILED - {e}", file=sys.stderr)
        return False

def main():
    print("Verifying core package installations...")

    # Core packages to test
    packages = [
        ("torch", "torch"),
        ("whisperx", "whisperx"),
        ("pyannote.audio", "pyannote.audio"),
        ("transformers", "transformers"),
        ("numpy", "numpy"),
    ]

    failed_packages = []

    for package_name, import_name in packages:
        if not test_package(package_name, import_name):
            failed_packages.append(package_name)

    if failed_packages:
        print(f"FAILED_PACKAGES: {','.join(failed_packages)}", file=sys.stderr)
        sys.exit(1)
    else:
        print("VERIFICATION_SUCCESS")
        sys.exit(0)

if __name__ == "__main__":
    main()
