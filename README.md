<div align="center">

AI StudyMate
Your AI-Powered Learning Companion for IT Students
Aplikasi pembelajaran berbasis AI yang membantu mahasiswa Informatika dan bidang IT memahami materi kuliah melalui dokumen, rangkuman, percakapan berbasis sumber, dan kuis interaktif.
<!-- Ganti URL berikut setelah aset tersedia di repository -->
<!-- <img src="docs/assets/ai-studymate-banner.png" alt="AI StudyMate Banner" width="100%"> -->

Features · Tech Stack · Getting Started · Team · Contributing
</div>

Tentang Proyek
AI StudyMate adalah proyek aplikasi pembelajaran untuk mahasiswa Informatika dan bidang IT. Aplikasi ini dirancang untuk membantu pengguna mempelajari materi secara lebih terstruktur dengan memanfaatkan kecerdasan buatan (AI).
Pengguna direncanakan dapat mengunggah dokumen pembelajaran, bertanya berdasarkan isi materi, membuat rangkuman, dan berlatih melalui kuis. Jawaban AI diharapkan menyertakan referensi ke materi sumber apabila informasi tersebut tersedia.
Proyek ini dikembangkan sebagai proyek kolaborasi tim mahasiswa untuk menerapkan pengembangan web, mobile, backend, database, integrasi AI, dan quality assurance dalam satu aplikasi.
Status proyek: Dalam pengembangan. Daftar fitur di bawah merupakan target proyek; ketersediaan setiap fitur harus diverifikasi terhadap implementasi terbaru.

🎯 Tujuan
- Membantu mahasiswa IT memahami materi perkuliahan.
- Mempermudah pengelolaan dokumen pembelajaran.
- Menyediakan rangkuman dan latihan soal dari materi yang dipelajari.
- Mendorong penggunaan AI yang mengacu pada sumber materi, bukan sekadar menghasilkan jawaban tanpa konteks.
- Menjadi proyek portofolio kolaboratif yang menerapkan praktik pengembangan perangkat lunak.
✨ Fitur Utama
Fitur	Deskripsi	Target platform
Autentikasi pengguna	Registrasi/login dan pengelolaan sesi pengguna.	Web & Android
Pustaka dokumen	Mengunggah dan melihat dokumen pembelajaran.	Web & Android
Ekstraksi materi	Mengambil teks dari dokumen yang didukung.	Backend
AI chat berbasis dokumen	Mengajukan pertanyaan berdasarkan materi yang dipilih.	Web & Android
Referensi sumber	Menampilkan kutipan atau referensi materi jika tersedia dari sistem AI.	Web & Android
Rangkuman otomatis	Membuat rangkuman dari materi pembelajaran.	Web & Android
Generator kuis	Menghasilkan pertanyaan latihan dari materi.	Web & Android
Penilaian kuis	Memeriksa jawaban dan menampilkan hasil sesuai respons backend.	Web & Android
Riwayat belajar	Melihat aktivitas belajar sebelumnya jika data riwayat sudah tersedia.	Web & Android
Tema tampilan	Pilihan tema terang dan gelap.	Web & Android


Fitur dapat berubah mengikuti hasil implementasi, evaluasi teknis, dan prioritas MVP.
🧰 Teknologi
Teknologi yang direncanakan/digunakan dalam proyek:
Bagian	Teknologi
Backend API	Python, FastAPI
Web	React
Android	Flutter, Dart
Database	PostgreSQL
AI	Provider/model AI yang dikonfigurasi melalui environment
Version control	Git & GitHub


Versi bahasa, framework, dan dependensi mengikuti file konfigurasi terbaru di masing-masing direktori proyek.
🏗️ Gambaran Arsitektur
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
    │   PostgreSQL    │    │    AI Provider  │
    │ User & Learning │    │   AI Processing │
    │ Data            │    │                 │
    └─────────────────┘    └─────────────────┘
