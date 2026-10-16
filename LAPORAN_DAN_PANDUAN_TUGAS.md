# LAPORAN PEMODELAN SISTEM INFORMASI
## ARSITEKTUR SISTEM INFORMASI

---

### FORMAT ISIAN PENGUMPULAN TUGAS (SALIN KE KOLOM JAWABAN LMS)

```text
PEMODELAN SISTEM INFORMASI (DIAGRAM KONTEKS, DFD, DAN ERD)

Nama Lengkap         : Moh. Radithyo Surya Martuah
NIM                  : 531424113
Kelas                : Arsitektur Sistem Informasi E
Nomor Urut Presensi  : 18
Judul Studi Kasus    : Sistem Katalog Online Terpusat untuk Produk UMKM Lokal

```

---

## 1. PANDUAN MENGGUNAKAN FILE DRAW.IO DAN MEMBUAT TAUTAN BERBAGI (LINK SHARE)

File proyek Draw.io multi-halaman telah dibuat dan siap digunakan:
- **Nama Berkas**: `Sistem_Katalog_UMKM_Gorontalo.drawio`
- **Lokasi Berkas**: `d:\kuliah\Arsitektur Sistem Informasi\tugas-5\Sistem_Katalog_UMKM_Gorontalo.drawio`
- **Halaman yang Tersedia**:
  1. Tab 1: `1. Diagram Konteks`
  2. Tab 2: `2. DFD Level 0`
  3. Tab 3: `3. DFD Level 1 (Proses 3.0)`
  4. Tab 4: `4. ERD (Katalog UMKM)`

