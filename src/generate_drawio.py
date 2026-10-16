import html
import os

def create_drawio_xml():
    cell_id = 100
    def get_id():
        nonlocal cell_id
        cell_id += 1
        return str(cell_id)

    # =========================================================================
    # PAGE 1: DIAGRAM KONTEKS (CONTEXT DIAGRAM)
    # Page size: 1260 x 820
    # =========================================================================
    p1_cells = []
    
    # Title Banner
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;DIAGRAM KONTEKS (LEVEL 0) - SISTEM KATALOG ONLINE TERPUSAT PRODUK UMKM GORONTALO&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px; font-weight: normal;&quot;&gt;Studi Kasus 18: Dinas Koperasi dan UKM Gorontalo | Etalase Promosi Digital Terpusat (Non-Transaksi Langsung)&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;fontColor=#ffffff;fontSize=14;fontFamily=Helvetica;align=center;" vertex="1" parent="1">
      <mxGeometry x="40" y="25" width="1180" height="55" as="geometry" />
    </mxCell>
    ''')

    # External Entity 1: Admin Dinas
    admin_id = get_id()
    p1_cells.append(f'''
    <mxCell id="{admin_id}" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;ADMIN SISTEM&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 12px;&quot;&gt;(Dinas Koperasi &amp;amp; UKM)&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px; font-weight: normal;&quot;&gt;&amp;bull; Registrasi &amp;amp; verifikasi UMKM&lt;br&gt;&amp;bull; Unggah spesifikasi &amp;amp; foto produk&lt;br&gt;&amp;bull; Kurasi akurasi data katalog&lt;br&gt;&amp;bull; Kelola rumpun kategori produk&lt;br&gt;&amp;bull; Pantau statistik minat publik&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=12;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="50" y="190" width="220" height="200" as="geometry" />
    </mxCell>
    ''')

    # Main System (Process 0.0)
    sys_id = get_id()
    p1_cells.append(f'''
    <mxCell id="{sys_id}" value="&lt;b style=&quot;font-size: 16px;&quot;&gt;0.0&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 13px;&quot;&gt;SISTEM INFORMASI KATALOG ONLINE&lt;br&gt;TERPUSAT PRODUK UMKM LOKAL&lt;br&gt;GORONTALO&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px; font-weight: normal;&quot;&gt;(Etalase Promosi Digital Terpusat &amp;amp;&lt;br&gt;Direktori Kontak Resmi Pelaku UMKM)&lt;/font&gt;" style="rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=12;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2.5;" vertex="1" parent="1">
      <mxGeometry x="470" y="170" width="320" height="240" as="geometry" />
    </mxCell>
    ''')

    # External Entity 2: Masyarakat / Publik
    public_id = get_id()
    p1_cells.append(f'''
    <mxCell id="{public_id}" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;MASYARAKAT / PUBLIK&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 12px;&quot;&gt;(Pengunjung Katalog)&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 10px; font-weight: normal;&quot;&gt;&amp;bull; Cari produk per kategori lokal&lt;br&gt;&amp;bull; Cari produk via kata kunci&lt;br&gt;&amp;bull; Telusuri rincian detail &amp;amp; harga&lt;br&gt;&amp;bull; Dapatkan kontak resmi penjual&lt;br&gt;&amp;bull; Hubungi UMKM via WA mandiri&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=12;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="990" y="190" width="220" height="200" as="geometry" />
    </mxCell>
    ''')

    # Flow Admin -> System
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1.&lt;/b&gt; Kredensial Login Admin&#xa;&lt;b&gt;2.&lt;/b&gt; Data Profil &amp; Legalitas UMKM&#xa;&lt;b&gt;3.&lt;/b&gt; Data Kategori &amp; Spesifikasi Produk&#xa;&lt;b&gt;4.&lt;/b&gt; Berkas Foto &amp; Status Tayang" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#2563eb;strokeWidth=2;fontSize=9.5;fontColor=#1e3a8a;align=left;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_id}" target="{sys_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="-12" />
      </mxGeometry>
    </mxCell>
    ''')

    # Flow System -> Admin
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1.&lt;/b&gt; Status Autentikasi &amp; Sesi Login&#xa;&lt;b&gt;2.&lt;/b&gt; Konfirmasi Simpan/Update UMKM&#xa;&lt;b&gt;3.&lt;/b&gt; Notifikasi Publikasi Produk&#xa;&lt;b&gt;4.&lt;/b&gt; Laporan Statistik Katalog UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.75;entryDx=0;entryDy=0;exitX=0;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#9333ea;strokeWidth=2;fontSize=9.5;fontColor=#6b21a8;align=left;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sys_id}" target="{admin_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="12" />
      </mxGeometry>
    </mxCell>
    ''')

    # Flow Masyarakat -> System
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1.&lt;/b&gt; Kata Kunci Pencarian Produk&#xa;&lt;b&gt;2.&lt;/b&gt; Pilihan Filter Kategori Produk&#xa;&lt;b&gt;3.&lt;/b&gt; Permintaan Detail &amp; Foto Produk&#xa;&lt;b&gt;4.&lt;/b&gt; Permintaan Kontak Penjual UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#059669;strokeWidth=2;fontSize=9.5;fontColor=#065f46;align=right;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{public_id}" target="{sys_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="-12" />
      </mxGeometry>
    </mxCell>
    ''')

    # Flow System -> Masyarakat
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1.&lt;/b&gt; Tampilan Etalase Katalog Produk&#xa;&lt;b&gt;2.&lt;/b&gt; Hasil Pencarian &amp; Filter Produk&#xa;&lt;b&gt;3.&lt;/b&gt; Informasi Spesifikasi &amp; Kisaran Harga&#xa;&lt;b&gt;4.&lt;/b&gt; Kontak WhatsApp, Sosmed &amp; Alamat UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.75;entryDx=0;entryDy=0;exitX=1;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#db2777;strokeWidth=2;fontSize=9.5;fontColor=#9d174d;align=right;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sys_id}" target="{public_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="12" />
      </mxGeometry>
    </mxCell>
    ''')

    # Notes & Rule Legend Box
    p1_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;Catatan Arsitektur Sistem Informasi (Studi Kasus 18):&lt;/b&gt;&lt;br&gt;1. &lt;b&gt;Karakteristik Etalase Digital Terpusat:&lt;/b&gt; Sistem berfungsi murni mempromosikan produk lokal Gorontalo dan mempertemukan calon pembeli dengan pelaku usaha secara transparan.&lt;br&gt;2. &lt;b&gt;Batasan Penting (Non-Transaksional):&lt;/b&gt; Sistem sama sekali &lt;u&gt;tidak menangani transaksi penjualan langsung&lt;/u&gt; (tidak ada payment gateway, keranjang belanja checkout, maupun kurir pengiriman).&lt;br&gt;3. &lt;b&gt;Hubungan Mandiri Konsumen-UMKM:&lt;/b&gt; Konsumen menghubungi pemilik usaha secara independen melalui kontak WhatsApp/telepon yang tercantum pada detail katalog.&lt;br&gt;4. &lt;b&gt;Otoritas Terpusat Dinas:&lt;/b&gt; Petugas Dinas Koperasi dan UKM bertindak sebagai kurator tunggal dalam mendaftarkan UMKM serta menjaga validitas informasi produk." style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#cbd5e1;fontSize=10.5;fontFamily=Helvetica;align=left;spacingLeft=15;" vertex="1" parent="1">
      <mxGeometry x="40" y="450" width="1180" height="120" as="geometry" />
    </mxCell>
    ''')

    # =========================================================================
    # PAGE 2: DFD LEVEL 0
    # Page size: 1280 x 820
    # Clean 5-column layout:
    # Col 1: Admin (x=40)
    # Col 2: Admin Processes (x=280)
    # Col 3: Data Stores D1-D5 (x=550)
    # Col 4: Public Processes (x=830)
    # Col 5: Masyarakat (x=1080)
    # =========================================================================
    p2_cells = []

    # Title Banner
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;DATA FLOW DIAGRAM (DFD) LEVEL 0 - SISTEM KATALOG ONLINE TERPUSAT PRODUK UMKM GORONTALO&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px; font-weight: normal;&quot;&gt;Dekomposisi Sistem Menjadi 6 Proses Utama, 5 Data Store, dan 2 Entitas Eksternal (Tata Letak Jalur Bebas Tabrakan)&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;fontColor=#ffffff;fontSize=14;fontFamily=Helvetica;align=center;" vertex="1" parent="1">
      <mxGeometry x="40" y="20" width="1200" height="50" as="geometry" />
    </mxCell>
    ''')

    # External Entity: Admin Dinas (Col 1)
    admin_0_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{admin_0_id}" value="&lt;b style=&quot;font-size: 12px;&quot;&gt;ADMIN SISTEM&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 11px;&quot;&gt;(Dinas Koperasi &amp;amp; UKM)&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 9.5px;&quot;&gt;Pengelola &amp;amp; Kurator Data&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="40" y="230" width="170" height="150" as="geometry" />
    </mxCell>
    ''')

    # External Entity: Masyarakat (Col 5)
    public_0_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{public_0_id}" value="&lt;b style=&quot;font-size: 12px;&quot;&gt;MASYARAKAT / PUBLIK&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 11px;&quot;&gt;(Pengunjung Etalase)&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 9.5px;&quot;&gt;Penelusur Produk &amp;amp; Kontak&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="1070" y="230" width="170" height="150" as="geometry" />
    </mxCell>
    ''')

    # Processes Admin Side (Col 2)
    proc1_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc1_id}" value="&lt;b&gt;1.0&lt;/b&gt;&lt;br&gt;Autentikasi &amp;amp; Kelola Akun Admin" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="270" y="90" width="170" height="65" as="geometry" />
    </mxCell>
    ''')

    proc2_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc2_id}" value="&lt;b&gt;2.0&lt;/b&gt;&lt;br&gt;Pengelolaan Data UMKM Lokal" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="270" y="200" width="170" height="65" as="geometry" />
    </mxCell>
    ''')

    proc3_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc3_id}" value="&lt;b&gt;3.0&lt;/b&gt;&lt;br&gt;Pengelolaan Kategori &amp;amp; Produk UMKM" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="270" y="320" width="170" height="75" as="geometry" />
    </mxCell>
    ''')

    proc6_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc6_id}" value="&lt;b&gt;6.0&lt;/b&gt;&lt;br&gt;Pembuatan Laporan &amp;amp; Statistik Katalog" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="270" y="470" width="170" height="70" as="geometry" />
    </mxCell>
    ''')

    # Data Stores (Col 3: Center)
    d1_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{d1_id}" value="&lt;b&gt;D1&lt;/b&gt; | Data Pengguna Admin" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="540" y="100" width="180" height="45" as="geometry" />
    </mxCell>
    ''')

    d2_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{d2_id}" value="&lt;b&gt;D2&lt;/b&gt; | Data UMKM Lokal" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="540" y="210" width="180" height="45" as="geometry" />
    </mxCell>
    ''')

    d3_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{d3_id}" value="&lt;b&gt;D3&lt;/b&gt; | Data Kategori Produk" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="540" y="315" width="180" height="45" as="geometry" />
    </mxCell>
    ''')

    d4_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{d4_id}" value="&lt;b&gt;D4&lt;/b&gt; | Data Produk UMKM" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="540" y="415" width="180" height="45" as="geometry" />
    </mxCell>
    ''')

    d5_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{d5_id}" value="&lt;b&gt;D5&lt;/b&gt; | Data Log Kunjungan &amp;amp; Cari" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="540" y="525" width="180" height="45" as="geometry" />
    </mxCell>
    ''')

    # Processes Public Side (Col 4)
    proc4_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc4_id}" value="&lt;b&gt;4.0&lt;/b&gt;&lt;br&gt;Pencarian &amp;amp; Filter Katalog Produk" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="810" y="210" width="170" height="65" as="geometry" />
    </mxCell>
    ''')

    proc5_id = get_id()
    p2_cells.append(f'''
    <mxCell id="{proc5_id}" value="&lt;b&gt;5.0&lt;/b&gt;&lt;br&gt;Penayangan Detail Produk &amp;amp; Kontak UMKM" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="810" y="340" width="170" height="75" as="geometry" />
    </mxCell>
    ''')

    # ------------------ EDGES DFD LEVEL 0 ------------------
    # Process 1.0 (Auth)
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Kredensial Login" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_0_id}" target="{proc1_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Validasi Akun" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc1_id}" target="{d1_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Process 2.0 (UMKM)
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Formulir Data UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.25;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_0_id}" target="{proc2_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Simpan/Update UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc2_id}" target="{d2_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Process 3.0 (Kategori & Produk)
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Data Kategori &amp; Produk" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.75;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_0_id}" target="{proc3_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Simpan Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.25;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc3_id}" target="{d3_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Simpan Produk &amp; Foto" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.75;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc3_id}" target="{d4_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Process 4.0 (Pencarian Katalog - Public)
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Kata Kunci &amp; Filter Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.25;exitDx=0;exitDy=0;entryX=1;entryY=0.3;entryDx=0;entryDy=0;strokeColor=#059669;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{public_0_id}" target="{proc4_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="-8" />
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Daftar Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.2;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d3_id}" target="{proc4_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="760" y="338" />
          <mxPoint x="760" y="223" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Daftar Produk Aktif" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.3;exitDx=0;exitDy=0;entryX=0;entryY=0.7;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d4_id}" target="{proc4_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="780" y="428" />
          <mxPoint x="780" y="255" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Hasil Katalog Produk" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.8;exitDx=0;exitDy=0;entryX=0;entryY=0.45;entryDx=0;entryDy=0;strokeColor=#db2777;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc4_id}" target="{public_0_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="8" />
      </mxGeometry>
    </mxCell>
    ''')

    # Process 5.0 (Detail & Kontak Penjual)
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Pilih Produk / Klik Detail" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.75;exitDx=0;exitDy=0;entryX=1;entryY=0.3;entryDx=0;entryDy=0;strokeColor=#059669;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{public_0_id}" target="{proc5_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="-8" />
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Detail &amp; Foto Produk" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.7;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d4_id}" target="{proc5_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="750" y="446" />
          <mxPoint x="750" y="377" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Kontak WA &amp; Alamat UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d2_id}" target="{proc5_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="795" y="232" />
          <mxPoint x="795" y="300" />
          <mxPoint x="895" y="300" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Halaman Detail &amp; Kontak UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.8;exitDx=0;exitDy=0;entryX=0;entryY=0.9;entryDx=0;entryDy=0;strokeColor=#db2777;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc5_id}" target="{public_0_id}">
      <mxGeometry relative="1" as="geometry">
        <mxPoint as="offset" y="8" />
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Catat Log Cari / View" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.8;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#9333ea;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc5_id}" target="{d5_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="760" y="400" />
          <mxPoint x="760" y="547" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')

    # Process 6.0 (Pelaporan Dinas) - Routed cleanly to avoid collision!
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Statistik Log Kunjungan" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.7;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d5_id}" target="{proc6_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Rekap Data UMKM &amp; Produk" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.8;exitDx=0;exitDy=0;entryX=1;entryY=0.2;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d2_id}" target="{proc6_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="500" y="246" />
          <mxPoint x="500" y="484" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="Laporan Statistik Katalog UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;strokeColor=#9333ea;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{proc6_id}" target="{admin_0_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="125" y="505" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')

    # Legend at bottom
    p2_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;Keterangan DFD Level 0:&lt;/b&gt; &lt;b&gt;Entitas Eksternal:&lt;/b&gt; Persegi berwarna (Admin Dinas Koperasi &amp;amp; UKM, Masyarakat Pengunjung) | &lt;b&gt;Proses:&lt;/b&gt; Kotak Tumpul 1.0 s.d 6.0 | &lt;b&gt;Data Store:&lt;/b&gt; Kotak Terbuka D1 s.d D5. Jalur aliran data telah dipisahkan secara tegas antara jalur pengelolaan kurasi dinas (kiri) dan jalur pencarian publik (kanan) tanpa modul transaksi penjualan langsung." style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#ced4da;fontSize=10.5;fontFamily=Helvetica;align=left;spacingLeft=15;" vertex="1" parent="1">
      <mxGeometry x="40" y="605" width="1200" height="50" as="geometry" />
    </mxCell>
    ''')

    # =========================================================================
    # PAGE 3: DFD LEVEL 1 (PROSES 3.0: PENGELOLAAN KATEGORI & PRODUK UMKM)
    # Page size: 1260 x 820
    # =========================================================================
    p3_cells = []

    # Title Banner
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;DATA FLOW DIAGRAM (DFD) LEVEL 1 - BREAKDOWN PROSES 3.0: PENGELOLAAN KATEGORI &amp;amp; PRODUK UMKM&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px; font-weight: normal;&quot;&gt;Dekomposisi Mendalam 4 Sub-Proses Kurasi, Validasi Spesifikasi Produk, Media Foto, dan Publikasi Etalase (Jalur Aliran Bebas Tabrakan)&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;fontColor=#ffffff;fontSize=14;fontFamily=Helvetica;align=center;" vertex="1" parent="1">
      <mxGeometry x="40" y="20" width="1180" height="50" as="geometry" />
    </mxCell>
    ''')

    # Admin Entity (Left)
    admin_1_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{admin_1_id}" value="&lt;b style=&quot;font-size: 13px;&quot;&gt;ADMIN SISTEM&lt;/b&gt;&lt;br&gt;&lt;b style=&quot;font-size: 11px;&quot;&gt;(Dinas Koperasi &amp;amp; UKM)&lt;/b&gt;&lt;br&gt;&lt;br&gt;&lt;font style=&quot;font-size: 9.5px;&quot;&gt;Petugas Kurasi &amp;amp; Input&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="40" y="260" width="180" height="150" as="geometry" />
    </mxCell>
    ''')

    # Sub-processes (Center: x=400, w=190)
    sub31_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{sub31_id}" value="&lt;b&gt;3.1&lt;/b&gt;&lt;br&gt;Pengelolaan Data Kategori Produk" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="390" y="95" width="200" height="70" as="geometry" />
    </mxCell>
    ''')

    sub32_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{sub32_id}" value="&lt;b&gt;3.2&lt;/b&gt;&lt;br&gt;Input &amp;amp; Validasi Spesifikasi Produk" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="390" y="235" width="200" height="70" as="geometry" />
    </mxCell>
    ''')

    sub33_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{sub33_id}" value="&lt;b&gt;3.3&lt;/b&gt;&lt;br&gt;Unggah &amp;amp; Kurasi Foto/Media Produk" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="390" y="375" width="200" height="70" as="geometry" />
    </mxCell>
    ''')

    sub34_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{sub34_id}" value="&lt;b&gt;3.4&lt;/b&gt;&lt;br&gt;Publikasi &amp;amp; Pembaruan Status Etalase" style="rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;fontFamily=Helvetica;align=center;shadow=1;strokeWidth=1.5;" vertex="1" parent="1">
      <mxGeometry x="390" y="515" width="200" height="70" as="geometry" />
    </mxCell>
    ''')

    # Data Stores (Right: x=800, w=200)
    d3_1_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{d3_1_id}" value="&lt;b&gt;D3&lt;/b&gt; | Data Kategori Produk" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="800" y="105" width="200" height="50" as="geometry" />
    </mxCell>
    ''')

    d2_1_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{d2_1_id}" value="&lt;b&gt;D2&lt;/b&gt; | Data UMKM Lokal" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="800" y="245" width="200" height="50" as="geometry" />
    </mxCell>
    ''')

    d4_1_id = get_id()
    p3_cells.append(f'''
    <mxCell id="{d4_1_id}" value="&lt;b&gt;D4&lt;/b&gt; | Data Produk UMKM" style="shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontFamily=Helvetica;align=center;strokeWidth=2;" vertex="1" parent="1">
      <mxGeometry x="800" y="475" width="200" height="50" as="geometry" />
    </mxCell>
    ''')

    # Flows Process 3.1
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Nama &amp; Deskripsi Kategori Baru" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_1_id}" target="{sub31_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="130" y="130" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Simpan/Update Master Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sub31_id}" target="{d3_1_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Flows Process 3.2
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Form Detail Produk &amp; Harga" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.25;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_1_id}" target="{sub32_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Cek Validitas ID Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.2;exitY=1;exitDx=0;exitDy=0;entryX=0.8;entryY=0;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d3_1_id}" target="{sub32_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="840" y="195" />
          <mxPoint x="550" y="195" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Cek Validitas ID UMKM" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{d2_1_id}" target="{sub32_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Draft Data Produk Tervalidasi" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeColor=#059669;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sub32_id}" target="{sub33_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Flows Process 3.3
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Berkas Foto Produk (JPG/PNG)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.75;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_1_id}" target="{sub33_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Paket Produk Lengkap (Data + URL Foto)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeColor=#059669;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sub33_id}" target="{sub34_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # Flows Process 3.4 - Completely re-routed so lines NEVER intersect!
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Instruksi Status (Tayang/Arsip)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;strokeColor=#2563eb;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{admin_1_id}" target="{sub34_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="130" y="536" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Simpan/Update Data Produk Siap Tayang" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#333333;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sub34_id}" target="{d4_1_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="700" y="550" />
          <mxPoint x="700" y="500" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="Konfirmasi Publikasi Berhasil" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.75;exitDx=0;exitDy=0;entryX=0.2;entryY=1;entryDx=0;entryDy=0;strokeColor=#9333ea;strokeWidth=1.5;fontSize=9;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{sub34_id}" target="{admin_1_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="290" y="568" />
          <mxPoint x="290" y="610" />
          <mxPoint x="76" y="610" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')

    # Legend at bottom
    p3_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;Penjelasan Alur Dekomposisi 3.0:&lt;/b&gt; Admin mengelola kategori di 3.1 &amp;rarr; Menginput detail spesifikasi produk serta memilih relasi UMKM &amp;amp; Kategori di 3.2 &amp;rarr; Mengunggah foto produk beresolusi baik di 3.3 &amp;rarr; Melakukan kurasi akhir dan mengaktifkan status publikasi etalase di 3.4 &amp;rarr; Data disimpan ke D4 (Data Produk UMKM)." style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#ced4da;fontSize=10.5;fontFamily=Helvetica;align=left;spacingLeft=15;" vertex="1" parent="1">
      <mxGeometry x="40" y="640" width="1180" height="50" as="geometry" />
    </mxCell>
    ''')

    # =========================================================================
    # PAGE 4: ENTITY-RELATIONSHIP DIAGRAM (ERD)
    # Page size: 1260 x 840
    # Clean 3-column layout with 80px vertical gaps:
    # Col 1: ADMIN_DINAS (y=80), KATEGORI (y=420)
    # Col 2: UMKM (y=80), PRODUK (y=420)
    # Col 3: LOG_PENCARIAN (y=80), FOTO_PRODUK (y=420)
    # =========================================================================
    p4_cells = []

    # Title Banner
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;ENTITY-RELATIONSHIP DIAGRAM (ERD) - SISTEM KATALOG ONLINE TERPUSAT PRODUK UMKM GORONTALO&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px; font-weight: normal;&quot;&gt;Model Data Konseptual &amp;amp; Logikal Basis Data (Primary Key [PK], Foreign Key [FK], dan Kardinalitas Relasi 1:N Terkoordinasi Luas Tanpa Overlap)&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#1e293b;strokeColor=#0f172a;fontColor=#ffffff;fontSize=14;fontFamily=Helvetica;align=center;" vertex="1" parent="1">
      <mxGeometry x="40" y="20" width="1180" height="50" as="geometry" />
    </mxCell>
    ''')

    # Entity: ADMIN_DINAS (Col 1 Top)
    ent_admin_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_admin_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;4&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #6d28d9; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;ADMIN_DINAS&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_admin&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;INT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  username&lt;/td&gt;&lt;td&gt;VARCHAR(50)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  password_hash&lt;/td&gt;&lt;td&gt;VARCHAR(255)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nama_petugas&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nip&lt;/td&gt;&lt;td&gt;VARCHAR(30)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  email&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  no_telepon&lt;/td&gt;&lt;td&gt;VARCHAR(20)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  role&lt;/td&gt;&lt;td&gt;VARCHAR(20)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  created_at&lt;/td&gt;&lt;td&gt;TIMESTAMP&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#faf5ff;strokeColor=#9333ea;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="50" y="85" width="230" height="235" as="geometry" />
    </mxCell>
    ''')

    # Entity: UMKM (Col 2 Top)
    ent_umkm_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_umkm_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;3&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #0e7490; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;UMKM&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_umkm&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;INT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_admin&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nama_umkm&lt;/td&gt;&lt;td&gt;VARCHAR(150)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nama_pemilik&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nib_izin_usaha&lt;/td&gt;&lt;td&gt;VARCHAR(50)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  alamat_lengkap&lt;/td&gt;&lt;td&gt;TEXT&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  kecamatan&lt;/td&gt;&lt;td&gt;VARCHAR(50)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  kabupaten_kota&lt;/td&gt;&lt;td&gt;VARCHAR(50)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  no_whatsapp&lt;/td&gt;&lt;td&gt;VARCHAR(20)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  email_umkm&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  tautan_sosmed&lt;/td&gt;&lt;td&gt;VARCHAR(255)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  status_verifikasi&lt;/td&gt;&lt;td&gt;ENUM&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  tanggal_daftar&lt;/td&gt;&lt;td&gt;DATE&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ecfeff;strokeColor=#06b6d4;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="480" y="85" width="240" height="265" as="geometry" />
    </mxCell>
    ''')

    # Entity: LOG_PENCARIAN (Col 3 Top)
    ent_log_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_log_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;4&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #475569; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;LOG_PENCARIAN&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_log&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;BIGINT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  kata_kunci&lt;/td&gt;&lt;td&gt;VARCHAR(150)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  waktu_akses&lt;/td&gt;&lt;td&gt;TIMESTAMP&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  ip_pengunjung&lt;/td&gt;&lt;td&gt;VARCHAR(45)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_kategori&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK, Null]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_produk&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK, Null]&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#64748b;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="900" y="95" width="230" height="180" as="geometry" />
    </mxCell>
    ''')

    # Entity: KATEGORI (Col 1 Bottom)
    ent_kat_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_kat_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;4&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #15803d; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;KATEGORI&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_kategori&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;INT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nama_kategori&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  slug_kategori&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  deskripsi&lt;/td&gt;&lt;td&gt;TEXT&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  icon_kategori&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#22c55e;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="50" y="420" width="230" height="160" as="geometry" />
    </mxCell>
    ''')

    # Entity: PRODUK (Col 2 Bottom)
    ent_prod_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_prod_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;3&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #c2410c; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;PRODUK&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_produk&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;INT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_umkm&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_kategori&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_admin&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  nama_produk&lt;/td&gt;&lt;td&gt;VARCHAR(150)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  deskripsi_produk&lt;/td&gt;&lt;td&gt;TEXT&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  kisaran_harga_min&lt;/td&gt;&lt;td&gt;DECIMAL(12,2)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  kisaran_harga_max&lt;/td&gt;&lt;td&gt;DECIMAL(12,2)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  satuan_produk&lt;/td&gt;&lt;td&gt;VARCHAR(50)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  foto_utama&lt;/td&gt;&lt;td&gt;VARCHAR(255)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  status_tayang&lt;/td&gt;&lt;td&gt;ENUM&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  total_dilihat&lt;/td&gt;&lt;td&gt;INT&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  created_at&lt;/td&gt;&lt;td&gt;TIMESTAMP&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff7ed;strokeColor=#f97316;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="480" y="420" width="240" height="280" as="geometry" />
    </mxCell>
    ''')

    # Entity: FOTO_PRODUK (Col 3 Bottom)
    ent_foto_id = get_id()
    p4_cells.append(f'''
    <mxCell id="{ent_foto_id}" value="&lt;table border=&quot;0&quot; cellpadding=&quot;4&quot; cellspacing=&quot;0&quot; style=&quot;width: 100%; border-collapse: collapse;&quot;&gt;&lt;tr style=&quot;background-color: #7e22ce; color: #ffffff;&quot;&gt;&lt;td colspan=&quot;2&quot; align=&quot;center&quot;&gt;&lt;b&gt;FOTO_PRODUK&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;&lt;font color=&quot;#e11d48&quot;&gt;+ id_foto&lt;/font&gt;&lt;/b&gt;&lt;/td&gt;&lt;td&gt;&lt;b&gt;INT [PK]&lt;/b&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;font color=&quot;#2563eb&quot;&gt;# id_produk&lt;/font&gt;&lt;/td&gt;&lt;td&gt;INT [FK]&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  url_file_foto&lt;/td&gt;&lt;td&gt;VARCHAR(255)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  judul_foto&lt;/td&gt;&lt;td&gt;VARCHAR(100)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  urutan_tampil&lt;/td&gt;&lt;td&gt;INT&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;  is_thumbnail&lt;/td&gt;&lt;td&gt;BOOLEAN&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#faf5ff;strokeColor=#a855f7;strokeWidth=2;shadow=1;align=left;spacing=0;overflow=hidden;" vertex="1" parent="1">
      <mxGeometry x="900" y="440" width="230" height="175" as="geometry" />
    </mxCell>
    ''')

    # Connectors & Cardinalities:
    # 1. ADMIN_DINAS (1) -> (N) UMKM
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Mengelola / Verifikasi" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.4;exitDx=0;exitDy=0;entryX=0;entryY=0.35;entryDx=0;entryDy=0;strokeColor=#0284c7;strokeWidth=2;fontSize=10;fontColor=#0369a1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_admin_id}" target="{ent_umkm_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # 2. ADMIN_DINAS (1) -> (N) PRODUK
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Mengurasi / Input" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.8;exitDx=0;exitDy=0;entryX=0;entryY=0.3;entryDx=0;entryDy=0;strokeColor=#0284c7;strokeWidth=2;fontSize=10;fontColor=#0369a1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_admin_id}" target="{ent_prod_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="380" y="273" />
          <mxPoint x="380" y="504" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')

    # 3. UMKM (1) -> (N) PRODUK (Spacious 70px vertical channel!)
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Memproduksi / Memiliki" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeColor=#dc2626;strokeWidth=2;fontSize=10;fontColor=#b91c1c;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_umkm_id}" target="{ent_prod_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # 4. KATEGORI (1) -> (N) PRODUK (Clean horizontal line!)
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Menaungi / Kategori" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.65;entryDx=0;entryDy=0;strokeColor=#16a34a;strokeWidth=2;fontSize=10;fontColor=#15803d;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_kat_id}" target="{ent_prod_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # 5. PRODUK (1) -> (N) FOTO_PRODUK (Clean horizontal line!)
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Memiliki Galeri" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#9333ea;strokeWidth=2;fontSize=10;fontColor=#7e22ce;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_prod_id}" target="{ent_foto_id}">
      <mxGeometry relative="1" as="geometry" />
    </mxCell>
    ''')

    # 6. PRODUK (1) -> (N) LOG_PENCARIAN
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;1 : N&lt;/b&gt;&lt;br&gt;Dicatat di Log" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.2;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;strokeColor=#64748b;strokeWidth=1.5;strokeDasharray=3 3;fontSize=9.5;fontColor=#475569;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="{ent_prod_id}" target="{ent_log_id}">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="810" y="476" />
          <mxPoint x="810" y="320" />
          <mxPoint x="1015" y="320" />
        </Array>
      </mxGeometry>
    </mxCell>
    ''')

    # Legend / Cardinality explanation box
    p4_cells.append(f'''
    <mxCell id="{get_id()}" value="&lt;b&gt;Ringkasan Kardinalitas &amp;amp; Kamus Relasi ERD:&lt;/b&gt;&lt;br&gt;1. &lt;b&gt;ADMIN_DINAS &amp;rarr; UMKM (1:N):&lt;/b&gt; Satu admin dinas memverifikasi &amp;amp; mendaftarkan banyak UMKM; Setiap UMKM dikelola oleh petugas admin.&lt;br&gt;2. &lt;b&gt;ADMIN_DINAS &amp;rarr; PRODUK (1:N):&lt;/b&gt; Satu admin dinas mengurasi/mengunggah banyak produk; Setiap produk dikurasi oleh admin dinas.&lt;br&gt;3. &lt;b&gt;UMKM &amp;rarr; PRODUK (1:N):&lt;/b&gt; Satu UMKM lokal dapat memproduksi/memiliki banyak produk di katalog; Setiap produk berasal dari satu UMKM yang sah.&lt;br&gt;4. &lt;b&gt;KATEGORI &amp;rarr; PRODUK (1:N):&lt;/b&gt; Satu kategori (misal: Kerajinan Karawo, Kuliner, Kopi Pinogu) menaungi banyak produk; Setiap produk masuk dalam 1 kategori utama.&lt;br&gt;5. &lt;b&gt;PRODUK &amp;rarr; FOTO_PRODUK (1:N):&lt;/b&gt; Satu produk etalase dapat memiliki banyak foto galeri/sudut pandang; Setiap foto terikat pada satu produk.&lt;br&gt;&lt;b&gt;Simbol:&lt;/b&gt; &lt;font color=&quot;#e11d48&quot;&gt;&lt;b&gt;+ [PK]&lt;/b&gt;&lt;/font&gt; = Primary Key (Kunci Utama) | &lt;font color=&quot;#2563eb&quot;&gt;&lt;b&gt;# [FK]&lt;/b&gt;&lt;/font&gt; = Foreign Key (Kunci Tamu)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#ced4da;fontSize=10;fontFamily=Helvetica;align=left;spacingLeft=15;" vertex="1" parent="1">
      <mxGeometry x="40" y="725" width="1180" height="90" as="geometry" />
    </mxCell>
    ''')

    # Combine all pages into multi-page mxfile
    xml_content = f'''<mxfile host="app.diagrams.net" modified="2026-10-15T12:00:00.000Z" agent="Antigravity" version="24.0.0" type="device">
  <diagram id="diag-context" name="1. Diagram Konteks">
    <mxGraphModel dx="1280" dy="850" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1280" pageHeight="850" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(p1_cells)}
      </root>
    </mxGraphModel>
  </diagram>
  <diagram id="diag-dfd0" name="2. DFD Level 0">
    <mxGraphModel dx="1280" dy="850" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1280" pageHeight="850" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(p2_cells)}
      </root>
    </mxGraphModel>
  </diagram>
  <diagram id="diag-dfd1" name="3. DFD Level 1 (Proses 3.0)">
    <mxGraphModel dx="1280" dy="850" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1280" pageHeight="850" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(p3_cells)}
      </root>
    </mxGraphModel>
  </diagram>
  <diagram id="diag-erd" name="4. ERD (Katalog UMKM)">
    <mxGraphModel dx="1280" dy="850" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1280" pageHeight="850" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {''.join(p4_cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

    target_file = r"d:\kuliah\Arsitektur Sistem Informasi\tugas-5\Sistem_Katalog_UMKM_Gorontalo.drawio"
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(xml_content.strip())
    print(f"Successfully updated with collision-free coordinates: {target_file}")

if __name__ == "__main__":
    create_drawio_xml()