Diagram ini menunjukkan rancangan konseptual. Detail layanan, penyimpanan file, dan alur AI mengikuti implementasi aktual.
📁 Struktur Repository
Struktur berikut adalah contoh susunan yang disarankan. Sesuaikan dengan direktori yang benar-benar ada di repository.
AIStudy/
├── backend/             # FastAPI backend
│   ├── app/
│   ├── tests/
│   └── requirements.txt
├── web/                 # React web application
│   ├── src/
│   └── package.json
├── android/             # Flutter application (jika ditempatkan di root)
│   ├── lib/
│   ├── test/
│   └── pubspec.yaml
├── database/            # Skema, migration, atau dokumentasi database
├── docs/                # Dokumentasi API, desain, dan panduan
├── .gitignore
└── README.md
Jika folder Android berada pada nama atau lokasi berbeda, gunakan struktur aktual repository sebagai acuan.

🚀 Menjalankan Proyek
Prasyarat
Pasang tools yang dibutuhkan sesuai komponen yang ingin dijalankan:
- Git
- Python versi yang sesuai dengan konfigurasi backend
- Node.js dan npm yang sesuai dengan aplikasi web
- Flutter SDK dan Android SDK untuk aplikasi Android
- PostgreSQL
- API key AI provider jika fitur AI memerlukannya
1. Clone repository
git clone https://github.com/NoxSans24/AIStudy.git
cd AIStudy
2. Backend (FastAPI)
Masuk ke direktori backend sesuai struktur repository. Contoh jika direktori bernama backend:
cd backend
python -m venv .venv
Aktifkan virtual environment:
Windows PowerShell
.\.venv\Scripts\Activate.ps1
macOS/Linux
source .venv/bin/activate
Pasang dependency menggunakan file dependency yang benar-benar tersedia di repository, misalnya:
pip install -r requirements.txt
Siapkan konfigurasi lokal dengan mengacu pada .env.example jika tersedia. Isi nilai lokal yang diperlukan, misalnya konfigurasi database, secret autentikasi, dan AI provider. Jangan commit file .env atau secret ke Git.
Jalankan server sesuai entry point yang diterapkan. Contoh umum jika aplikasi menyediakan objek app pada app.main:
uvicorn app.main:app --reload
Jika entry point proyek berbeda, ikuti instruksi dalam direktori backend.
3. Web (React)
Buka terminal baru dan masuk ke direktori web sesuai struktur repository:
cd web
npm install
Buat file environment lokal sesuai kebutuhan aplikasi. Gunakan nama variabel yang didefinisikan oleh proyek; jangan mengasumsikan nama variabel API tanpa memeriksa kode.
Jalankan aplikasi menggunakan script yang tersedia di package.json, misalnya:
npm run dev
Jika proyek menggunakan script lain, periksa bagian scripts di package.json.
4. Android (Flutter)
Buka terminal baru dan masuk ke direktori aplikasi Flutter yang sebenarnya:
cd android
flutter pub get
flutter doctor
flutter run
Pastikan emulator atau perangkat Android tersedia. Atur base URL backend berdasarkan konfigurasi aplikasi. Perlu diperhatikan bahwa localhost pada emulator Android biasanya menunjuk ke emulator itu sendiri, bukan komputer host; gunakan alamat host yang sesuai dengan lingkungan pengujian.
5. Database (PostgreSQL)
- Jalankan layanan PostgreSQL.
- Buat database development sesuai konfigurasi proyek.
- Atur koneksi melalui environment variable.
- Jalankan migration menggunakan tool yang benar-benar digunakan oleh repository.
- Gunakan data uji, bukan data pribadi atau produksi.
Perintah migration tidak dicantumkan secara spesifik karena harus disesuaikan dengan tool migration yang diterapkan pada proyek.
🔐 Konfigurasi dan Keamanan
- Jangan commit .env, password, token, API key, private key, atau keystore.
- Sediakan .env.example yang hanya berisi nama variabel dan contoh nilai non-rahasia.
- Simpan password dengan mekanisme hashing yang sesuai; jangan menyimpan password asli.
- Pastikan backend memverifikasi kepemilikan data pada setiap endpoint yang relevan.
- Jangan mengandalkan pembatasan tampilan UI untuk mengamankan data pengguna.
- Validasi tipe, ukuran, dan isi file yang diunggah.
- Gunakan HTTPS untuk deployment dan batasi CORS pada origin yang diperlukan.
- Jangan mencantumkan secret dalam log, screenshot, issue, atau dokumentasi publik.
🌿 Workflow Git dan Kontribusi
Kami menggunakan branch terpisah dan Pull Request agar perubahan anggota tim dapat ditinjau sebelum digabungkan.
Alur kerja
1. Pilih issue yang ditugaskan di GitHub Project.
2. Pastikan issue dan dependensinya sudah dipahami.
3. Tarik perubahan terbaru dari main.
4. Buat branch untuk pekerjaan.
5. Implementasikan perubahan dan jalankan pemeriksaan yang relevan.
6. Commit dan push branch.
7. Buat Pull Request dan tautkan issue.
8. Minta review anggota tim.
9. Merge setelah review dan pemeriksaan yang diperlukan lolos.
10. Perbarui status issue sesuai progres sebenarnya.
Contoh perintah:
git switch main
git pull origin main
git switch -c feature/nama-fitur

