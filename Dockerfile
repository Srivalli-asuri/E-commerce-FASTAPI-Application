FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required for argon2 + psycopg
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt


# Copy your env file properly
COPY .env /app/.env

# Copy application
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



























# # Use an official lightweight Python runtime as a base image
# FROM python:3.11-slim AS base

# # Set environment variables to make Python behave well in containers
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Create a non-root user and app directory
# RUN adduser --disabled-password --gecos "" appuser
# WORKDIR /app

# # Install system dependencies required by psycopg2 and argon2 (if needed)
# # keep packages minimal to reduce image size
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements first to leverage Docker cache
# COPY requirements.txt /app/requirements.txt

# # Install Python dependencies
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r /app/requirements.txt

# # Copy application code
# COPY . /app

# # Make sure files are owned by non-root user
# RUN chown -R appuser:appuser /app
# USER appuser

# # Expose the port the app will listen on
# EXPOSE 8000

# # Default command (use uvicorn production-ready args)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]
