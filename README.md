<div align="center">

<img src="docs/assets/ai-studymate-banner.png" alt="AI StudyMate Banner" width="100%">

# AI StudyMate

**Your AI-Powered Learning Companion for IT Students**

Aplikasi pembelajaran berbasis AI yang membantu mahasiswa Informatika dan bidang IT memahami materi kuliah melalui dokumen, rangkuman, percakapan berbasis sumber, dan kuis interaktif.

[Fitur](#-fitur-utama) · [Teknologi](#-teknologi) · [Menjalankan Proyek](#-menjalankan-proyek) · [Tim](#-tim-pengembang) · [Kontribusi](#-workflow-git-dan-kontribusi)

</div>

---

## Tentang Proyek

AI StudyMate adalah aplikasi pembelajaran untuk mahasiswa Informatika dan bidang IT. Pengguna direncanakan dapat mengunggah dokumen pembelajaran, bertanya berdasarkan isi materi, membuat rangkuman, dan berlatih melalui kuis. Jawaban AI diharapkan menyertakan referensi ke materi sumber bila tersedia.

Proyek ini dikembangkan oleh tim mahasiswa untuk menerapkan pengembangan web, mobile, backend, database, integrasi AI, dan quality assurance dalam satu aplikasi.

> **Status: dalam pengembangan.** Fitur dan roadmap di bawah adalah target proyek, bukan jaminan sudah selesai. Verifikasi terhadap implementasi terbaru.

## 🎯 Tujuan

- Membantu mahasiswa IT memahami materi perkuliahan.
- Mempermudah pengelolaan dokumen pembelajaran.
- Menyediakan rangkuman dan latihan soal dari materi yang dipelajari.
- Mendorong penggunaan AI yang mengacu pada sumber materi, bukan sekadar jawaban tanpa konteks.
- Menjadi proyek portofolio kolaboratif yang menerapkan praktik pengembangan perangkat lunak.

## ✨ Fitur Utama

| Fitur | Deskripsi | Platform |
| --- | --- | --- |
| Autentikasi pengguna | Registrasi/login dan pengelolaan sesi | Web & Android |
| Pustaka dokumen | Mengunggah dan melihat dokumen pembelajaran | Web & Android |
| Ekstraksi materi | Mengambil teks dari dokumen yang didukung | Backend |
| AI chat berbasis dokumen | Bertanya berdasarkan materi yang dipilih | Web & Android |
| Referensi sumber | Menampilkan kutipan/referensi materi bila tersedia dari sistem AI | Web & Android |
| Rangkuman otomatis | Membuat rangkuman dari materi | Web & Android |
| Generator kuis | Menghasilkan pertanyaan latihan dari materi | Web & Android |
| Penilaian kuis | Memeriksa jawaban dan menampilkan hasil sesuai respons backend | Web & Android |
| Riwayat belajar | Melihat aktivitas belajar sebelumnya bila data riwayat tersedia | Web & Android |
| Tema tampilan | Pilihan tema terang dan gelap | Web & Android |

## 🧰 Teknologi

| Bagian | Teknologi |
| --- | --- |
| Backend API | Python, FastAPI |
| Web | React |
| Android | Flutter, Dart |
| Database | PostgreSQL |
| AI | Provider/model AI yang dikonfigurasi lewat environment |
| Version control | Git & GitHub |

Versi bahasa, framework, dan dependensi mengikuti file konfigurasi di masing-masing direktori.

## 🏗️ Arsitektur

```text
┌─────────────────────┐       ┌─────────────────────┐
│     Web (React)     │       │  Android (Flutter)  │
└──────────┬──────────┘       └──────────┬──────────┘
           │                             │
           └──────────────┬──────────────┘
                          │ HTTP API
                          ▼
                ┌──────────────────┐
                │ Backend FastAPI  │
                │ Auth, Documents, │
                │ Chat, Summary,   │
                │ Quiz             │
                └────────┬─────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
    ┌─────────────────┐    ┌─────────────────┐
    │   PostgreSQL    │    │   AI Provider   │
    │ User & Learning │    │  AI Processing  │
    │ Data            │    │                 │
    └─────────────────┘    └─────────────────┘
```

Diagram ini adalah rancangan konseptual; detail layanan, penyimpanan file, dan alur AI mengikuti implementasi aktual.

## 📁 Struktur Repository

```text
AIStudy/
├── backend/        # FastAPI backend
│   ├── app/
│   ├── tests/
│   └── requirements.txt
├── web/            # React web application
│   ├── src/
│   └── package.json
├── android/        # Flutter application
│   ├── lib/
│   ├── test/
│   └── pubspec.yaml
├── database/       # Skema, migration, dokumentasi database
├── docs/           # Dokumentasi API, desain, dan panduan
├── .gitignore
└── README.md
```

> Struktur di atas adalah susunan yang disarankan. Sesuaikan dengan direktori yang benar-benar ada.

## 🚀 Menjalankan Proyek

### Prasyarat

- Git
- Python (sesuai konfigurasi backend)
- Node.js dan npm (sesuai aplikasi web)
- Flutter SDK dan Android SDK (aplikasi Android)
- PostgreSQL
- API key AI provider, jika fitur AI memerlukannya

### 1. Clone repository

```bash
git clone https://github.com/NoxSans24/AIStudy.git
cd AIStudy
```

### 2. Backend (FastAPI)

```bash
cd backend
python -m venv .venv
```

Aktifkan virtual environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
source .venv/bin/activate
```

Pasang dependensi dan jalankan server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Salin `.env.example` (jika ada) menjadi `.env`, lalu isi konfigurasi lokal: database, secret autentikasi, dan AI provider. **Jangan commit `.env` atau secret ke Git.** Jika entry point berbeda dari `app.main:app`, ikuti instruksi di direktori `backend`.

### 3. Web (React)

Di terminal baru:

```bash
cd web
npm install
npm run dev
```

Buat file environment lokal dengan nama variabel yang didefinisikan proyek. Jika script berbeda, cek bagian `scripts` di `package.json`.

### 4. Android (Flutter)

Di terminal baru:

```bash
cd android
flutter pub get
flutter doctor
flutter run
```

Pastikan emulator atau perangkat Android tersedia, lalu atur base URL backend sesuai konfigurasi aplikasi. Di emulator Android, `localhost` menunjuk ke emulator itu sendiri, bukan komputer host; gunakan alamat host yang sesuai (umumnya `10.0.2.2`).

### 5. Database (PostgreSQL)

1. Jalankan layanan PostgreSQL.
2. Buat database development sesuai konfigurasi proyek.
3. Atur koneksi melalui environment variable.
4. Jalankan migration dengan tool yang dipakai repository (perintah belum dicantumkan karena bergantung pada tool tersebut).
5. Gunakan data uji, bukan data pribadi atau produksi.

## 🔐 Konfigurasi dan Keamanan

- Jangan commit `.env`, password, token, API key, private key, atau keystore.
- Sediakan `.env.example` yang hanya berisi nama variabel dan contoh nilai non-rahasia.
- Simpan password dengan hashing; jangan menyimpan password asli.
- Backend harus memverifikasi kepemilikan data pada setiap endpoint yang relevan, bukan mengandalkan pembatasan tampilan UI.
- Validasi tipe, ukuran, dan isi file yang diunggah.
- Gunakan HTTPS untuk deployment dan batasi CORS pada origin yang diperlukan.
- Jangan mencantumkan secret di log, screenshot, issue, atau dokumentasi publik.

## 🌿 Workflow Git dan Kontribusi

Setiap perubahan dikerjakan di branch terpisah dan ditinjau lewat Pull Request sebelum digabungkan.

1. Pilih issue yang ditugaskan di GitHub Project dan pahami dependensinya.
2. Tarik perubahan terbaru dari `main`.
3. Buat branch untuk pekerjaan.
4. Implementasikan perubahan dan jalankan pemeriksaan yang relevan.
5. Commit dan push branch.
6. Buat Pull Request dan tautkan issue.
7. Minta review anggota tim.
8. Merge setelah review dan pemeriksaan lolos.
9. Perbarui status issue sesuai progres sebenarnya.

```bash
git switch main
git pull origin main
git switch -c feature/nama-fitur

# kerjakan perubahan, lalu:
git add .
git commit -m "feat: deskripsi perubahan"
git push -u origin feature/nama-fitur
```

Hindari bekerja langsung di `main`, force push tanpa koordinasi, atau memasukkan perubahan anggota lain tanpa review.

### Konvensi commit

```text
feat: add document upload endpoint
fix: handle expired access token
test: add document access tests
docs: update local setup guide
refactor: organize API service layer
```

## 👥 Tim Pengembang

<!-- TODO: ganti "Member 1-4" dengan nama dan profil GitHub anggota tim -->

| Peran | Tanggung jawab |
| --- | --- |
| Member 1 — Backend & AI | FastAPI, autentikasi backend, API, pemrosesan dokumen, integrasi AI |
| Member 2 — Web Developer | React, antarmuka web, routing, integrasi API |
| Member 3 — Android Developer | Flutter, antarmuka Android, navigasi, integrasi API |
| Member 4 — Database, QA & Integrasi | Skema/migration database bersama backend, pengujian, integrasi, dokumentasi |

Seluruh anggota menjaga kualitas kode, memperbarui issue, melakukan review, dan membantu integrasi lintas komponen.

## 🧪 Testing

- **Backend:** unit test, integration test API, validasi input, autentikasi, isolasi data pengguna.
- **Web:** build, alur login, integrasi API, loading/error state, responsivitas.
- **Android:** analisis Flutter, widget test, alur navigasi, integrasi API, uji perangkat.
- **AI:** kesesuaian jawaban dengan dokumen sumber, relevansi referensi, kualitas rangkuman, ketepatan kunci jawaban kuis.

Catat hanya hasil pengujian yang benar-benar dijalankan; jangan menyatakan fitur lulus tanpa bukti.

## 🗺️ Roadmap

- [ ] **Week 1 — Fondasi:** repository, kontrak API, database, kerangka backend/web/Android.
- [ ] **Week 2 — Core features:** autentikasi, upload dokumen, ekstraksi materi, fitur AI awal.
- [ ] **Week 3 — Integrasi:** chat, rangkuman, kuis, integrasi web/Android, perbaikan awal.
- [ ] **Week 4 — Release:** QA, keamanan, deployment, build APK, dokumentasi, demo.

Jika waktu tidak cukup, prioritaskan alur MVP yang benar-benar berfungsi.

## 📌 Status dan Dokumentasi

- Repository: <https://github.com/NoxSans24/AIStudy>
- Issue tracker: <https://github.com/NoxSans24/AIStudy/issues>
- Project board: lihat GitHub Projects yang digunakan tim
- Dokumentasi API: _tambahkan tautan setelah tersedia_
- Web demo / APK: _tambahkan tautan setelah deployment dan build tersedia_

## 📄 Lisensi

Lisensi belum ditentukan. Tambahkan file `LICENSE` dan perbarui bagian ini setelah tim menyepakati lisensi.

<div align="center">

AI StudyMate · Built collaboratively by an Informatics student team

</div>
