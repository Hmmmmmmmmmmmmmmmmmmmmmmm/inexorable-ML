FROM python:3.10-slim

# ENV FLASK_APP = app.py

# ENV FLASK_RUN_HOST=0.0.0.0

# # Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# # Prevent Python buffering logs
ENV PYTHONUNBUFFERED=1

# # Set working directory
WORKDIR /app

# # Copy dependency file first (Docker caching optimization)
COPY requirements_c_app.txt .

# # Install dependencies
RUN pip install --no-cache-dir -r requirements_c_app.txt

# # Copy project
COPY . .

# # Default web port
EXPOSE 8000

# # Start command (change depending on framework)
# CMD ["python", "app.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
