#!/bin/bash
echo "Building the project..."

# Force install python packages
python3 -m pip install -r requirements.txt --break-system-packages

# Collect static files
python3 manage.py collectstatic --noinput

echo "Build completed!"