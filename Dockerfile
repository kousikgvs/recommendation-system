# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY dataset/ ./dataset/
COPY dataset_cleaned/ ./dataset_cleaned/

# Expose port (if needed)
EXPOSE 8000

# Run the application
CMD [ "python", "-m", "src.main" ]