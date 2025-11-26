#!/usr/bin/env python3
"""
PyTorch Verification Script for WhisperX Installation

This script validates PyTorch installation in a virtual environment.
Used by install_packages_and_venv.py to verify successful PyTorch setup.

Usage: python scripts/pytorch_verify.py
"""

import sys

def main():
    try:
        import torch

        # Get version
        version = torch.__version__
        print(f"PyTorch {version}")

        # Check CUDA availability
        cuda_available = torch.cuda.is_available()
        print(f"CUDA: {cuda_available}")

        # Run basic tensor test
        if cuda_available:
            x = torch.randn(10, 10, device='cuda')
            print("GPU test: PASSED")
        else:
            x = torch.randn(10, 10)
            print("CPU test: PASSED")

        # Success marker
        print("VERIFICATION_SUCCESS")
        sys.exit(0)

    except ImportError as e:
        print(f"ERROR: PyTorch import failed - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: PyTorch verification failed - {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
