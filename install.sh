#!/bin/bash

# Claude Master Skills One-Line Installer
echo "🚀 Running Claude Master Skills Installer..."

if ! command -v python3 &> /dev/null
then
    echo "❌ Error: Python 3 is not installed. Please install it to continue."
    exit
fi

python3 setup.py "$@"
