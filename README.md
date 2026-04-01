# 🥊 Cross Fight API

Kickboxing platformasi uchun Django REST API.
Bu loyiha foydalanuvchilarni **Student / Teacher / Admin** rollariga ajratadi va JWT orqali autentifikatsiya qiladi.

---

## 🚀 Texnologiyalar

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL
* SimpleJWT (JWT Authentication)
* DRF Spectacular (Swagger UI)

---

## 👤 Foydalanuvchi rollari

| Role    | Imkoniyatlar                        |
| ------- | ----------------------------------- |
| Student | Ro‘yxatdan o‘tadi va tizimga kiradi |
| Teacher | Faqat Admin tomonidan yaratiladi    |
| Admin   | Barcha userlarni boshqaradi         |

---

## 🔐 Authentication

Loyihada JWT ishlatiladi:

* **Login** → access & refresh token beradi
* **Authorize** → Swagger orqali token bilan ishlash mumkin

---

## 📌 API Endpointlar

### 🔑 Auth

* `POST /api/register/`
  → Faqat **Student** sifatida ro‘yxatdan o‘tadi

* `POST /api/token/`
  → Login (JWT token olish)

---

### 👥 Users

* `GET /api/accounts/`
  → Admin: barcha userlar
  → Boshqalar: faqat o‘zi

* `POST /api/accounts/`
  → Admin: Teacher qo‘sha oladi
  → Student: faqat Student yaratadi

---

## ⚙️ O‘rnatish

### 1. Clone qilish

```bash
git clone https://github.com/your-username/crossfight-api.git
cd crossfight-api
```

---

### 2. Virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3. Paketlarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

### 4. .env fayl yaratish

```env
SECRET_KEY=your_secret_key
DEBUG=True

PG_DATABASE=postgres
PG_USER=postgres
PG_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Migratsiya

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Superuser yaratish

```bash
python manage.py createsuperuser
```

---

### 7. Serverni ishga tushirish

```bash
python manage.py runserver
```

---

## 📚 Swagger (API Docs)

Swagger UI:

```
http://127.0.0.1:8000/api/
```

---

## 🔑 Swagger orqali ishlash

1. `/api/token/` orqali login qiling
2. Access token oling
3. **Authorize** tugmasini bosing
4. Tokenni kiriting:

```
Bearer your_access_token
```

---

## 🧠 Business Logic

* ❗ Teacher’ni faqat **Admin** qo‘sha oladi
* ❗ Register faqat **Student** uchun
* ❗ Har bir user faqat o‘zini ko‘radi (Admin bundan mustasno)

---

## 📁 Loyihaning tuzilishi

```
account/
    models.py
    serializers.py
    views.py
    urls.py

config/
    settings.py
    urls.py
```

---

## 🛠 Kelajakdagi imkoniyatlar

* Course / Training moduli
* Payment integration
* Notification system
* Role-based permissions kengaytirish

---

## 👨‍💻 Muallif

**Sen 😎**
Agar savol bo‘lsa bemalol yoz!

---
