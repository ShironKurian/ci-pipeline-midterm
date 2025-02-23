# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app and test files
COPY app/ app/
COPY tests/ tests/
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app/app.py"]