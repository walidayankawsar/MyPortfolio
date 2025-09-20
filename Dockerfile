FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Static collect
RUN python manage.py collectstatic --noinput

# Expose port for Django
EXPOSE 8000

# Run Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




# Run with gunicorn (better for production)
CMD ["gunicorn", "Portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]



