FROM python:3.9-slim

# Prevent Python from writing .pyc files and buffer-free terminal output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy and install the Python dependencies first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Document the Flask application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]