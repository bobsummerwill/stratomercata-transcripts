#!/usr/bin/env python3
# ==============================================================================
# Python Environment Setup Script for WhisperX Transcription
# ==============================================================================
#
# DESCRIPTION:
#   Automated setup script that installs and configures WhisperX for audio
#   transcription with speaker diarization. Supports both NVIDIA GPU and
#   CPU-only systems with automatic hardware detection.
#
# OPERATING SYSTEM SUPPORT:
#   - macOS Sonoma (14.x)
#   - Ubuntu 24.04 LTS
#   Note: Script will fail immediately on any other OS or version
#
# HARDWARE SUPPORT:
#   - NVIDIA GPUs: RTX 5070 Blackwell, RTX 50/40/30/20 series, GTX, Tesla
#   - CPU-only: Any system without NVIDIA GPU (including AMD GPUs via CPU)
#
# WHAT IT DOES:
#   1. Detects OS and version
#   2. Detects hardware (NVIDIA GPU vs CPU)
#   3. Installs system dependencies (ffmpeg, build tools, Python dev)
#   4. Creates isolated Python virtual environment
#   5. Installs WhisperX and dependencies
#   6. Installs PyTorch 2.9.0 (GPU or CPU)
#   7. Verifies PyTorch installation
#   8. Applies compatibility patches to WhisperX
#   9. Installs pyannote.audio 4.0+
#  10. Applies compatibility patches to SpeechBrain
#  11. Configures LD_LIBRARY_PATH for NVIDIA
#  12. Verifies package installations
#  13. Installs AI provider SDKs (transcription & post-processing)
#  14. Builds Ethereum glossaries
#  15. Sets up environment configuration file
#
# REQUIREMENTS:
#   - macOS Sonoma (14.x) OR Ubuntu 24.04 LTS
#   - Python 3.12
#   - macOS: Homebrew installed (script will check and guide installation)
#   - Ubuntu: sudo access for system package installation
#   - For NVIDIA (Ubuntu): Driver 565+ installed (run install_nvidia_drivers.sh first)
#
# USAGE:
#   python3 scripts/install_packages_and_venv.py                    # Auto-detect hardware
#   python3 scripts/install_packages_and_venv.py --force-cpu        # Force CPU-only mode
#
# OPTIONS:
#   --force-cpu       Force CPU-only installation even if NVIDIA GPU is present
#                     Useful for testing or when you want CPU mode on GPU system
#
# POST-INSTALLATION:
#   1. Get HuggingFace token: https://huggingface.co/settings/tokens
#   2. Edit setup_env.sh and add your token
#   3. Accept model agreements:
#      - https://huggingface.co/pyannote/speaker-diarization-3.1
#      - https://huggingface.co/pyannote/segmentation-3.0
#
# ==============================================================================

