#!/bin/bash

# Check if there's an active virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    # No active venv found

    # Create a new virtual environment
    python3 -m venv myenv

    # Activate the virtual environment
    source myenv/bin/activate

    # Install packages from requirements.txt
    pip install -r requirements.txt

    echo "Virtual environment setup complete!"
else
    echo "There's already an active virtual environment. Please deactivate it before running this script."
fi
