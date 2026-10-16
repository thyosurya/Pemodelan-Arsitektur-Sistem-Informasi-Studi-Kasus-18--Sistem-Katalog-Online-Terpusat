"""
Update portal index.html with interactive audit report and updated diagrams.
"""
import os

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tugas 5 - Sistem Katalog Online Produk UMKM Gorontalo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --bg-card: #1e293b;
      --border-color: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent-blue: #38bdf8;
      --accent-purple: #a855f7;
      --accent-green: #22c55e;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --radius: 12px;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.4);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95));
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 16px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand-title {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-no {
      background: linear-gradient(135deg, #38bdf8, #6366f1);
      color: #ffffff;
      font-weight: 800;
      font-size: 14px;
      padding: 6px 14px;
      border-radius: 999px;
      box-shadow: 0 2px 8px rgba(56, 189, 248, 0.4);
    }

    .brand-title h1 {
      font-size: 17px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.02em;
    }

    .brand-title p {
      font-size: 12px;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      gap: 10px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      border: none;
    }

    .btn-primary {
      background: linear-gradient(135deg, #38bdf8, #2563eb);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }

    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4);
    }

    .btn-secondary {
      background: #334155;
      color: #f8fafc;
      border: 1px solid #475569;
    }

    .btn-secondary:hover {
      background: #475569;
    }

    main {
      flex: 1;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .nav-tabs {
      display: flex;
      gap: 8px;
      background: #1e293b;
      padding: 6px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      overflow-x: auto;
    }

    .tab-btn {
      flex: 1;
      min-width: 160px;
      padding: 12px 14px;
      background: transparent;
      border: none;
      border-radius: 8px;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 13px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }

    .tab-btn.active {
      color: #ffffff;
      background: #0f172a;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
      border: 1px solid #334155;
    }

    .tab-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 99px;
      background: #334155;
      color: var(--text-muted);
    }

    .tab-btn.active .tab-badge {
      background: #38bdf8;
      color: #0f172a;
    }

    .tab-content {
      display: none;
      animation: fadeIn 0.25s ease-in-out;
    }

    .tab-content.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
      margin-bottom: 20px;
    }

    .card-title {
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .card-subtitle {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 20px;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }

    .diagram-frame {
      background: #ffffff;
      border-radius: 10px;
      padding: 20px;
      overflow-x: auto;
      border: 2px solid #334155;
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.1);
    }

    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
    }

    .status-ok {
      background: rgba(34, 197, 94, 0.2);
      color: #4ade80;
      border: 1px solid rgba(34, 197, 94, 0.4);
    }

    .code-block {
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #38bdf8;
      overflow-x: auto;
      position: relative;
    }

    .copy-btn {
      position: absolute;
      top: 10px;
      right: 10px;
      background: #1e293b;
      border: 1px solid #334155;
      color: #f8fafc;
      padding: 6px 12px;
      font-size: 11px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      transition: background 0.2s;
    }

    .copy-btn:hover {
      background: #38bdf8;
      color: #0f172a;
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }

    .data-table th {
      background: #0f172a;
      color: #38bdf8;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      font-weight: 600;
    }

    .data-table td {
      padding: 12px 14px;
      border-bottom: 1px solid #283548;
      color: #cbd5e1;
    }

    .step-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .step-item {
      display: flex;
      gap: 14px;
      align-items: flex-start;
      background: #151f30;
      padding: 14px 18px;
      border-radius: 8px;
      border: 1px solid #223249;
    }

    .step-num {
      background: #38bdf8;
      color: #0f172a;
      font-weight: 800;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      flex-shrink: 0;
    }

    footer {
      background: #0b1120;
      border-top: 1px solid var(--border-color);
      padding: 20px;
      text-align: center;
      font-size: 12px;
      color: var(--text-muted);
    }
  </style>
