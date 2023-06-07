# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY server.py .

# Expose the port on which the server will run
EXPOSE 8000

# Run the Python script when the container starts
CMD ["python", "main.py"]
