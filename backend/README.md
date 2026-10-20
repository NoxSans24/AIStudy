# AI StudyMate — Backend

Backend AI StudyMate dibangun menggunakan Python dan FastAPI sebagai fondasi API untuk aplikasi pembelajaran.

## Teknologi

- Python
- FastAPI
- Uvicorn

## Persyaratan
Pastikan Python sudah terpasang di komputer. Periksa versi Python dengan:

`python --version`

## Instalasi

Jalankan perintah berikut dari direktori root repository `AIStudy`.

### 1. Buat virtual environment
`python -m venv backend/.venv`

### 2. Aktifkan virtual environment
`.\backend\.venv\Scripts\Activate.ps1`

### 3. Instal dependensi
`python -m pip install -r backend/requirements.txt`

## Menjalankan Server

Pastikan terminal berada di direktori root repository dan virtual environment sudah aktif.

Jalankan:

`python -m uvicorn app.main:app --app-dir backend --reload`

Server akan tersedia di:

- API: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/health
- Dokumentasi API: http://127.0.0.1:8000/docs

## Health Check

Endpoint `GET /health` digunakan untuk memeriksa apakah backend berjalan.

Contoh respons:

```json
{
  "status": "ok"
}
```

## Konfigurasi Environment
Salin file `.env.example` menjadi `.env` jika konfigurasi environment lokal diperlukan.

`Copy-Item backend/.env.example backend/.env`

Jangan memasukkan kredensial, API key, atau informasi rahasia ke repository. File `.env` harus tetap diabaikan oleh Git.

## Catatan Pengembangan

Backend ini masih merupakan fondasi awal. Autentikasi, database, upload dokumen, dan integrasi AI akan dikembangkan melalui issue terpisah.

## Testing

Jalankan perintah berikut dari direktori root repository `AIStudy`:

```powershell
python -m pytest backend/tests -v
```

Tes saat ini mencakup pemeriksaan endpoint health check.