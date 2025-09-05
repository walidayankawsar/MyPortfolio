# Python base image
FROM python:3.11-slim

# Workdir সেট করা
WORKDIR /app

# Dependencies কপি করা
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# প্রোজেক্ট ফাইল কপি করা
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# App run করার জন্য default command
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]