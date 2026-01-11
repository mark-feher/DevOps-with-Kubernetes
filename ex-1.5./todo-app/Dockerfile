# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./src/app.py .

# Set default environment variables
# ENV PORT=3030
# EXPOSE 3030

# Use flask's built-in server
CMD ["python", "app.py"]
