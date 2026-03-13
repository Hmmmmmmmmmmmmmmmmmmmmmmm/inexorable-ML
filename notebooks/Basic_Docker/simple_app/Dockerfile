FROM python:3.10-alpine

COPY . /simple_app
WORKDIR /simple_app

RUN pip install -r requirements_app.txt

EXPOSE 5000

# CMD run app.py
CMD ["python", "app.py"]




# Notes:

# Putting It All Together
# Your Dockerfile workflow becomes:

# Step 1 — Start with Python environment
# FROM python:3.10-alpine
# Step 2 — Add your project files
# COPY . /simple_app
# Step 3 — Set working directory
# WORKDIR /simple_app
# Step 4 — Install dependencies
# RUN pip install -r requirements_app.txt
# Step 5 — Start the app
# CMD ["python", "app.py"]


# Layer 1: Linux (Alpine)
# Layer 2: Python 3.10
# Layer 3: Project files
# Layer 4: Python dependencies
# Layer 5: Start command


# Universal Python Web App Dockerfile:


# FROM python:3.11-slim

# # Prevent Python from writing pyc files
# ENV PYTHONDONTWRITEBYTECODE=1

# # Prevent Python buffering logs
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Copy dependency file first (Docker caching optimization)
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project
# COPY . .

# # Default web port
# EXPOSE 8000

# # Start command (change depending on framework)
# CMD ["python", "app.py"]