# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (optional, if you use them)
RUN python manage.py collectstatic --noinput || true

# Expose port (default Django port)
EXPOSE 8000

# Run the server
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
