# Use the official Python image as the base image
FROM python:3.14-rc-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask application code into the container
COPY . .

# Set the environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app when the container starts
CMD flask run -h 0.0.0.0 -p 5000