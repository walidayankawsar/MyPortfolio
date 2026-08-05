#!/bin/bash
echo "Building the project..."

# pip install এর সাথে --break-system-packages ফ্ল্যাগ যোগ করুন
python3 -m pip install -r requirements.txt --break-system-packages

# Static files সংগ্রহ করুন
python3 manage.py collectstatic --noinput --clear

python3 manage.py migrate

echo "Build completed!"