import argparse
import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def run_command(cmd, description, cwd=None, check=True):
    """Run a command and return the result"""
    print(description)
    if isinstance(cmd, str):
        shell = True
        cmd_str = cmd
    else:
        shell = False
        cmd_str = ' '.join(cmd)
    result = subprocess.run(cmd, shell=shell, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running: {cmd_str}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        sys.exit(1)
    print("✓ Complete")
    return result

def check_homebrew():
    """Check if Homebrew is installed on macOS"""
    try:
        run_command(["brew", "--version"], "Checking Homebrew installation", check=False)  # This will always try to print
        return True
    except SystemExit:  # From our run_command with check=True we'd exit, but here we catch
        return False

def detect_os():
    """Detect operating system and version"""
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

def detect_hardware(force_cpu):
    """Detect hardware capabilities"""
    if force_cpu:
        print("--force-cpu flag detected")
        print("⚠ Forcing CPU-only mode (ignoring any NVIDIA GPU)")
        print("Will install PyTorch 2.9.0 CPU-only version")
        return False

    if os_type == "macos":
        print("⚠ macOS detected - using CPU/MPS mode")
        print("Will install PyTorch 2.9.0 CPU-only version (Metal Performance Shaders supported)")
        return False

    # Check for NVIDIA GPU - run_command with check=False since nvidia-smi may not exist
    try:
        result = run_command(["nvidia-smi"], "Checking for NVIDIA GPU availability", check=False)
        if result.returncode == 0:
            gpu_name = result.stdout.split('\n')[7].split('|')[1].strip() if len(result.stdout.split('\n')) > 7 else "NVIDIA GPU"
            print(f"✓ Detected NVIDIA GPU: {gpu_name}")
            print("Will install PyTorch 2.9.0 with CUDA 13.0 support")
            return True
        else:
            print(f"NVIDIA GPU check failed (return code: {result.returncode})")
    except Exception as e:
        print(f"NVIDIA GPU detection failed: {e}")

    print("⚠ No NVIDIA GPU detected - using CPU mode")
    print("Will install PyTorch 2.9.0 CPU-only version")
    return False

def install_system_dependencies():
    """Install system dependencies"""
    print("[2/15] Installing system dependencies...")

    if os_type == "macos":
        print("Installing required packages via Homebrew:")
        print("  - ffmpeg: Audio/video processing for WhisperX")
        print("  - python@3.12: Python 3.12 interpreter")
        print("  - git: Version control for installing packages from GitHub")

        # Check if packages are already installed
        to_install = []
        for pkg in ["ffmpeg", "python@3.12", "git"]:
            result = run_command(["brew", "list", pkg], f"Checking if {pkg} is installed", check=False)
            if result.returncode != 0:
                to_install.append(pkg)
            else:
                print(f"✓ {pkg} is already installed")

        if to_install:
            cmd = ["brew", "install"] + to_install
            run_command(cmd, f"Installing: {' '.join(to_install)}")
        else:
            print("✓ All required packages are already installed")

        # Set Python 3.12 from Homebrew
        print("Setting up Python 3.12 from Homebrew...")
        os.environ["PATH"] = f"/opt/homebrew/opt/python@3.12/libexec/bin:{os.environ.get('PATH', '')}"

        # Verify Python version
        run_command(["python3", "--version"], "Verifying Python version after Homebrew setup", check=False)

    elif os_type == "ubuntu":
        print("Installing required system packages:")
        print("  - build-essential: C/C++ compilers for building Python packages")
        print("  - ca-certificates: SSL/TLS certificates for secure connections")
        print("  - curl: HTTP client for API requests")
        print("  - ffmpeg: Audio/video processing for WhisperX")
        print("  - git: Version control for installing packages from GitHub")
        print("  - libcurl4-openssl-dev: cURL development libraries for Python packages")
        print("  - libssl-dev: SSL development libraries")
        print("  - python3-dev: Python headers for compiling extensions")
        print("  - python3-pip: Python package installer")
        print("  - python3-venv: Python virtual environment support")

        packages = [
            "build-essential", "ca-certificates", "curl", "ffmpeg", "git",
            "libcurl4-openssl-dev", "libssl-dev", "python3-dev", "python3-pip", "python3-venv"
        ]

        # Update package list first
        run_command(["sudo", "apt", "update"], "Updating package list...")

        # Check what's already installed and install missing packages
        result = run_command(["dpkg", "-l"] + packages, "Checking installed packages...", check=False)
        missing = []
        installed_lines = result.stdout.split('\n')
        for pkg in packages:
            if not any(pkg in line and line.startswith('ii') for line in installed_lines):
                missing.append(pkg)

        if missing:
            run_command(["sudo", "apt", "install", "-y"] + missing, f"Installing missing packages: {' '.join(missing)}")

def install_ollama():
    """Install Ollama"""
    print("[3/15] Installing Ollama (optional AI tool)...")
    print("Installing/upgrading Ollama for local AI post-processing (optional, FREE, private)...")

    if shutil.which("ollama"):
        result = run_command(["ollama", "--version"], "Checking current Ollama version", check=False)
        current_version = "unknown"
        if result.returncode == 0:
            # Parse version - this might need adjustment based on actual output format
            output = result.stdout.strip()
            current_version = output.split()[-1] if len(output.split()) > 1 else "unknown"

        print(f"Current version: {current_version}")
        print("Checking for updates...")
    else:
        print("Installing Ollama...")

    if os_type == "macos":
        # macOS: Use Homebrew
        brew_outdated = run_command(["brew", "outdated", "ollama"], "Checking if Ollama needs upgrade", check=False)
        if brew_outdated.returncode == 0:
            print("Upgrading Ollama via Homebrew...")
            run_command(["brew", "upgrade", "ollama"], "Upgrading Ollama...")
        else:
            print("Ollama not installed or already up to date")

    elif os_type == "ubuntu":
        # Ubuntu: Use official installer script
        run_command("curl -fsSL https://ollama.com/install.sh | sh", "Installing Ollama via official script...")

    # Pull default model
    if shutil.which("ollama"):
        print("Starting Ollama service...")
        # Check if already running
        result = run_command(["pgrep", "-x", "ollama"], "Checking if Ollama service is running", check=False)
        if result.returncode != 0:
            # Start in background
            print("Starting Ollama service in background...")
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("Pulling Ollama model for qwen (lightweight: qwen2.5:7b)...")
        print("Note: Qwen requires NVIDIA GPU with 6GB+ VRAM for transcript processing")
        print("This will download ~4.7GB - may take 3-7 minutes depending on your internet speed...")
        print("")

        result = run_command(["ollama", "pull", "qwen2.5:7b"], "Downloading Ollama model qwen2.5:7b", check=False)
        if result.returncode == 0 and "success" in result.stdout.lower():
            print("✓ Model qwen2.5:7b downloaded")
        else:
            print("⚠ Model qwen2.5:7b pull completed (check with: ollama list)")

    print("")
    print("✓ Qwen 7B model ready (lightweight, stable):")
    print("  • Optimized for: RTX 5070, RTX 4060+, and similar GPUs (6GB+ VRAM)")
    print("  • Uses: ~5-6GB VRAM during processing")
    print("  • CPU-only systems: Qwen will be automatically skipped with warning")
    print("  • Performance: 15-30 seconds per transcript")

def main():
    global os_type

    parser = argparse.ArgumentParser(description="Python Environment Setup for WhisperX Transcription")
    parser.add_argument("--force-cpu", action="store_true",
                       help="Force CPU-only installation even if NVIDIA GPU is present")
    parser.add_argument("--start-step", type=int, default=0,
                       help="Start installation from specific step number (0-14)")
    args = parser.parse_args()
    start_step = args.start_step

    print("=" * 72)
    print("Python Environment Setup for WhisperX")
    if start_step > 0:
        print(f"Starting from step {start_step}")
    print("=" * 72)
    print()

    # Step 0: OS Detection - Always required
    if start_step <= 0:
        print("[0/15] Detecting operating system...")
    os_type, os_version, os_major = detect_os()

    if os_type == "macos":
        if os_major != 14:
            print(f"ERROR: Unsupported macOS version")
            print(f"This script requires macOS Sonoma (14.x)")
            print(f"Your version: {os_version}")
            sys.exit(1)
        if start_step <= 0:
            print("✓ macOS Sonoma detected")
            if not check_homebrew():
                print("ERROR: Homebrew not installed")
                print("Homebrew is required for macOS installations.")
                print("Install it from: https://brew.sh")
                print("Then run this script again.")
                sys.exit(1)
            print("✓ Homebrew is installed")
    elif os_type == "ubuntu":
        if os_version != "24.04":
            print("ERROR: Unsupported Ubuntu version")
            print("This script requires Ubuntu 24.04 LTS")
            print(f"Your version: {os_version}")
            sys.exit(1)
        if start_step <= 0:
            print("✓ Ubuntu 24.04 LTS detected")

    if start_step <= 0:
        print()

    # Step 1: Hardware Detection - Always required for later steps
    if start_step <= 1:
        print("[1/15] Detecting hardware...")
    force_cpu = args.force_cpu
    has_nvidia = detect_hardware(force_cpu)
    if start_step <= 1:
        print()

    # Step 2: System Dependencies
    if start_step <= 2:
        print(f"[2/15] Installing system dependencies...")
        install_system_dependencies()
        if start_step <= 2:
            print()

    # Step 3: Ollama (Optional AI tool)
    if start_step <= 3:
        print(f"[3/15] Installing Ollama (optional AI tool)...")
        install_ollama()
        print()

    # Step 4: Create Python virtual environment
    if start_step <= 4:
        print("[4/15] Creating Python virtual environment...")
        venv_path = Path.cwd() / "venv"
        if venv_path.exists():
            print(f"Virtual environment already exists at {venv_path}")
            print("Removing existing venv...")
            shutil.rmtree(venv_path)
        print(f"Creating new virtual environment at {venv_path}")
        run_command(["python3", "-m", "venv", str(venv_path)], "Creating virtual environment...")

        # Upgrade pip first
        python_exe = venv_path / "bin" / "python"
        run_command([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"], "Upgrading pip to latest version")
        if start_step <= 4:
            print()
    elif start_step > 4:
        # Resume: virtual environment should already exist from previous run
        venv_path = Path.cwd() / "venv"
        if not venv_path.exists():
            print(f"❌ ERROR: Virtual environment not found at {venv_path}")
            print("Cannot resume from step 9 without existing virtual environment.")
            print("Run from step 0 first to create the environment, or ensure venv/ exists.")
            sys.exit(1)
        python_exe = venv_path / "bin" / "python"

    if start_step <= 5:
        print("[5/15] Installing base packages...")
        print("Installing WhisperX, AI provider SDKs, and dependencies from requirements.txt")
        print("This may take 5-10 minutes...")
        run_command([str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"], "Installing requirements from requirements.txt")
        if start_step <= 5:
            print()

    if start_step <= 6:
        print("[6/15] Installing PyTorch 2.9.0...")
        print("Installing PyTorch 2.9.0 for consistency across platforms")

        if os_type == "ubuntu" and has_nvidia:
            print("Platform: Ubuntu with NVIDIA GPU - installing with CUDA 13.0 support")
            print("Provides full Blackwell (sm_120) support for RTX 50-series GPUs")
            print("This may take 2-5 minutes depending on internet speed...")
            run_command([str(python_exe), "-m", "pip", "install", "--force-reinstall", "--index-url", "https://download.pytorch.org/whl/cu130",
                       "torch==2.9.0", "torchvision==0.24.0", "torchaudio==2.9.0"], "Installing PyTorch 2.9.0 with CUDA 13.0 support")
        else:
            print("Platform: Ubuntu CPU or macOS - installing CPU-only version")
            run_command([str(python_exe), "-m", "pip", "install", "--force-reinstall", "--index-url", "https://download.pytorch.org/whl/cpu",
                       "torch==2.9.0", "torchvision==0.24.0", "torchaudio==2.9.0"], "Installing PyTorch 2.9.0 CPU-only version")
        if start_step <= 6:
            print()

    if start_step <= 7:
        print("[7/15] Verifying PyTorch installation...")

    try:
        result = run_command([str(python_exe), "scripts/pytorch_verify.py"], "Running PyTorch verification", check=True)
        output_lines = result.stdout.strip().split('\n')

        if "VERIFICATION_SUCCESS" in result.stdout:
            for line in output_lines:
                if line.startswith("PyTorch"):
                    print(f"✓ {line}")
                elif line.startswith("CUDA:"):
                    cuda_status = line.split(": ")[1]
                    print(f"✓ CUDA available: {cuda_status}")
                elif "test:" in line and "PASSED" in line:
                    test_type = line.split(":")[0]
                    print(f"✓ {test_type} verification completed")

            if has_nvidia and "CUDA: True" in result.stdout:
                print("✓ PyTorch verified - GPU ready")
            else:
                print("✓ PyTorch verified - CPU ready")
        else:
            print("❌ PyTorch verification failed - missing success marker")
            for line in output_lines:
                print(f"  {line}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ PyTorch verification script failed: {e}")
        sys.exit(1)

    if start_step <= 7:
        print()

    if start_step <= 8:
        # Step 8: Apply WhisperX patches
        print("[8/15] Applying WhisperX patches...")
        print("Updating WhisperX to use 'token' parameter for HuggingFace authentication")

        # Find the actual site-packages directory (handles any Python version)
    try:
        result = run_command([str(python_exe), "scripts/find_site_packages.py"], "Finding site-packages directory", check=True)
        if "SUCCESS" in result.stdout:
            site_packages = result.stdout.strip().split('\n')[0]
        else:
            print("❌ Failed to find site-packages directory")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error finding site-packages directory: {e}")
        sys.exit(1)

    whisperx_vads = os.path.join(site_packages, "whisperx", "vads", "pyannote.py")
    whisperx_asr = os.path.join(site_packages, "whisperx", "asr.py")

    if not os.path.exists(whisperx_vads):
        raise FileNotFoundError(f"WhisperX vads/pyannote.py not found at {whisperx_vads}")
    if not os.path.exists(whisperx_asr):
        raise FileNotFoundError(f"WhisperX asr.py not found at {whisperx_asr}")

    # Apply patches using Python file operations (avoid sed complexity)
    def apply_patch(file_path, old_text, new_text):
        with open(file_path, 'r') as f:
            content = f.read()
        if old_text in content:
            content = content.replace(old_text, new_text)  # Replace ALL occurrences
            with open(file_path, 'w') as f:
                f.write(content)
            return True
        return False

    # Apply vads patch: replace 'use_auth_token' with 'token'
    apply_patch(whisperx_vads, 'use_auth_token', 'token')

    # Apply ASR patch: replace 'use_auth_token=None' with 'token=None' on line ~412
    apply_patch(whisperx_asr, 'use_auth_token=None', 'token=None')

    # Verify patches - count how many 'use_auth_token' remain (should be 0)
    with open(whisperx_vads, 'r') as f:
        vads_content = f.read()
    vads_count = vads_content.count('use_auth_token')
    if vads_count != 0:
        raise AssertionError(f"Patch verification failed for vads/pyannote.py - {vads_count} instances of 'use_auth_token' remain")

    print("✓ WhisperX patches applied successfully")
    print()

    if start_step <= 9:
        # Step 9: Install pyannote.audio 4.0+
        print("[9/15] Installing pyannote.audio 4.0+...")
        print("Installing pyannote.audio 4.0+ for PyTorch 2.9.0 compatibility...")

        # Check if basic requirements are installed (like shell script step 5)
        # If resuming from step 9, we may have skipped coordinated requirements installation
        try:
            run_command([str(python_exe), "-c", "import whisperx"], "Checking if basic requirements are installed", check=False)
        except SystemExit:
            # Requirements not installed, install them first (like shell step 5)
            print("Installing coordinated dependencies from requirements.txt first...")
            run_command([str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"], "Installing coordinated requirements")
            print("Continuing with pyannote.audio installation...")

        # Check PyTorch version and upgrade if needed (like shell script step 6)
        result = run_command([str(python_exe), "-c", "import torch; print(torch.__version__[:3])"], "Checking PyTorch version")
        pytorch_version = result.stdout.strip()
        if pytorch_version != "2.9":
            print(f"PyTorch version {pytorch_version} found, upgrading to 2.9.0...")
            # Upgrade PyTorch like step 6
            if os_type == "ubuntu" and has_nvidia:
                run_command([str(python_exe), "-m", "pip", "install", "--force-reinstall", "--index-url", "https://download.pytorch.org/whl/cu130",
                           "torch==2.9.0", "torchvision==0.24.0", "torchaudio==2.9.0"], "Upgrading PyTorch to 2.9.0 with CUDA 13.0 support")
            else:
                run_command([str(python_exe), "-m", "pip", "install", "--force-reinstall", "--index-url", "https://download.pytorch.org/whl/cpu",
                           "torch==2.9.0", "torchvision==0.24.0", "torchaudio==2.9.0"], "Upgrading PyTorch to 2.9.0 CPU-only version")
            print("PyTorch upgrade complete. Continuing with pyannote.audio installation...")

        run_command([str(python_exe), "-m", "pip", "install", "--upgrade", "pyannote.audio>=4.0.0"], "Installing pyannote.audio 4.0+ for PyTorch 2.9.0 compatibility")
        print()

    if start_step <= 10:
        # Step 10: Apply SpeechBrain compatibility patches
        print("[10/15] Applying SpeechBrain compatibility patches...")
        print("Updating SpeechBrain for torchaudio 2.9.0 compatibility")

        speechbrain_backend = os.path.join(site_packages, "speechbrain", "utils", "torch_audio_backend.py")

        if not os.path.exists(speechbrain_backend):
            raise FileNotFoundError(f"SpeechBrain torch_audio_backend.py not found at {speechbrain_backend}")

        run_command([str(python_exe), "scripts/speechbrain_patch.py", speechbrain_backend], "Applying SpeechBrain compatibility patch")

    # Verify the patch - check that the new compatibility code was added
    result = run_command(["grep", "-q", 'hasattr(torchaudio, "list_audio_backends")', speechbrain_backend], "Verifying SpeechBrain patch", check=False)
    if result.returncode != 0:
        raise AssertionError("SpeechBrain patch verification failed - compatibility check not found")

    if start_step <= 10:
        print("✓ SpeechBrain compatibility patch applied successfully")
        print()

    if start_step <= 11:
        # Step 11: Verify package installations
        print("[11/15] Verifying package installations...")

        try:
            result = run_command([str(python_exe), "scripts/verify_packages.py"], "Running package verification", check=True)
            if "VERIFICATION_SUCCESS" in result.stdout:
                # Print the individual package results
                for line in result.stdout.strip().split('\n'):
                    if ": OK" in line:
                        print(f"✓ {line}")
                print("✓ All core packages verified")
            else:
                print("❌ Package verification failed")
                for line in result.stdout.strip().split('\n'):
                    print(f"  {line}")
                for line in result.stderr.strip().split('\n'):
                    if line:
                        print(f"  ❌ {line}")
                sys.exit(1)
        except Exception as e:
            print(f"❌ Package verification script failed: {e}")
            sys.exit(1)

        if start_step <= 11:
            print()

    if start_step <= 12:
        # Step 12: NVIDIA LD_LIBRARY_PATH configuration
        if has_nvidia:
            print("[12/15] Configuring LD_LIBRARY_PATH for NVIDIA...")
            nvidia_libs = "/usr/local/cuda/lib64:/usr/lib/x86_64-linux-gnu"
            os.environ["LD_LIBRARY_PATH"] = f"{nvidia_libs}:$LD_LIBRARY_PATH" if "LD_LIBRARY_PATH" in os.environ else nvidia_libs
            print(f"✓ Set LD_LIBRARY_PATH to include NVIDIA libraries: {nvidia_libs}")
        else:
            print("[12/15] Skipping NVIDIA configuration (CPU-only system)")
            print("✓ CPU configuration verified")
        if start_step <= 12:
            print()

    if start_step <= 13:
        # Step 13: Verify AI provider SDKs
        print("[13/15] Verifying AI provider SDKs...")
        print("Verifying packages installed from requirements.txt:")

        try:
            result = run_command([str(python_exe), "scripts/verify_ai_sdks.py"], "Running AI SDK verification", check=True)
            if "VERIFICATION_SUCCESS" in result.stdout:
                # Print the individual SDK results
                for line in result.stdout.strip().split('\n'):
                    if line.startswith("✓ "):
                        print(f"{line}")
                print("✓ All AI provider SDKs verified")
            else:
                print("❌ AI SDK verification failed")
                for line in result.stdout.strip().split('\n'):
                    print(f"  {line}")
                for line in result.stderr.strip().split('\n'):
                    if line:
                        print(f"  ❌ {line}")
                sys.exit(1)
        except Exception as e:
            print(f"❌ AI SDK verification script failed: {e}")
            sys.exit(1)

        if start_step <= 13:
            print()

    if start_step <= 14:
        # Step 14: Create project directories
        print("[14/15] Creating project directories...")
        print("Creating project directory structure...")
        intermediates_dir = Path.cwd() / "intermediates"
        outputs_dir = Path.cwd() / "outputs"
        intermediates_dir.mkdir(exist_ok=True)
        outputs_dir.mkdir(exist_ok=True)
        print("✓ Created intermediates/ and outputs/ directories")
        if start_step <= 14:
            print()

    if start_step <= 15:
        # Step 15: Environment file setup
        print("[15/15] Setting up environment configuration...")
        print("Checking for setup_env.sh (required for HuggingFace authentication)")
        setup_env_path = Path.cwd() / "setup_env.sh"
        if not setup_env_path.exists():
            example_path = Path.cwd() / "setup_env.sh.example"
            if example_path.exists():
                shutil.copy(example_path, setup_env_path)
                print("✓ Created setup_env.sh from example template")
                print("You'll need to edit this file to add your HuggingFace token")
            else:
                print("⚠ setup_env.sh.example not found - you'll need to create it manually")
        else:
            print("setup_env.sh already exists - skipping creation")
        if start_step <= 15:
            print()

    print("=" * 72)
    print("✓ Installation Complete!")
    print("=" * 72)
    print()
    print("MANUAL CONFIGURATION REQUIRED:")
    print()
    print("1. Get a HuggingFace token:")
    print("   https://huggingface.co/settings/tokens")
    print()
    print("2. Edit setup_env.sh and add your token:")
    if os_type == "macos":
        print("   nano setup_env.sh  (or use your preferred editor)")
    else:
        print("   nano setup_env.sh")

if __name__ == "__main__":
    main()
