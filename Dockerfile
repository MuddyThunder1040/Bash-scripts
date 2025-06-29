# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
    && pip install pytest pytest-cov

# Run pytest as health check (optional)
CMD ["pytest", "-v"]
