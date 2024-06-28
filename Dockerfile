# Use Python 3.11 base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the files to the container
COPY . .

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=rentEase.settings

# Expose port 8000 to access the application
EXPOSE 8000

