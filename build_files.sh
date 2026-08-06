#!/bin/bash
echo "Building the project..."

# Python dependencies install
python3 -m pip install -r requirements.txt

# Static files collect (NO --clear flag)
python3 manage.py collectstatic --noinput

echo "Build completed!"