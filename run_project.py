#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def projects():
    items = []
    for p in sorted(ROOT.iterdir()):
        if p.is_dir() and p.name[:2].isdigit() and p.name[2] == "_":
            try:
                n = int(p.name[:2])
                items.append((n, p))
            except ValueError:
                pass
    return sorted(items)

def run(cmd, cwd):
    print("\n$", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd).returncode

def main():
    items = projects()

    print("\n" + "=" * 60)
    print("        AI TOOLBOX - MINI PROJECT LAUNCHER")
    print("=" * 60)

    for n, p in items:
        print(f"{n:02d}. {p.name[3:].replace('_', ' ')}")

    print("\n0. Exit")
    choice = input("\nSelect project (1-29): ").strip()

    if choice == "0":
        return

    if not choice.isdigit() or int(choice) not in [n for n, _ in items]:
        print("❌ Invalid selection.")
        return

    n = int(choice)
    project = dict(items)[n]
    venv = project / ".venv"
    python = venv / "bin" / "python"

    print(f"\n📁 Selected: {project.name}")

    # Create isolated venv
    if not venv.exists():
        print("🔧 Creating virtual environment...")
        rc = run([sys.executable, "-m", "venv", ".venv"], project)
        if rc != 0:
            print("❌ Could not create virtual environment.")
            return

    if not python.exists():
        print("❌ Python executable not found inside .venv.")
        return

    # Upgrade pip
    print("⬆️ Updating pip...")
    run([str(python), "-m", "pip", "install", "--upgrade", "pip"], project)

    # Install requirements
    requirements = project / "requirements.txt"
    if requirements.exists():
        print("📦 Installing requirements...")
        rc = run([str(python), "-m", "pip", "install", "-r", "requirements.txt"], project)
        if rc != 0:
            print("\n⚠️ Dependency installation failed.")
            print("Read the project's README.md for extra setup requirements.")
            return

    # Special instructions
    special = {
        4: "Kafka must be running on localhost:9092. Run consumer.py in one terminal and producer.py in another.",
        5: "Airflow is a service/DAG workflow. Put the DAG under your Airflow dags folder and run it through Airflow.",
        15: "MCP project is a server. Run server.py and connect it from an MCP-compatible client.",
        28: "Tesseract OCR engine must also be installed/configured in the Codespace.",
        29: "PaddleOCR may require additional runtime packages depending on the Codespace image.",
    }

    if n in special:
        print(f"\n⚠️ NOTE: {special[n]}")

    # Find runnable Python file
    candidates = []
    for name in ["main.py", "producer.py", "server.py"]:
        f = project / name
        if f.exists():
            candidates.append(f)

    if not candidates:
        print("\nℹ️ No automatic main.py runner found.")
        return

    script = candidates[0]
    print(f"\n🚀 Running {script.name}...\n")
    rc = run([str(python), script.name], project)

    print("\n" + "=" * 60)
    if rc == 0:
        print("✅ PROJECT FINISHED")
    else:
        print(f"⚠️ PROJECT EXITED WITH CODE {rc}")
    print("=" * 60)

if __name__ == "__main__":
    main()
