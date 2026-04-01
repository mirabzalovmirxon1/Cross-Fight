#!/bin/sh

echo "⏳ Waiting for database..."

# Postgres tayyor bo‘lishini kutadi

while ! nc -z $DB_HOST $DB_PORT; do
sleep 1
done

echo "✅ Database is ready!"

# Migratsiyalar

echo "📦 Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Static collect (agar kerak bo‘lsa)

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Superuser avtomatik yaratish (ixtiyoriy)

if [ "$DJANGO_SUPERUSER_EMAIL" ]; then
echo "👤 Creating superuser..."
python manage.py createsuperuser 
--email $DJANGO_SUPERUSER_EMAIL 
--noinput || true
fi

echo "🚀 Starting server..."

# Gunicorn yoki runserver

exec "$@"
