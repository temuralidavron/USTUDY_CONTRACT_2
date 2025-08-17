# Rasmiy Python bazaviy image
FROM python:3.11-slim

# Ishchi katalog
WORKDIR /app

# System package larni o‘rnatish
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ni copy qilish
COPY requirments.txt .

# Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirments.txt

# Loyihani copy qilish
COPY . .

# Django serverni run qilish uchun default command
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
