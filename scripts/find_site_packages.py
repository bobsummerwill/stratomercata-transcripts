#!/usr/bin/env python3
"""
Find site-packages directory for installation verification.

Used by install_packages_and_venv.py to verify site-packages location.
Usage: python scripts/find_site_packages.py
"""

import site

try:
    site_packages = site.getsitepackages()[0]
    print(site_packages)
    print("SUCCESS")
except Exception as e:
    print(f"ERROR: {e}", file=__import__("sys").stderr)
    exit(1)
