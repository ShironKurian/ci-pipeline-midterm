# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variable for Flask app location
ENV FLASK_APP=app/app.py

# Run the Flask app when the container launches
CMD ["python", "app/app.py"]