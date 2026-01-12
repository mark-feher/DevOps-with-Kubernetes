FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY ./src/app.py .

# Run the script
CMD ["python", "app.py"]
