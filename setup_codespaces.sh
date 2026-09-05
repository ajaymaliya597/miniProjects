#!/usr/bin/env bash
set -e

echo "=========================================="
echo " AI TOOLBOX - CODESPACES SETUP"
echo "=========================================="

python3 --version

echo ""
echo "Creating isolated virtual environments only when a project is selected."
echo "Use the launcher instead:"
echo ""
echo "    python3 run_project.py"
echo ""
echo "Then choose 1-29."
echo ""
echo "This avoids installing all 29 projects and causing dependency conflicts."
