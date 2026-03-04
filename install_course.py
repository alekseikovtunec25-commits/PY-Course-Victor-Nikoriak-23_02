import subprocess
import sys
import os
from pathlib import Path

VENV = Path(".venv")


def run(cmd):
    subprocess.check_call(cmd)


if not VENV.exists():
    print("Creating virtual environment...")
    run([sys.executable, "-m", "venv", ".venv"])

if os.name == "nt":
    pip = ".venv\\Scripts\\pip.exe"
else:
    pip = ".venv/bin/pip"

print("Installing dependencies...")
run([pip, "install", "--upgrade", "pip"])
run([pip, "install", "-r", "requirements.txt"])

print("Done.")
