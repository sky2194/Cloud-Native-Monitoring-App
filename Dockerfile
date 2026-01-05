## Dockerfile for the Cloud Native Application

## Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code(. . means copy everything in the current directory)
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]