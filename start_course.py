import os
import re
import sys
import subprocess
import webbrowser
from pathlib import Path

PORT = 8891


def find_lessons():
    lessons = {}
    for nb in Path(".").rglob("*_student.ipynb"):
        folder = nb.parent.name
        match = re.match(r"(\d+)_", folder)
        if match:
            number = int(match.group(1))
            lessons[number] = nb
    return dict(sorted(lessons.items()))


def get_python():
    if os.name == "nt":
        return ".venv\\Scripts\\python.exe"
    return ".venv/bin/python"


if not Path(".venv").exists():
    print("Environment not found. Run install_course.py first.")
    sys.exit(1)

lessons = find_lessons()

if not lessons:
    print("No lessons found.")
    sys.exit(1)

print("\nAvailable lessons:")
for num in lessons:
    print(f"[{num}] {lessons[num]}")

choice = input("\nEnter lesson number: ")

if not choice.isdigit() or int(choice) not in lessons:
    print("Invalid choice.")
    sys.exit(1)

notebook = str(lessons[int(choice)])

print(f"\nLaunching on http://localhost:{PORT}\n")
webbrowser.open(f"http://localhost:{PORT}/")

subprocess.run([
    get_python(),
    "-m",
    "voila",
    notebook,
    f"--port={PORT}"
])