### Langkah Membuka dan Memeriksa Diagram di Draw.io:
1. Buka browser dan kunjungi **[https://app.diagrams.net/](https://app.diagrams.net/)** (atau [https://www.drawio.com/](https://www.drawio.com/)).
2. Pilih **"Open Existing Diagram"** (Buka Diagram yang Ada).
3. Unggah file `Sistem_Katalog_UMKM_Gorontalo.drawio` dari folder tugas ini.
4. Di bagian bawah jendela Draw.io, Anda akan melihat **4 Tab Halaman**. Klik masing-masing tab untuk melihat diagram secara utuh dan interaktif.

### Langkah Menghasilkan Tautan Berbagi Publik (Sesuai Ketentuan Dosen):
Agar dosen/penilai dapat langsung membuka tanpa meminta izin (permission request), pilih salah satu metode berikut:

#### Opsi A: Menggunakan Google Drive (Paling Umum & Direkomendasikan)
1. Di Draw.io, klik menu **File** &rarr; **Save as...** &rarr; Pilih **Google Drive**.
2. Beri nama file: `Tugas5_StudiKasus18_[Nama]_[NIM].drawio`.
3. Buka Google Drive Anda, klik kanan file tersebut &rarr; Pilih **Bagikan (Share)**.
4. Pada bagian **Akses Umum (General Access)**, ubah dari *Dibatasi (Restricted)* menjadi:
   - **"Siapa saja yang memiliki tautan" (Anyone with the link)**
   - Peran: **Pelihat (Viewer)**
5. Klik **Salin Tautan (Copy Link)**, lalu tempelkan link tersebut pada format pengumpulan di atas.

#### Opsi B: Menggunakan Fitur "Publish Link" Langsung dari Draw.io
1. Pada menu Draw.io, klik **File** &rarr; **Publish** &rarr; **Link...**
2. Centang opsi yang diinginkan (default sudah optimal).
3. Klik tombol **Create / Buat**.
4. Salin tautan `https://viewer.diagrams.net/?...` yang dihasilkan. Tautan ini langsung membuka viewer Draw.io tanpa perlu login Google Drive.

---

## 2. DESKRIPSI & ANALISIS KEBUTUHAN SISTEM (STUDI KASUS 18)

### 2.1 Latar Belakang & Ruang Lingkup
Dinas Koperasi dan UKM Gorontalo berinisiatif membangun **Sistem Katalog Online Terpusat untuk Produk UMKM Lokal**. Sistem ini berfungsi sebagai **etalase promosi digital** terpusat bagi produk-produk unggulan daerah Gorontalo (seperti kain kerajinan sulaman Karawo, olahan kelapa, kopi Pinogu, kuliner khas, dan perikanan).

### 2.2 Batasan Arsitektur Penting (Critical Boundary)
Sesuai arahan spesifikasi studi kasus:
1. **Bukan Marketplace Transaksional**: Sistem **TIDAK** menangani transaksi penjualan secara langsung (tidak ada modul keranjang belanja/checkout, pembayaran gateway, rekening bersama, maupun tarif ongkos kirim ekspedisi).
2. **Koneksi Mandiri Pelanggan-UMKM**: Sistem menyajikan direktori kontak resmi (nomor WhatsApp, telepon, email, alamat fisik gerai) sehingga pembeli atau masyarakat yang tertarik dapat langsung menghubungi UMKM secara mandiri.
3. **Otoritas Kurasi Terpusat oleh Dinas**: Admin sistem (petugas dari Dinas Koperasi & UKM Gorontalo) memegang kendali penuh dalam mendaftarkan UMKM, mengunggah produk, mengelola kategori, dan memverifikasi akurasi informasi produk agar kredibel dan terpercaya bagi publik.

---

## 3. KOMPONEN 1: DIAGRAM KONTEKS (CONTEXT DIAGRAM / DFD LEVEL 0)

Diagram Konteks memposisikan sistem secara global sebagai satu proses utama dengan memetakan seluruh entitas luar yang berinteraksi secara langsung.

### 3.1 Identifikasi Entitas Eksternal
1. **Admin Sistem (Dinas Koperasi & UKM Gorontalo)**:
   - Pengguna internal dari dinas yang memiliki hak otorisasi penuh untuk mengelola data UMKM, kategori, kurasi informasi dan foto produk, serta memantau statistik katalog.
2. **Masyarakat / Publik (Pengunjung Katalog)**:
   - Calon pembeli, wisatawan, investor, maupun masyarakat umum yang menjelajahi produk lokal berdasarkan kategori, mencari kata kunci, melihat detail produk, serta mencari kontak UMKM.

### 3.2 Matriks Aliran Data Diagram Konteks

| Entitas Eksternal | Aliran Data Masuk (Input ke Sistem) | Aliran Data Keluar (Output ke Entitas) |
| :--- | :--- | :--- |
| **Admin Sistem (Dinas)** | 1. Data Kredensial Login Admin<br>2. Data Profil & Legalitas UMKM Baru/Pembaruan<br>3. Data Master Kategori Produk<br>4. Data Spesifikasi Produk & Berkas Foto<br>5. Instruksi Status Kurasi (Tayang/Arsip) | 1. Status Autentikasi & Hak Akses Sesi<br>2. Notifikasi Konfirmasi Penyimpanan & Pembaruan<br>3. Status Validasi & Kurasi Produk<br>4. Laporan Statistik Katalog & Kunjungan Produk |
| **Masyarakat / Publik** | 1. Kata Kunci Pencarian Produk<br>2. Pilihan Filter Kategori Produk<br>3. Permintaan Detail Spesifikasi Produk<br>4. Permintaan Kontak Resmi Penjual UMKM | 1. Tampilan Etalase Katalog Produk Unggulan<br>2. Daftar Hasil Pencarian & Penyaringan Produk<br>3. Informasi Detail Produk & Kisaran Harga<br>4. Informasi Kontak Resmi (WhatsApp/Telp) & Lokasi UMKM |

---

## 4. KOMPONEN 2: DATA FLOW DIAGRAM (DFD LEVEL 0)

Pada DFD Level 0, proses sistem utama `0.0` didekomposisi menjadi **6 proses utama**, didukung oleh **5 Data Store (Penyimpanan Data)**.

### 4.1 Daftar Data Store (Penyimpanan Data)
- **`D1 | Data Pengguna Admin`**: Menyimpan kredensial login, NIP, nama petugas dinas, dan hak akses.
- **`D2 | Data UMKM Lokal`**: Menyimpan data identitas UMKM (Nama usaha, nama pemilik, NIB, kontak WhatsApp, email, media sosial, dan alamat wilayah Gorontalo).
- **`D3 | Data Kategori Produk`**: Menyimpan klasifikasi produk (Karawo, Kuliner Tradisional, Olahan Pertanian/Perikanan, dll.).
- **`D4 | Data Produk UMKM`**: Menyimpan informasi produk (nama, deskripsi, kisaran harga, foto utama, status tayang/kurasi, relasi ke UMKM dan Kategori).
- **`D5 | Data Log Kunjungan & Pencarian`**: Menyimpan jejak pencarian kata kunci dan produk yang paling sering dilihat untuk statistik dinas.

### 4.2 Dekomposisi 6 Proses Utama DFD Level 0

1. **Proses 1.0: Autentikasi & Kelola Akun Admin**
   - *Input*: Kredensial login (Username & Password) dari Admin Dinas.
   - *Akses Data Store*: Membaca dan memvalidasi ke `D1 (Data Pengguna Admin)`.
   - *Output*: Status otentikasi login, sesi aktif, dan hak akses dashboard admin.

2. **Proses 2.0: Pengelolaan Data UMKM Lokal**
   - *Input*: Formulir pendaftaran/pembaruan UMKM (Profil usaha, NIB/izin, kontak WA, alamat kecamatan/kabupaten).
   - *Akses Data Store*: Menulis, memperbarui, dan membaca ke `D2 (Data UMKM Lokal)`.
   - *Output*: Konfirmasi penyimpanan data UMKM dan daftar UMKM terverifikasi.

3. **Proses 3.0: Pengelolaan Kategori & Produk UMKM**
   - *Input*: Data kategori baru, spesifikasi produk, foto produk, kisaran harga, dan pilihan UMKM penanggung jawab.
   - *Akses Data Store*:
     - Membaca validitas UMKM dari `D2`.
     - Menulis/membaca kategori ke `D3`.
     - Menulis/memperbarui data produk ke `D4`.
   - *Output*: Konfirmasi berhasil kurasi dan notifikasi produk aktif siap tayang.

4. **Proses 4.0: Pencarian & Filter Katalog Produk**
   - *Input*: Kata kunci pencarian dan pilihan kategori dari Masyarakat/Publik.
   - *Akses Data Store*:
     - Mengambil daftar kategori dari `D3`.
     - Mengambil produk yang berstatus aktif dari `D4`.
     - Mencatat tren kata kunci ke `D5`.
   - *Output*: Daftar katalog produk hasil pencarian beserta foto thumbnail dan kisaran harga.

5. **Proses 5.0: Penayangan Detail Produk & Kontak UMKM**
   - *Input*: Aksi klik produk tertentu oleh Masyarakat/Publik.
   - *Akses Data Store*:
     - Mengambil spesifikasi lengkap dan galeri foto dari `D4`.
     - Mengambil kontak resmi (nomor WhatsApp, telepon, alamat fisik, peta) dari `D2`.
     - Mencatat kenaikan jumlah dilihat (view count) ke `D5`.
   - *Output*: Halaman detail produk lengkap beserta tautan langsung untuk menghubungi UMKM via WhatsApp atau telepon.

6. **Proses 6.0: Pembuatan Laporan & Statistik Katalog**
   - *Input*: Permintaan rekapitulasi laporan oleh Admin Dinas.
   - *Akses Data Store*: Membaca rekap UMKM (`D2`), rekap produk per kategori (`D4`), dan data log pencarian/kunjungan (`D5`).
   - *Output*: Laporan statistik katalog, sebaran UMKM, dan tren produk paling diminati kepada Admin Dinas.

---

## 5. KOMPONEN 3: DFD LEVEL 1 (BREAKDOWN PROSES 3.0: PENGELOLAAN KATEGORI & PRODUK)

Proses **3.0 Pengelolaan Kategori & Produk UMKM** didekomposisi lebih mendalam ke level 1 menjadi 4 sub-proses berurutan secara konsisten:

```
[Admin Dinas]
      │
      ├─► 3.1 Pengelolaan Data Kategori Produk ─────────► [D3: Data Kategori]
      │
      ├─► 3.2 Input & Validasi Spesifikasi Produk ◄─────► [D2: Data UMKM]
      │              │                             ◄─────► [D3: Data Kategori]
      │              ▼ (Draft Produk Tervalidasi)
      ├─► 3.3 Unggah & Kurasi Foto/Media Produk
      │              │
      │              ▼ (Paket Produk Lengkap + URL Media)
      └─► 3.4 Publikasi & Pembaruan Status Etalase ─────► [D4: Data Produk]
                     │
                     ▼ (Konfirmasi Publikasi)
               [Admin Dinas]
```

### Penjelasan Sub-Proses:
- **Sub-Proses 3.1: Pengelolaan Data Kategori Produk**
  - Menerima input nama kategori baru, slug URL, dan deskripsi kategori dari Admin Dinas.
  - Memperbarui tabel data kategori pada `D3 (Data Kategori Produk)`.
- **Sub-Proses 3.2: Input & Validasi Spesifikasi Produk**
  - Menerima formulir detail produk (nama produk, deskripsi produk, kisaran harga min-max, satuan).
  - Melakukan cross-check apakah ID UMKM yang dipilih sah pada `D2 (Data UMKM Lokal)` dan ID Kategori sah pada `D3 (Data Kategori Produk)`.
  - Meneruskan draft produk terverifikasi ke sub-proses berikutnya.
- **Sub-Proses 3.3: Unggah & Kurasi Foto/Media Produk**
  - Memproses unggahan foto produk dari Admin Dinas.
  - Melakukan validasi format berkas (JPG/PNG), kompresi ukuran, penamaan unik, dan kurasi kelayakan visual produk.
  - Menghasilkan URL foto dan menghubungkannya dengan draft produk.
- **Sub-Proses 3.4: Publikasi & Pembaruan Status Etalase**
  - Mengatur status tayang: `Tayang (Aktif)`, `Draft`, atau `Arsip (Nonaktif)`.
  - Menyimpan record akhir ke `D4 (Data Produk UMKM)` sehingga langsung muncul di etalase katalog online publik.
  - Mengirimkan konfirmasi publikasi berhasil ke layar Admin Dinas.

---

## 6. KOMPONEN 4: ENTITY-RELATIONSHIP DIAGRAM (ERD)

ERD dirancang untuk mendukung seluruh kebutuhan etalase digital UMKM tanpa modul transaksi langsung, dengan integritas referensial yang kuat (Primary Key dan Foreign Key).

### 6.1 Kamus Data Entitas dan Atribut

#### 1. Entitas `ADMIN_DINAS` (Pengelola Sistem)
- `id_admin` : **INT [PK]** *(Identifier unik petugas admin dinas)*
- `username` : **VARCHAR(50)** *(Akun login)*
- `password_hash` : **VARCHAR(255)** *(Kata sandi terenkripsi)*
- `nama_petugas` : **VARCHAR(100)** *(Nama lengkap petugas)*
- `nip` : **VARCHAR(30)** *(Nomor Induk Pegawai)*
- `email` : **VARCHAR(100)** *(Email dinas)*
- `no_telepon` : **VARCHAR(20)** *(Nomor kontak)*
- `role` : **VARCHAR(20)** *(Peran hak akses)*
- `created_at` : **TIMESTAMP** *(Waktu pembuatan akun)*

#### 2. Entitas `UMKM` (Pelaku Usaha Lokal Gorontalo)
- `id_umkm` : **INT [PK]** *(Identifier unik pelaku usaha UMKM)*
- `id_admin` : **INT [FK]** *(Admin penanggung jawab verifikasi)*
- `nama_umkm` : **VARCHAR(150)** *(Nama merk/usaha UMKM)*
- `nama_pemilik` : **VARCHAR(100)** *(Nama pemilik usaha)*
- `nib_izin_usaha` : **VARCHAR(50)** *(Nomor Induk Berusaha / Izin P-IRT/Halal)*
- `alamat_lengkap` : **TEXT** *(Alamat fisik lokasi gerai/rumah produksi)*
- `kecamatan` : **VARCHAR(50)** *(Kecamatan di wilayah Gorontalo)*
- `kabupaten_kota` : **VARCHAR(50)** *(Kab/Kota di Gorontalo)*
- `no_whatsapp` : **VARCHAR(20)** *(Nomor WhatsApp resmi untuk dihubungi pembeli)*
- `email_umkm` : **VARCHAR(100)** *(Email resmi UMKM)*
- `tautan_sosmed` : **VARCHAR(255)** *(Link Instagram/Facebook/Website)*
- `status_verifikasi` : **ENUM('Terverifikasi','Pending','Nonaktif')**
- `tanggal_daftar` : **DATE** *(Tanggal terdaftar di dinas)*

#### 3. Entitas `KATEGORI` (Pengelompokan Produk)
- `id_kategori` : **INT [PK]** *(Identifier unik kategori produk)*
- `nama_kategori` : **VARCHAR(100)** *(Nama kategori: Sulaman Karawo, Olahan Jagung/Kelapa, dll.)*
- `slug_kategori` : **VARCHAR(100)** *(Pengenal URL ramah SEO)*
- `deskripsi` : **TEXT** *(Penjelasan rumpun produk)*
- `icon_kategori` : **VARCHAR(100)** *(Ikon visual)*

#### 4. Entitas `PRODUK` (Barang Etalase)
- `id_produk` : **INT [PK]** *(Identifier unik produk katalog)*
- `id_umkm` : **INT [FK]** *(Relasi ke UMKM pembuat produk)*
- `id_kategori` : **INT [FK]** *(Relasi ke Kategori produk)*
- `id_admin` : **INT [FK]** *(Relasi ke Admin yang mengurasi/mengunggah)*
- `nama_produk` : **VARCHAR(150)** *(Nama produk lokal)*
- `deskripsi_produk` : **TEXT** *(Uraian spesifikasi, bahan baku, keunikan)*
- `kisaran_harga_min` : **DECIMAL(12,2)** *(Harga terendah)*
- `kisaran_harga_max` : **DECIMAL(12,2)** *(Harga tertinggi atau harga pas)*
- `satuan_produk` : **VARCHAR(50)** *(Pcs, Paket, Lembar, Botol, Kg)*
- `foto_utama` : **VARCHAR(255)** *(URL foto cover produk)*
- `status_tayang` : **ENUM('Tayang','Arsip','Draft')**
- `total_dilihat` : **INT** *(Penghitung jumlah klik tayang)*
- `created_at` : **TIMESTAMP**
- `updated_at` : **TIMESTAMP**

#### 5. Entitas `FOTO_PRODUK` (Galeri Visual Produk)
- `id_foto` : **INT [PK]** *(Identifier foto)*
- `id_produk` : **INT [FK]** *(Relasi ke produk induk)*
- `url_file_foto` : **VARCHAR(255)** *(Lokasi penyimpanan file gambar)*
- `judul_foto` : **VARCHAR(100)** *(Keterangan sudut pengambilan foto)*
- `urutan_tampil` : **INT** *(Urutan penayangan di slider galeri)*
- `is_thumbnail` : **BOOLEAN** *(Penanda foto sampul)*

#### 6. Entitas `LOG_PENCARIAN` (Analisis Kata Kunci Pengunjung)
- `id_log` : **BIGINT [PK]** *(Identifier log pencarian)*
- `kata_kunci` : **VARCHAR(150)** *(Kata kunci yang dicari publik)*
- `waktu_akses` : **TIMESTAMP** *(Waktu pencarian)*
- `ip_pengunjung` : **VARCHAR(45)** *(Alamat IP untuk analitik)*
- `id_kategori` : **INT [FK, Nullable]** *(Filter kategori yang digunakan)*
- `id_produk` : **INT [FK, Nullable]** *(Produk yang diklik)*

---

### 6.2 Kardinalitas dan Relasi Antar-Entitas

| Hubungan Relasi | Kardinalitas | Penjelasan Makna Bisnis |
| :--- | :---: | :--- |
| **`ADMIN_DINAS` &rarr; `UMKM`** | **1 : N** *(One-to-Many)* | Satu petugas Admin Dinas dapat mendaftarkan dan memverifikasi banyak UMKM; Setiap UMKM diverifikasi oleh seorang Admin Dinas penanggung jawab. |
| **`ADMIN_DINAS` &rarr; `PRODUK`** | **1 : N** *(One-to-Many)* | Satu petugas Admin Dinas dapat mengurasi dan mengunggah banyak Produk ke etalase; Setiap Produk dikurasi oleh petugas Admin Dinas. |
| **`UMKM` &rarr; `PRODUK`** | **1 : N** *(One-to-Many)* | Satu UMKM memproduksi dan memiliki banyak Produk di etalase; Setiap Produk berasal dari satu entitas UMKM yang sah. |
| **`KATEGORI` &rarr; `PRODUK`** | **1 : N** *(One-to-Many)* | Satu Kategori (misal: "Kerajinan Sulam Karawo") menaungi banyak Produk UMKM; Setiap Produk dikelompokkan ke dalam satu Kategori utama. |
| **`PRODUK` &rarr; `FOTO_PRODUK`** | **1 : N** *(One-to-Many)* | Satu Produk dapat memiliki banyak Foto galeri untuk menunjukkan detail produk dari berbagai sisi; Setiap Foto galeri terikat pada satu Produk. |
| **`PRODUK` &rarr; `LOG_PENCARIAN`** | **1 : N** *(One-to-Many)* | Satu Produk dapat tercatat berkali-kali pada riwayat pencarian/penayangan oleh pengunjung publik. |

---

## 7. KESIMPULAN ARSITEKTUR SISTEM

Pemodelan sistem ini secara menyeluruh telah memenuhi seluruh kriteria Tugas 5:
1. **Diagram Konteks** mengabstraksikan sistem etalase digital terpusat dengan memisahkan wewenang antara Admin Dinas (pengendali data) dan Masyarakat (penikmat etalase).
2. **DFD Level 0** menggambarkan 6 proses inti, pemisahan 5 data store terstruktur, dan penegasan bahwa tidak ada aliran kas/pembayaran di dalam sistem.
3. **DFD Level 1** mendekomposisi Proses 3.0 secara konsisten dan sistematis mulai dari kategori, data teknis, kurasi foto, hingga publikasi ke etalase publik.
4. **ERD** dirancang terstandardisasi dengan identifikasi Primary Key (`+`), Foreign Key (`#`), tipe data, serta kardinalitas relasi `1:N` yang harmonis.
