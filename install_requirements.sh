#!/bin/bash
# Script to install all the requirements from the requirements.txt

# Check if requirements.txt file exists
if [[ -f "requirements.txt" ]]; then
    echo "requirements.txt found. Installing requirements..."

    # Upgrade pip to the latest version
    echo "Upgrading pip..."
    python3 -m pip install --upgrade pip

    # Install requirements from requirements.txt
    echo "Installing requirements..."
    pip install -r requirements.txt
(not tested)
    echo "All requirements installed."
else
    echo "requirements.txt not found. Please make sure the file exists in the current directory."
    exit 1
fi
