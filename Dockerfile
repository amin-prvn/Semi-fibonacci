# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the Python code into the container
COPY app.py .

# Run the script when the container starts
CMD ["python", "app.py"]