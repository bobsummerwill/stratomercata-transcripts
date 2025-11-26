#!/usr/bin/env python3
# ==============================================================================
# NVIDIA Driver Installation Script for RTX 5070
# ==============================================================================
#
# This script installs NVIDIA drivers on Ubuntu 24.04 LTS for RTX 5070 GPU.
# RTX 5070 requires driver version 565 or newer.
#
# Usage:
#   sudo python3 install_nvidia_drivers.py
#   sudo reboot
#
# ==============================================================================

import os
import sys
import subprocess
import platform

def detect_os():
    """Detect operating system and version (same as main installer)"""
    system = platform.system().lower()

    if system == "darwin":
        os_type = "macos"
        version = platform.mac_ver()[0]
        major = int(version.split('.')[0])
        return os_type, version, major

    elif system == "linux":
        try:
            with open("/etc/os-release", "r") as f:
                content = f.read()
                if "ID=ubuntu" in content:
                    for line in content.split('\n'):
                        if line.startswith("VERSION_ID="):
                            version = line.split('=')[1].strip('"')
                            return "ubuntu", version, int(version.split('.')[0])
        except FileNotFoundError:
            pass

    print(f"ERROR: Unsupported operating system: {system}")
    print("This script requires either:")
    print("  - macOS Sonoma (14.x)")
    print("  - Ubuntu 24.04 LTS")
    sys.exit(1)

def run_command(cmd, description, capture_output=True, text=True, check=True):
    """Run a command and handle errors comprehensively"""
    print(description)
    try:
        result = subprocess.run(cmd, shell=False, capture_output=capture_output, text=text)
        if check and result.returncode != 0:
            print(f"Error running command: {' '.join(cmd)}")
            if result.stdout:
                print(f"STDOUT: {result.stdout}")
            if result.stderr:
                print(f"STDERR: {result.stderr}")
            print(f"Command failed with exit code: {result.returncode}")
            sys.exit(1)
        print("✓ Complete")
        return result
    except FileNotFoundError:
        print(f"Command not found: {cmd[0]}")
        print("This might indicate missing dependencies or PATH issues.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error running command: {e}")
        sys.exit(1)

def main():
    print("=" * 50)
    print("NVIDIA Driver Installation")
    print("=" * 50)
    print()

    # OS Detection - same as main installer
    os_type, os_version, os_major = detect_os()

    if os_type == "macos":
        if os_major != 14:
            print(f"ERROR: Unsupported macOS version")
            print(f"This script requires macOS Sonoma (14.x)")
            print(f"Your version: {os_version}")
            sys.exit(1)
        print("✓ macOS Sonoma detected")
        print("")
        print("ℹ  NVIDIA drivers are not needed on macOS")
        print("macOS uses Metal Performance Shaders (MPS) for GPU acceleration")
        print("PyTorch will automatically use MPS when available")
        print("")
        print("If you have an external NVIDIA GPU connected via Thunderbolt,")
        print("it will not be accessible for CUDA workloads in this setup.")
        print("")
        print("NVIDIA driver installation: NOT REQUIRED")
        print("You can proceed directly to:")
        print("  python3 scripts/install_packages_and_venv.py")
        sys.exit(1)  # Exit with error code to indicate "not needed"
    elif os_type == "ubuntu":
        if os_version != "24.04":
            print("ERROR: Unsupported Ubuntu version")
            print("This script requires Ubuntu 24.04 LTS")
            print(f"Your version: {os_version}")
            sys.exit(1)
        print("✓ Ubuntu 24.04 LTS detected")
    else:
        # detect_os() already handles unsupported OSes, but belt and suspenders
        print("ERROR: This script only supports Ubuntu 24.04 LTS")
        print("On macOS, NVIDIA drivers are not required (uses MPS)")
        sys.exit(1)

    print()

    # Check if running as root (only needed for Ubuntu)
    if os.geteuid() != 0:
        print("ERROR: This script must be run as root (use sudo)")
        sys.exit(1)

    # Step 1: Update system packages
    print("[1/4] Updating system packages...")
    run_command(["apt", "update"], "Updating package list...")
    run_command(["apt", "upgrade", "-y"], "Upgrading packages...")

    # Step 2: Install NVIDIA driver
    print("[2/4] Installing NVIDIA driver...")
    print("This will automatically detect your GPU and install the latest compatible driver.")
    run_command(["ubuntu-drivers", "install"], "Installing NVIDIA driver...")

    # Step 3: Check current nvidia-smi status (may not work until reboot)
    print("[3/4] Checking current driver status...")
    result = run_command(["nvidia-smi"], "Checking current NVIDIA driver status...", check=False)
    if result.returncode == 0:
        print("Driver is already loaded:")
        print(result.stdout)
    else:
        print("Driver installed but not loaded yet (reboot required)")
        print("This is normal - drivers become active after system reboot")

    # Step 4: Final instructions
    print("=" * 50)
    print("✓ Installation Complete!")
    print("=" * 50)
    print()
    print("IMPORTANT: You MUST reboot for the driver to work.")
    print()
    print("After reboot, verify the installation with:")
    print("  nvidia-smi")
    print()
    print("Expected output should show:")
    print("  - Driver Version: 565.xx or newer")
    print("  - CUDA Version: 12.8 or newer")
    print("  - GPU: NVIDIA GeForce RTX 5070")
    print()
    print("To reboot now, run:")
    print("  sudo reboot")
    print()
    print("After reboot, continue with:")
    print("  python3 scripts/install_packages_and_venv.py")
    print()

if __name__ == "__main__":
    main()
