FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Expose port for Django
EXPOSE 8000

# Run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]











# alpine destrubation er vitore python packaeg install korbe (python base image)
#FROM python:alpine
# amr project to (.) mane root dir er /Protfolio name akta folder create kore copy kore rakhbe.
#COPY . /Portfolio
# amr project ta kon dir theke khujbe ta define kore dicci
#WORKDIR /Portfolio
# command
#CMD python manage.py runserver









# Python base image
#FROM python:3.11-slim

# Dependencies কপি করা
#COPY requirements.txt .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt


# Collect static files
#RUN python manage.py collectstatic --noinput

# App run করার জন্য default command
#CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]