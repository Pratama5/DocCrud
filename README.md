# DocCrud - CRUD Aplikasi Menggunakan Docker

DocCrud adalah aplikasi CRUD sederhana yang dibangun menggunakan Flask dan MySQL, yang memungkinkan pengguna untuk menambah, melihat, mengedit, dan menghapus dokumen melalui antarmuka web.

## Instalasi dan Menjalankan Aplikasi dengan Docker

### 1. Persiapkan Docker
Pastikan Docker sudah terinstal di sistem Anda. Jika belum, unduh dan instal Docker dari [sini](https://www.docker.com/get-started).

### 2. Clone Repository
Clone repository ini ke mesin lokal Anda:
```bash
   git clone https://github.com/username/repository-name.git
```

### 3. Masuk ke Direktori Proyek
Navigasi ke direktori proyek:
```bash
   cd repository-name
```

### 4. Build dan Jalankan Docker Container
Untuk membangun dan menjalankan aplikasi menggunakan Docker Compose, gunakan perintah berikut 
```bash
   docker-compose up --build
```
Perintah ini akan:

- Membangun gambar Docker untuk aplikasi web (Flask) dan MySQL.
- Menjalankan aplikasi di dalam container, dengan Flask yang dapat diakses pada http://localhost:5000 dan MySQL di localhost:3306 .

### 5. Mengakses Aplikasi
Setelah proses build dan startup selesai, Anda dapat mengakses aplikasi melalui browser di http://localhost:5000.

Untuk menghentikan container, gunakan perintah berikut:
```bash
   docker-compose down
```


## Penjelasan Singkat Tentang Aplikasi dan Fungsi Utama dari Masing-Masing Fitur CRUD
DocCrud adalah aplikasi web untuk mengelola dokumen melalui empat operasi dasar dalam database, yaitu:

- Create: Menambahkan dokumen baru dengan memasukkan judul dan konten.
- Read: Menampilkan daftar semua dokumen yang sudah ditambahkan beserta judul dan kontennya.
- Update: Mengedit dokumen yang sudah ada, baik judul maupun kontennya.
- Delete: Menghapus dokumen yang sudah tidak diperlukan.

Aplikasi ini menyediakan antarmuka web sederhana yang memungkinkan pengguna untuk mengelola data dokumen secara efisien.

## Penjelasan Dockerfile dan Peran Setiap Instruksi di Dalamnya
Dockerfile adalah skrip yang berisi serangkaian instruksi untuk membangun gambar Docker untuk aplikasi web (Flask).
Dockerfile dapat dilihat pada direktori /doccrud sebagai Dockerfile
### Penjelasan Instruksi Dockerfile
1. FROM python:3.8-slim: Menentukan gambar dasar yang digunakan untuk aplikasi ini, yaitu Python 3.8 dengan varian slim.
2. WORKDIR /app: Menetapkan /app sebagai direktori kerja dalam container. Semua perintah selanjutnya akan dijalankan di dalam direktori ini.
3. COPY requirements.txt /app/: Menyalin file requirements.txt yang berisi daftar dependensi Python ke dalam container.
4. RUN pip install --no-cache-dir -r requirements.txt: Menginstall semua dependensi yang ada di requirements.txt.
5. COPY . /app/: Menyalin seluruh kode aplikasi ke dalam container.
6. EXPOSE 5000: Menyatakan bahwa container akan menggunakan port 5000 untuk aplikasi Flask.
7. CMD ["python", "app.py"]: Perintah untuk menjalankan aplikasi Flask saat container dijalankan.

## Penjelasan Docker-Compose dan file docker-compose.yml
Docker Compose digunakan untuk mengelola multi-container Docker applications, dalam hal ini untuk aplikasi DocCrud yang terdiri dari dua container: satu untuk aplikasi web (Flask) dan satu untuk database (MySQL). 
File docker-compose.yml dapat dilihat pada direktori /doccrud

### Penjelasan File docker-compose.yml
1. version: '3.8': Menentukan versi Docker Compose yang digunakan.

2. services: Bagian ini mendefinisikan dua layanan, web untuk aplikasi Flask dan db untuk MySQL.
   * web:
      - build: .: Menunjukkan Dockerfile di direktori yang sama digunakan untuk membangun image. 
      - ports: Mengekspos port 5000 pada host dan menghubungkannya ke port 5000 di dalam container.
      - environment: Mengatur variabel lingkungan seperti mode pengembangan dan koneksi database.
      - volumes: Menyambungkan direktori proyek dengan container untuk memudahkan pengembangan.
      - depends_on: Menjamin bahwa container web hanya dijalankan setelah container db aktif.
   * db:
      - image: mysql:5.7: Menggunakan image resmi MySQL versi 5.7.
      - environment: Mengatur password root dan nama database yang akan dibuat.
      - ports: Mengekspos port 3306 di host untuk akses ke MySQL.
      - volumes: Menggunakan volume db_data untuk menyimpan data MySQL agar tetap ada meskipun container dihentikan.

3. volumes: Bagian ini mendefinisikan volume db_data yang digunakan untuk menyimpan data MySQL secara persisten.

## Struktur Proyek
Berikut adalah struktur direktori dari aplikasi ini:
```bash
   /doccrud
      /app.py
      /Dockerfile         # Dockerfile untuk membangun image
      /docker-compose.yml # File konfigurasi Docker Compose
      /requirements.txt   # Daftar dependensi Python
      /templates/
          /index.html     # Halaman utama aplikasi
          /create.html    # Halaman untuk menambah dokumen baru
          /update.html    # Halaman untuk mengedit dokumen
```