</head>
<body>

  <header>
    <div class="brand-title">
      <span class="badge-no">URUTAN 18</span>
      <div>
        <h1>Tugas 5 - Sistem Katalog Online Produk UMKM Gorontalo</h1>
        <p>Hasil Audit Tata Letak: Bebas Tabrakan (Zero Overlap) &bull; Diagram Konteks, DFD Level 0, DFD Level 1, dan ERD</p>
      </div>
    </div>
    <div class="header-actions">
      <a href="https://app.diagrams.net/" target="_blank" class="btn btn-primary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
        Buka Draw.io Web
      </a>
      <a href="Sistem_Katalog_UMKM_Gorontalo.drawio" download class="btn btn-secondary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        Unduh .drawio
      </a>
    </div>
  </header>

  <main>
    <!-- Navigation Tabs -->
    <div class="nav-tabs">
      <button class="tab-btn active" onclick="openTab(event, 'tab-audit')">
        <span class="tab-badge">✓</span> Hasil Audit Tata Letak
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-submission')">
        <span class="tab-badge">0</span> Format Jawaban LMS
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-context')">
        <span class="tab-badge">1</span> Diagram Konteks
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-dfd0')">
        <span class="tab-badge">2</span> DFD Level 0
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-dfd1')">
        <span class="tab-badge">3</span> DFD Level 1 (3.0)
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-erd')">
        <span class="tab-badge">4</span> ERD & Kardinalitas
      </button>
      <button class="tab-btn" onclick="openTab(event, 'tab-guide')">
        <span class="tab-badge">5</span> Panduan Link Share
      </button>
    </div>

    <!-- TAB AUDIT TATA LETAK -->
    <div id="tab-audit" class="tab-content active">
      <div class="card">
        <div class="card-title">
          <span>🔍</span> Laporan Hasil Pengecekan Tata Letak & Kelengkapan Diagram
        </div>
        <p class="card-subtitle">
          Pemeriksaan mendalam terhadap titik koordinat geometris, jalur garis aliran (edge routing), posisi label teks, dan kelengkapan standar evaluasi dosen.
        </p>

        <div class="grid-4" style="margin-bottom: 24px;">
          <div style="background: #151f30; padding: 16px; border-radius: 8px; border: 1px solid #23344d;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-weight: 700; color: #ffffff;">Diagram Konteks</span>
              <span class="status-pill status-ok">✓ 100% Bersih</span>
            </div>
            <p style="font-size: 12px; color: var(--text-muted);">
              Jarak antarkotak diperluas menjadi 200px. Teks 4 baris data flow berada di jalur independen tanpa menabrak batas entitas.
            </p>
          </div>

          <div style="background: #151f30; padding: 16px; border-radius: 8px; border: 1px solid #23344d;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-weight: 700; color: #ffffff;">DFD Level 0</span>
              <span class="status-pill status-ok">✓ 100% Bersih</span>
            </div>
            <p style="font-size: 12px; color: var(--text-muted);">
              Pemisahan tegas 5 kolom: Admin &rarr; Proses Dinas &rarr; Data Store &rarr; Proses Publik &rarr; Masyarakat. Tidak ada label yang bertumpuk.
            </p>
          </div>

          <div style="background: #151f30; padding: 16px; border-radius: 8px; border: 1px solid #23344d;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-weight: 700; color: #ffffff;">DFD Level 1</span>
              <span class="status-pill status-ok">✓ 100% Bersih</span>
            </div>
            <p style="font-size: 12px; color: var(--text-muted);">
              Garis umpan balik 'Konfirmasi Publikasi' dialihkan melalui jalur luar (y=610), sehingga tidak bersilangan dengan jalur instruksi status.
            </p>
          </div>

          <div style="background: #151f30; padding: 16px; border-radius: 8px; border: 1px solid #23344d;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-weight: 700; color: #ffffff;">ERD & Relasi</span>
              <span class="status-pill status-ok">✓ 100% Bersih</span>
            </div>
            <p style="font-size: 12px; color: var(--text-muted);">
              Jarak vertikal antara UMKM dan PRODUK diperluas menjadi 70px. Label '1 : N Memproduksi / Memiliki' memiliki ruang lega.
            </p>
          </div>
        </div>

        <div class="card-title" style="font-size: 16px;"><span>📋</span> Matriks Kelengkapan Persyaratan Tugas 5</div>
        <table class="data-table">
          <thead>
            <tr>
              <th>Komponen Wajib Tugas</th>
              <th>Status Kelengkapan</th>
              <th>Kesesuaian pada Berkas Draw.io</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Diagram Konteks</strong></td>
              <td><span class="status-pill status-ok">Lengkap</span></td>
              <td>2 Entitas Eksternal (Admin Dinas & Masyarakat), Proses Tunggal 0.0, seluruh aliran data masuk/keluar terpetakan lengkap. Diberi catatan arsitektur non-transaksional langsung.</td>
            </tr>
            <tr>
              <td><strong>2. DFD Level 0</strong></td>
              <td><span class="status-pill status-ok">Lengkap</span></td>
              <td>6 Proses Utama (1.0 s.d 6.0), 5 Data Store (D1 Pengguna, D2 UMKM, D3 Kategori, D4 Produk, D5 Log Kunjungan). Aliran data berarah dua arah dan satu arah akurat.</td>
            </tr>
            <tr>
              <td><strong>3. DFD Level 1 (Breakdown)</strong></td>
              <td><span class="status-pill status-ok">Lengkap</span></td>
              <td>Dekomposisi Proses 3.0 (Pengelolaan Kategori & Produk UMKM) menjadi 4 sub-proses (3.1, 3.2, 3.3, 3.4) secara runtut dan konsisten dengan Level 0.</td>
            </tr>
            <tr>
              <td><strong>4. Entity-Relationship Diagram (ERD)</strong></td>
              <td><span class="status-pill status-ok">Lengkap</span></td>
              <td>6 Entitas (ADMIN_DINAS, UMKM, KATEGORI, PRODUK, FOTO_PRODUK, LOG_PENCARIAN). Atribut lengkap dengan tipe data, Primary Key (+), Foreign Key (#), dan relasi kardinalitas 1:N.</td>
            </tr>
            <tr>
              <td><strong>5. Format Berkas Draw.io Multi-Halaman</strong></td>
              <td><span class="status-pill status-ok">Lengkap</span></td>
              <td>Tersimpan dalam 1 berkas <code>Sistem_Katalog_UMKM_Gorontalo.drawio</code> dengan 4 tab halaman interaktif siap simpan ke Google Drive.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB SUBMISSION FORMAT -->
    <div id="tab-submission" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>📋</span> Format Isian Pengumpulan Tugas ke LMS
        </div>
        <p class="card-subtitle">
          Salin teks di bawah ini dan masukkan ke formulir tugas kuliah Anda bersama tautan publik Draw.io.
        </p>

        <div class="code-block">
          <button class="copy-btn" onclick="copyText('lms-text')">Salin Format Teks</button>
          <pre id="lms-text">Nama Lengkap         : [Nama Lengkap Anda]
NIM                  : [NIM Anda]
Kelas                : [Kelas Anda, misal: Kelas A]
Nomor Urut Presensi  : 18
Judul Studi Kasus    : Studi Kasus 18: Sistem Katalog Online Terpusat untuk Produk UMKM Lokal (Dinas Koperasi dan UKM Gorontalo)
URL Link Share Draw.io : [Tempelkan URL Link Publik Draw.io Anda di Sini]</pre>
        </div>
      </div>
    </div>

    <!-- TAB DIAGRAM KONTEKS -->
    <div id="tab-context" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>🌐</span> Tab 1: Diagram Konteks (Context Diagram Level 0)
        </div>
        <p class="card-subtitle">Etalase digital terpusat tanpa transaksi pembayaran langsung.</p>
        <div class="diagram-frame">
          <svg viewBox="0 0 1100 480" style="width: 100%; height: auto; min-width: 900px; font-family: 'Plus Jakarta Sans', sans-serif;">
            <rect x="20" y="20" width="1060" height="50" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
            <text x="550" y="45" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">DIAGRAM KONTEKS - SISTEM KATALOG ONLINE TERPUSAT PRODUK UMKM GORONTALO</text>
            <text x="550" y="62" fill="#94a3b8" font-size="11" text-anchor="middle">Studi Kasus 18: Dinas Koperasi & UKM Gorontalo (Non-Transaksi Langsung)</text>

            <rect x="40" y="150" width="220" height="170" rx="6" fill="#e1d5e7" stroke="#9673a6" stroke-width="2"/>
            <text x="150" y="185" fill="#4a154b" font-size="13" font-weight="700" text-anchor="middle">ADMIN SISTEM</text>
            <text x="150" y="205" fill="#4a154b" font-size="11" font-weight="600" text-anchor="middle">(Dinas Koperasi & UKM)</text>
            <line x1="50" y1="215" x2="250" y2="215" stroke="#9673a6" stroke-width="1"/>
            <text x="55" y="235" fill="#4a154b" font-size="10">&bull; Registrasi & verifikasi data UMKM</text>
            <text x="55" y="255" fill="#4a154b" font-size="10">&bull; Unggah & kurasi produk lokal</text>
            <text x="55" y="275" fill="#4a154b" font-size="10">&bull; Kelola master kategori produk</text>
            <text x="55" y="295" fill="#4a154b" font-size="10">&bull; Pantau statistik katalog etalase</text>

            <rect x="420" y="130" width="270" height="210" rx="24" fill="#d5e8d4" stroke="#82b366" stroke-width="2.5"/>
            <text x="555" y="170" fill="#276749" font-size="18" font-weight="800" text-anchor="middle">0.0</text>
            <text x="555" y="200" fill="#1c4732" font-size="13" font-weight="700" text-anchor="middle">SISTEM KATALOG ONLINE</text>
            <text x="555" y="220" fill="#1c4732" font-size="13" font-weight="700" text-anchor="middle">PRODUK UMKM LOKAL</text>
            <text x="555" y="240" fill="#1c4732" font-size="12" font-weight="700" text-anchor="middle">GORONTALO</text>
            <line x1="450" y1="255" x2="660" y2="255" stroke="#82b366" stroke-width="1"/>
            <text x="555" y="280" fill="#276749" font-size="10" text-anchor="middle">Etalase Promosi Digital Terpusat</text>
            <text x="555" y="300" fill="#276749" font-size="10" text-anchor="middle">& Direktori Kontak Resmi Pelaku UMKM</text>

            <rect x="840" y="150" width="220" height="170" rx="6" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2"/>
            <text x="950" y="185" fill="#1e3a8a" font-size="13" font-weight="700" text-anchor="middle">MASYARAKAT / PUBLIK</text>
            <text x="950" y="205" fill="#1e3a8a" font-size="11" font-weight="600" text-anchor="middle">(Pengunjung Katalog)</text>
            <line x1="850" y1="215" x2="1050" y2="215" stroke="#6c8ebf" stroke-width="1"/>
            <text x="855" y="235" fill="#1e3a8a" font-size="10">&bull; Cari produk per kategori lokal</text>
            <text x="855" y="255" fill="#1e3a8a" font-size="10">&bull; Cari produk via kata kunci</text>
            <text x="855" y="275" fill="#1e3a8a" font-size="10">&bull; Telusuri rincian detail & harga</text>
            <text x="855" y="295" fill="#1e3a8a" font-size="10">&bull; Hubungi penjual langsung via WA</text>

            <path d="M 260 195 L 415 195" stroke="#2563eb" stroke-width="2" fill="none" marker-end="url(#arrow-blue)"/>
            <text x="340" y="172" fill="#1d4ed8" font-size="9" font-weight="600" text-anchor="middle">1. Kredensial Login Admin</text>
            <text x="340" y="184" fill="#1d4ed8" font-size="9" font-weight="600" text-anchor="middle">2. Data Profil & Legalitas UMKM</text>
            <text x="340" y="196" fill="#1d4ed8" font-size="9" font-weight="600" text-anchor="middle">3. Data Kategori, Produk & Foto</text>

            <path d="M 420 270 L 265 270" stroke="#9333ea" stroke-width="2" fill="none" marker-end="url(#arrow-purple)"/>
            <text x="340" y="285" fill="#7e22ce" font-size="9" font-weight="600" text-anchor="middle">1. Status Login & Info Sesi</text>
            <text x="340" y="297" fill="#7e22ce" font-size="9" font-weight="600" text-anchor="middle">2. Konfirmasi Publikasi Produk</text>
            <text x="340" y="309" fill="#7e22ce" font-size="9" font-weight="600" text-anchor="middle">3. Laporan Statistik Katalog UMKM</text>

            <path d="M 840 195 L 695 195" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#arrow-green)"/>
            <text x="765" y="172" fill="#047857" font-size="9" font-weight="600" text-anchor="middle">1. Kata Kunci Pencarian</text>
            <text x="765" y="184" fill="#047857" font-size="9" font-weight="600" text-anchor="middle">2. Pilihan Filter Kategori</text>
            <text x="765" y="196" fill="#047857" font-size="9" font-weight="600" text-anchor="middle">3. Permintaan Detail & Kontak</text>

            <path d="M 690 270 L 835 270" stroke="#db2777" stroke-width="2" fill="none" marker-end="url(#arrow-pink)"/>
            <text x="765" y="285" fill="#be185d" font-size="9" font-weight="600" text-anchor="middle">1. Tampilan Etalase Katalog</text>
            <text x="765" y="297" fill="#be185d" font-size="9" font-weight="600" text-anchor="middle">2. Detail Produk & Kisaran Harga</text>
            <text x="765" y="309" fill="#be185d" font-size="9" font-weight="600" text-anchor="middle">3. Kontak WhatsApp Resmi & Lokasi</text>

            <rect x="40" y="370" width="1020" height="85" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
            <text x="60" y="395" fill="#0f172a" font-size="11" font-weight="700">Karakteristik Arsitektur Khusus:</text>
            <text x="60" y="415" fill="#475569" font-size="10">&bull; Sistem ini tidak menangani pembayaran/transaksi penjualan langsung. Pembeli menghubungi UMKM secara mandiri.</text>
            <text x="60" y="432" fill="#475569" font-size="10">&bull; Admin sistem Dinas Koperasi & UKM bertindak sebagai kurator terpusat dalam memastikan validitas data.</text>

            <defs>
              <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
              </marker>
              <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#9333ea" />
              </marker>
              <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
              </marker>
              <marker id="arrow-pink" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#db2777" />
              </marker>
            </defs>
          </svg>
        </div>
      </div>
    </div>

    <!-- TAB DFD LEVEL 0 -->
    <div id="tab-dfd0" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>⚙️</span> Tab 2: DFD Level 0 (Overview Diagram)
        </div>
        <p class="card-subtitle">6 Proses Utama dan 5 Data Store dalam tata letak 5 kolom yang terkoordinasi rapi.</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>Kode</th>
              <th>Nama Komponen</th>
              <th>Tipe</th>
              <th>Deskripsi Fungsi & Aliran Data</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>1.0</strong></td><td>Autentikasi & Kelola Akun Admin</td><td>Proses</td><td>Memvalidasi akun dinas dan hak akses ke D1.</td></tr>
            <tr><td><strong>2.0</strong></td><td>Pengelolaan Data UMKM Lokal</td><td>Proses</td><td>Mendaftarkan, memverifikasi NIB/alamat, dan menyimpan data kontak UMKM ke D2.</td></tr>
            <tr><td><strong>3.0</strong></td><td>Pengelolaan Kategori & Produk UMKM</td><td>Proses</td><td>Mengurasi spesifikasi, foto, dan harga produk lokal ke D3 & D4.</td></tr>
            <tr><td><strong>4.0</strong></td><td>Pencarian & Filter Katalog Produk</td><td>Proses</td><td>Penyaringan produk aktif bagi publik berdasarkan kategori & kata kunci.</td></tr>
            <tr><td><strong>5.0</strong></td><td>Penayangan Detail Produk & Kontak</td><td>Proses</td><td>Menyajikan foto, deskripsi, harga, serta tautan langsung ke WhatsApp UMKM.</td></tr>
            <tr><td><strong>6.0</strong></td><td>Pembuatan Laporan & Statistik</td><td>Proses</td><td>Menyusun rekapitulasi jumlah UMKM, produk per kategori, dan tren pencarian.</td></tr>
            <tr><td><strong>D1-D5</strong></td><td>5 Data Store Terpusat</td><td>Data Store</td><td>D1 Admin, D2 UMKM, D3 Kategori, D4 Produk, D5 Log Kunjungan & Pencarian.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB DFD LEVEL 1 -->
    <div id="tab-dfd1" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>🔍</span> Tab 3: DFD Level 1 (Breakdown Proses 3.0: Pengelolaan Kategori & Produk)
        </div>
        <p class="card-subtitle">Dekomposisi bertahap dari input kategori hingga tayang di etalase masyarakat.</p>
        <div class="step-list">
          <div class="step-item">
            <div class="step-num">3.1</div>
            <div>
              <strong>Pengelolaan Data Kategori Produk</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Input & pembaruan kategori unggulan daerah Gorontalo &rarr; disimpan ke D3 Data Kategori Produk.</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">3.2</div>
            <div>
              <strong>Input & Validasi Spesifikasi Produk</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Input formulir nama produk, deskripsi, dan kisaran harga &rarr; verifikasi silang ke D2 (UMKM) dan D3 (Kategori).</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">3.3</div>
            <div>
              <strong>Unggah & Kurasi Foto/Media Produk</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Validasi kelayakan resolusi foto produk resmi &rarr; mengaitkan URL foto dengan draft produk.</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">3.4</div>
            <div>
              <strong>Publikasi & Pembaruan Status Etalase</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Pengaturan status (Tayang / Arsip) &rarr; penyimpanan ke D4 Data Produk UMKM &rarr; konfirmasi ke Admin.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB ERD -->
    <div id="tab-erd" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>🗄️</span> Tab 4: Entity-Relationship Diagram (ERD) & Kardinalitas
        </div>
        <p class="card-subtitle">Model data terstandarisasi dengan pemisahan atribut Primary Key (+) dan Foreign Key (#).</p>
        <div class="grid-2" style="margin-bottom: 20px;">
          <div style="background: #171b26; border: 1px solid #7c3aed; border-radius: 8px; padding: 14px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
            <strong style="color: #c084fc; font-size: 14px;">ADMIN_DINAS</strong><br>
            + id_admin : INT [PK]<br>
            username, password_hash, nama_petugas, nip, email, no_telepon, role, created_at
          </div>
          <div style="background: #171b26; border: 1px solid #0891b2; border-radius: 8px; padding: 14px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
            <strong style="color: #22d3ee; font-size: 14px;">UMKM</strong><br>
            + id_umkm : INT [PK] | # id_admin : INT [FK]<br>
            nama_umkm, nama_pemilik, nib_izin_usaha, alamat_lengkap, kecamatan, kabupaten_kota, no_whatsapp, email_umkm, status_verifikasi, tanggal_daftar
          </div>
          <div style="background: #171b26; border: 1px solid #16a34a; border-radius: 8px; padding: 14px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
            <strong style="color: #4ade80; font-size: 14px;">KATEGORI</strong><br>
            + id_kategori : INT [PK]<br>
            nama_kategori, slug_kategori, deskripsi, icon_kategori
          </div>
          <div style="background: #171b26; border: 1px solid #ea580c; border-radius: 8px; padding: 14px; font-size: 12px; font-family: 'JetBrains Mono', monospace;">
            <strong style="color: #fb923c; font-size: 14px;">PRODUK</strong><br>
            + id_produk : INT [PK] | # id_umkm, # id_kategori, # id_admin [FK]<br>
            nama_produk, deskripsi_produk, kisaran_harga_min, kisaran_harga_max, satuan_produk, foto_utama, status_tayang, total_dilihat, created_at
          </div>
        </div>
      </div>
    </div>

    <!-- TAB PANDUAN LINK SHARE -->
    <div id="tab-guide" class="tab-content">
      <div class="card">
        <div class="card-title">
          <span>🚀</span> Tab 5: Panduan Mendapatkan Link Share Draw.io Publik Bebas Permission Request
        </div>
        <p class="card-subtitle">Ikuti langkah mudah di bawah ini agar dosen dapat langsung membuka diagram Anda tanpa meminta izin akses.</p>
        <div class="step-list">
          <div class="step-item">
            <div class="step-num">1</div>
            <div>
              <strong>Buka Aplikasi Draw.io Web</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Buka <a href="https://app.diagrams.net/" target="_blank" style="color: #38bdf8;">https://app.diagrams.net/</a>, lalu pilih <strong>"Open Existing Diagram"</strong> dan pilih berkas <code>Sistem_Katalog_UMKM_Gorontalo.drawio</code>.</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">2</div>
            <div>
              <strong>Simpan ke Google Drive Anda</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Klik menu <strong>File &rarr; Save As... &rarr; Pilih Google Drive</strong>. Beri nama berkas: <code>Tugas5_StudiKasus18_[Nama Anda]_[NIM].drawio</code>.</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">3</div>
            <div>
              <strong>Ubah Akses Berbagi ke Publik ("Anyone with the link")</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Buka Google Drive &rarr; klik kanan pada berkas Draw.io tersebut &rarr; klik <strong>Share (Bagikan)</strong>. Ubah akses dari <em>Restricted</em> ke <strong>"Anyone with the link" (Viewer)</strong>.</p>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">4</div>
            <div>
              <strong>Salin Link dan Tempelkan ke LMS</strong>
              <p style="color: var(--text-muted); font-size: 13px;">Klik <strong>Copy link (Salin tautan)</strong>, lalu tempelkan link tersebut ke format jawaban tugas di LMS.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer>
    Tugas 5 Arsitektur Sistem Informasi &bull; Studi Kasus 18: Sistem Katalog Online Terpusat Produk UMKM Lokal (Dinas Koperasi & UKM Gorontalo)
  </footer>

  <script>
    function openTab(evt, tabName) {
      const tabContents = document.querySelectorAll('.tab-content');
      tabContents.forEach(tc => tc.classList.remove('active'));

      const tabBtns = document.querySelectorAll('.tab-btn');
      tabBtns.forEach(btn => btn.classList.remove('active'));

      document.getElementById(tabName).classList.add('active');
      evt.currentTarget.classList.add('active');
    }

    function copyText(elementId) {
      const text = document.getElementById(elementId).innerText;
      navigator.clipboard.writeText(text).then(() => {
        alert("Format teks tugas berhasil disalin ke clipboard!");
      }).catch(err => {
        console.error('Gagal menyalin: ', err);
      });
    }
  </script>
</body>
</html>
'''

with open(r"d:\kuliah\Arsitektur Sistem Informasi\tugas-5\index.html", "w", encoding="utf-8") as f:
    f.write(html_content.strip())

print("Updated index.html portal successfully!")