# Kerjakan perubahan, lalu:
git add .
git commit -m "feat: deskripsi perubahan"
git push -u origin feature/nama-fitur
Buat Pull Request dari branch fitur menuju main. Hindari mengerjakan langsung di main, melakukan force push tanpa koordinasi, atau memasukkan perubahan milik anggota lain tanpa review.
Konvensi commit
Gunakan pesan singkat dan jelas, misalnya:
feat: add document upload endpoint
fix: handle expired access token
test: add document access tests
docs: update local setup guide
refactor: organize API service layer
👥 Tim Pengembang
AI StudyMate dikembangkan oleh empat anggota dengan pembagian tanggung jawab berikut. Ganti placeholder dengan nama dan profil GitHub anggota tim.
Peran	Tanggung jawab
Member 1 — Backend & AI	FastAPI, autentikasi backend, API, pemrosesan dokumen, dan integrasi AI
Member 2 — Web Developer	React, antarmuka web, routing, dan integrasi API
Member 3 — Android Developer	Flutter, antarmuka Android, navigasi, dan integrasi API
Member 4 — Database, QA & Integrasi	Skema/migration database bersama backend, pengujian, integrasi, dan dokumentasi


Seluruh anggota bertanggung jawab menjaga kualitas kode, memperbarui issue, melakukan review, dan membantu integrasi lintas komponen.
🧪 Testing
Jenis pengujian yang perlu disiapkan dan dijalankan sesuai komponen:
- Backend: unit test, integration test API, validasi input, autentikasi, dan isolasi data pengguna.
- Web: pemeriksaan build, alur login, integrasi API, loading/error state, dan responsivitas.
- Android: analisis Flutter, widget test jika tersedia, alur navigasi, integrasi API, dan uji perangkat.
- AI: pemeriksaan kesesuaian jawaban dengan dokumen sumber, relevansi referensi, kualitas rangkuman, dan ketepatan kunci jawaban kuis.
Catat hasil pengujian yang benar-benar dijalankan. Jangan menyatakan suatu fitur lulus pengujian sebelum ada bukti hasilnya.
🗺️ Roadmap
Roadmap berikut adalah target pengembangan, bukan pernyataan bahwa seluruh fitur telah selesai.
- [ ] Week 1 — Fondasi: repository, kontrak API, database, dan kerangka backend/web/Android.
- [ ] Week 2 — Core features: autentikasi, upload dokumen, ekstraksi materi, dan fitur AI awal.
- [ ] Week 3 — Integrasi: chat, rangkuman, kuis, integrasi web/Android, dan perbaikan awal.
- [ ] Week 4 — Release: QA, keamanan, deployment, build APK, dokumentasi, dan demo.
Prioritaskan alur MVP yang benar-benar berfungsi jika waktu tidak cukup untuk menyelesaikan semua fitur tambahan.
📌 Status dan Dokumentasi
- Repository: https://github.com/NoxSans24/AIStudy
- Issue tracker: https://github.com/NoxSans24/AIStudy/issues
- Project board: akses melalui GitHub Projects yang digunakan oleh tim
- Dokumentasi API: tambahkan tautan atau lokasi file setelah tersedia
- Web demo / APK: tambahkan tautan setelah deployment dan build benar-benar tersedia
📄 Lisensi
Lisensi belum ditentukan. Tambahkan file LICENSE dan perbarui bagian ini setelah tim menyepakati lisensi proyek.
<div align="center">

AI StudyMate · Built collaboratively by an Informatics student team
</div>