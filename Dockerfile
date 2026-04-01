# 1. Baza image
FROM python:3.12-slim

# 2. Ishchi papka
WORKDIR /app

# 3. Tizim paketlari (psycopg2 uchun kerak)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Requirements ni avval ko'chiramiz (cache uchun)
COPY requirements.txt .

# 5. Python paketlarini o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 6. Loyiha kodini ko'chiramiz
COPY . .

# 7. entrypoint.sh ni bajarish huquqi beramiz
RUN chmod +x /app/entrypoint.sh

# 8. Static fayllarni yig'amiz (ixtiyoriy — environment variable kerak bo'lsa skip qilish mumkin)
# RUN python manage.py collectstatic --noinput

# 9. Entrypoint va CMD
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8004", "--workers", "2", "config.wsgi:application"]