# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create a directory for your Python script
WORKDIR /app

# Copy the Python script into the container
COPY . /app

RUN pip install -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "DSscraper.py"]

