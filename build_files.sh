#!/bin/bash
echo "Building the project..."

# Python packages install
python3 -m pip install -r requirements.txt --break-system-packages

# Force folder creation
mkdir -p staticfiles_build

# Clear and collect static files
python3 manage.py collectstatic --noinput --clear

echo "Build completed!"