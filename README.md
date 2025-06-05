# 🎬 Film Log – Aplikasi Web Manajemen Film

Film Log adalah aplikasi web sederhana berbasis Django yang memungkinkan pengguna umum untuk melihat daftar dan detail film, serta menyediakan dashboard khusus admin untuk mengelola data film, genre, dan ulasan (review).

## 📺 Link Video dan PPT
#### Tonton video demo di YouTube: https://youtu.be/H4Vb64R20lo
#### Link PPT : https://drive.google.com/file/d/1MBjPBwXlCoMOFWJQB7SUyhg8N3kx9Z8F/view?usp=sharing

## 💡 Fitur Utama
### 🎯 Untuk User Umum
- Landing page daftar film
- Halaman detail film (judul, genre, deskripsi, tanggal rilis, gambar)
- Dapat melihat review dan rating dari pengguna lain

### 🔐 Untuk Admin
- Login admin (via Django Admin)
- CRUD data film
- CRUD data genre
- CRUD data review

---

## ⚙️ Teknologi

- Backend: [Django 5.2.1](https://www.djangoproject.com/)
- Database: SQLite3 (default Django)
- Auth: Django default auth (superuser login)

---

## 🛠️ Panduan Instalasi

1. **Clone repository**
```bash
git clone https://github.com/meutiaaini/FinalProject.git
cd filmlog
```

2. **Buat virtual environment & aktifkan**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Jalankan migrasi**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Buat superuser (admin)**
```bash
python manage.py createsuperuser
```

6. **Jalankan server**
```bash
python manage.py runserver
```

## 🔑 Login Admin
- Akses admin di: http://127.0.0.1:8000/admin/
- Masukkan username & password superuser yang sudah dibuat


