headers = ["ID", "CPMK 012", "CPMK 031", "CPMK 071", "CPMK 072"]
data = [
    ["2101020014", 100, 90, 100, 100],
    ["2101020024", 100, 20, 70, 70],
    ["2101020048", 100, 90, 100, 100],
    ["2101020058", 100, 90, 100, 100],
    ["2101020074", 90, 60, 70, 70],
    ["2101020092", 100, 20, 70, 70],
    ["2101020103", 0, 0, 0, 0],
    ["2101020104", 90, 60, 70, 70],
    ["2101020117", 90, 60, 70, 70],
    ["2201020001", 100, 60, 60, 60],
    ["2201020002", 100, 80, 70, 70],
    ["2201020010", 100, 80, 90, 90],
    ["2201020014", 100, 60, 60, 60],
    ["2201020015", 100, 60, 60, 60],
    ["2201020018", 100, 70, 100, 100],
    ["2201020019", 100, 80, 90, 90],
    ["2201020022", 90, 20, 50, 50],
    ["2201020026", 100, 80, 70, 70],
    ["2201020032", 100, 80, 90, 90],
    ["2201020039", 100, 80, 70, 70],
    ["2201020041", 100, 80, 90, 90],
    ["2201020047", 100, 75, 50, 50],
    ["2201020048", 100, 70, 100, 100],
    ["2201020057", 100, 75, 50, 50],
    ["2201020063", 100, 76, 100, 100],
    ["2201020065", 100, 75, 85, 85],
    ["2201020066", 100, 60, 50, 50],
    ["2201020067", 100, 80, 90, 90],
    ["2201020070", 100, 75, 100, 100],
    ["2201020074", 100, 60, 50, 50],
    ["2201020075", 100, 80, 90, 90],
    ["2201020083", 100, 80, 90, 90],
    ["2201020086", 0, 0, 0, 0],
    ["2201020090", 100, 75, 100, 100],
    ["2201020091", 100, 80, 90, 90],
    ["2201020092", 100, 60, 50, 50],
    ["2201020093", 100, 75, 85, 85],
    ["2201020094", 100, 80, 90, 90],
    ["2201020095", 100, 75, 85, 85],
    ["2201020098", 100, 75, 50, 50],
    ["2201020099", 100, 80, 90, 90],
    ["2201020100", 100, 80, 70, 70],
    ["2201020103", 100, 70, 100, 100],
    ["2201020104", 100, 80, 70, 70],
    ["2201020105", 100, 70, 50, 50],
    ["2201020106", 90, 50, 40, 40],
    ["2201020109", 100, 80, 70, 70],
    ["2201020112", 90, 50, 40, 40],
    ["2201020116", 90, 50, 40, 40],
    ["2201020117", 100, 70, 50, 50],
    ["2201020118", 100, 80, 90, 90],
    ["2201020122", 100, 70, 50, 50],
    ["2201020123", 90, 20, 50, 50],
]

warna = ["#FF5733", "#33FF57", "#3357FF", "#F39C12"]
lebar_kanvas = 1800
tinggi_kanvas = 650
jarak_tepi = 80
lebar_batang = 15
jarak_antar_grup = 20  # Sedikit mengurangi jarak antar grup agar muat 15 mahasiswa
jarak_antar_batang = 0
tinggi_grafik = 400
nilai_maksimum = 100
mahasiswa_per_halaman = 15  # Diubah dari 10 menjadi 15 mahasiswa per halaman

def hitung_statistik(data):
    """Menghitung berbagai statistik untuk setiap kategori CPMK"""
    statistik = {}
    
    # Lewati kolom pertama (ID) dan hitung statistik untuk setiap CPMK
    jumlah_cpmk = len(headers) - 1
    for i in range(jumlah_cpmk):
        nama_cpmk = headers[i+1]
        nilai_cpmk = [row[i+1] for row in data]
        
        # Hitung statistik
        nilai_rata_rata = sum(nilai_cpmk) / len(nilai_cpmk)
        nilai_maksimum = max(nilai_cpmk)
        nilai_minimum = min(nilai_cpmk)
        
        # Hitung jumlah mahasiswa yang lulus (nilai >= 60)
        mahasiswa_lulus = sum(1 for nilai in nilai_cpmk if nilai >= 60)
        persentase_lulus = (mahasiswa_lulus / len(nilai_cpmk)) * 100
        
        # Simpan statistik
        statistik[nama_cpmk] = {
            "rata_rata": round(nilai_rata_rata, 2),
            "maksimum": nilai_maksimum,
            "minimum": nilai_minimum,
            "mahasiswa_lulus": mahasiswa_lulus,
            "persentase_lulus": round(persentase_lulus, 2),
            "total_mahasiswa": len(nilai_cpmk)
        }
    
    return statistik

def buat_svg(headers, data_halaman, nomor_halaman, total_halaman):
    svg = []
    svg.append(f'<svg width="{lebar_kanvas}" height="{tinggi_kanvas}" xmlns="http://www.w3.org/2000/svg">')
    
    # Judul halaman
    svg.append(f'<text x="{lebar_kanvas/2}" y="30" font-size="16" text-anchor="middle" font-weight="bold">Histogram Nilai CPMK - Halaman {nomor_halaman} dari {total_halaman}</text>')
    
    # Sumbu
    svg.append(f'<line x1="{jarak_tepi}" y1="{jarak_tepi}" x2="{jarak_tepi}" y2="{tinggi_kanvas - jarak_tepi}" stroke="black" stroke-width="2"/>')
    svg.append(f'<line x1="{jarak_tepi}" y1="{tinggi_kanvas - jarak_tepi}" x2="{lebar_kanvas - jarak_tepi}" y2="{tinggi_kanvas - jarak_tepi}" stroke="black" stroke-width="2"/>')
    
    # Label sumbu Y
    for val in range(0, nilai_maksimum + 10, 10):
        y = tinggi_kanvas - jarak_tepi - (val / nilai_maksimum) * tinggi_grafik
        svg.append(f'<line x1="{jarak_tepi - 5}" y1="{y}" x2="{jarak_tepi}" y2="{y}" stroke="black"/>')
        svg.append(f'<text x="{jarak_tepi - 10}" y="{y + 3}" font-size="10" text-anchor="end">{val}</text>')
    
    # Batang-batang
    for i, row in enumerate(data_halaman):
        id_mahasiswa = row[0]
        nilai = row[1:]
        posisi_awal_grup_x = jarak_tepi + i * ((lebar_batang * len(nilai)) + jarak_antar_grup)
        for j, skor in enumerate(nilai):
            tinggi = (skor / nilai_maksimum) * tinggi_grafik
            x0 = posisi_awal_grup_x + j * lebar_batang
            y0 = tinggi_kanvas - jarak_tepi - tinggi
            warna_batang = warna[j % len(warna)]
            svg.append(f'<rect x="{x0}" y="{y0}" width="{lebar_batang}" height="{tinggi}" fill="{warna_batang}" stroke="black"/>')
            svg.append(f'<text x="{x0 + lebar_batang / 2}" y="{y0 - 5}" font-size="9" text-anchor="middle">{skor}</text>')
        
        tengah_x = posisi_awal_grup_x + ((lebar_batang * len(nilai)) - jarak_antar_batang) / 2
        svg.append(f'<text x="{tengah_x}" y="{tinggi_kanvas - jarak_tepi + 15}" font-size="10" text-anchor="middle">{id_mahasiswa}</text>')
    
    # Legenda
    posisi_legenda_x = lebar_kanvas - 150
    for i in range(1, len(headers)):
        y = jarak_tepi + (i - 1) * 20
        svg.append(f'<rect x="{posisi_legenda_x}" y="{y}" width="15" height="15" fill="{warna[i - 1]}" />')
        svg.append(f'<text x="{posisi_legenda_x + 20}" y="{y + 12}" font-size="12">{headers[i]}</text>')
    
    svg.append('</svg>')
    return '\n'.join(svg)

def buat_html_dengan_manajemen_data():
    # Hitung statistik
    statistik_cpmk = hitung_statistik(data)
    
    # Hitung jumlah halaman
    total_halaman = (len(data) + mahasiswa_per_halaman - 1) // mahasiswa_per_halaman
    
    berkas_html = []
    
    for nomor_halaman in range(1, total_halaman + 1):
        # Hitung indeks awal dan akhir untuk halaman saat ini
        indeks_awal = (nomor_halaman - 1) * mahasiswa_per_halaman
        indeks_akhir = min(indeks_awal + mahasiswa_per_halaman, len(data))
        data_halaman = data[indeks_awal:indeks_akhir]
        
        # Buat SVG untuk halaman ini
        konten_svg = buat_svg(headers, data_halaman, nomor_halaman, total_halaman)
        
        # Buat berkas HTML untuk halaman ini
        html = []
        html.append('<!DOCTYPE html>')
        html.append('<html lang="id">')
        html.append('<head>')
        html.append('    <meta charset="UTF-8">')
        html.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        html.append('    <title>Manajemen Data CPMK - Halaman ' + str(nomor_halaman) + '</title>')
        html.append('    <style>')
        html.append('        body {')
        html.append('            font-family: Arial, sans-serif;')
        html.append('            margin: 20px;')
        html.append('            background-color: #f5f5f5;')
        html.append('        }')
        html.append('        h1, h2 {')
        html.append('            text-align: center;')
        html.append('            color: #333;')
        html.append('        }')
        html.append('        .container {')
        html.append('            max-width: 1800px;')
        html.append('            margin: 0 auto;')
        html.append('        }')
        html.append('        .section {')
        html.append('            background-color: white;')
        html.append('            border-radius: 8px;')
        html.append('            box-shadow: 0 2px 4px rgba(0,0,0,0.1);')
        html.append('            padding: 20px;')
        html.append('            margin-bottom: 30px;')
        html.append('        }')
        html.append('        .chart-container {')
        html.append('            overflow-x: auto;')
        html.append('        }')
        html.append('        .pagination {')
        html.append('            text-align: center;')
        html.append('            margin: 20px 0;')
        html.append('        }')
        html.append('        .pagination a {')
        html.append('            display: inline-block;')
        html.append('            padding: 8px 16px;')
        html.append('            text-decoration: none;')
        html.append('            color: black;')
        html.append('            background-color: #f1f1f1;')
        html.append('            border-radius: 5px;')
        html.append('            margin: 0 5px;')
        html.append('        }')
        html.append('        .pagination a.active {')
        html.append('            background-color: #4CAF50;')
        html.append('            color: white;')
        html.append('        }')
        html.append('        .pagination a:hover:not(.active) {')
        html.append('            background-color: #ddd;')
        html.append('        }')
        html.append('        .stats-container {')
        html.append('            display: flex;')
        html.append('            flex-wrap: wrap;')
        html.append('            justify-content: space-between;')
        html.append('            margin-bottom: 20px;')
        html.append('        }')
        html.append('        .stats-card {')
        html.append('            background-color: #f9f9f9;')
        html.append('            border-radius: 8px;')
        html.append('            box-shadow: 0 1px 3px rgba(0,0,0,0.1);')
        html.append('            padding: 15px;')
        html.append('            margin-bottom: 20px;')
        html.append('            width: 48%;')
        html.append('        }')
        html.append('        .stats-card h3 {')
        html.append('            margin-top: 0;')
        html.append('            color: #333;')
        html.append('            border-bottom: 1px solid #eee;')
        html.append('            padding-bottom: 8px;')
        html.append('        }')
        html.append('        table {')
        html.append('            width: 100%;')
        html.append('            border-collapse: collapse;')
        html.append('            margin: 20px 0;')
        html.append('        }')
        html.append('        th, td {')
        html.append('            border: 1px solid #ddd;')
        html.append('            padding: 12px;')
        html.append('            text-align: left;')
        html.append('        }')
        html.append('        th {')
        html.append('            background-color: #4CAF50;')
        html.append('            color: white;')
        html.append('        }')
        html.append('        tr:nth-child(even) {')
        html.append('            background-color: #f2f2f2;')
        html.append('        }')
        html.append('        tr:hover {')
        html.append('            background-color: #ddd;')
        html.append('        }')
        html.append('        @media print {')
        html.append('            body {')
        html.append('                background-color: white;')
        html.append('            }')
        html.append('            .section {')
        html.append('                box-shadow: none;')
        html.append('                margin-bottom: 20px;')
        html.append('                page-break-inside: avoid;')
        html.append('            }')
        html.append('            .stats-card {')
        html.append('                box-shadow: none;')
        html.append('                border: 1px solid #eee;')
        html.append('            }')
        html.append('            .pagination {')
        html.append('                display: none;')
        html.append('            }')
        html.append('        }')
        html.append('    </style>')
        html.append('</head>')
        html.append('<body>')
        html.append('    <div class="container">')
        html.append('        <h1>Dashboard Manajemen Data CPMK</h1>')
        
        # Navigasi halaman
        html.append('        <div class="pagination">')
        if nomor_halaman > 1:
            html.append(f'            <a href="histogram_cpmk_halaman{nomor_halaman-1}.html">&laquo; Sebelumnya</a>')
        
        for i in range(1, total_halaman + 1):
            if i == nomor_halaman:
                html.append(f'            <a class="active" href="histogram_cpmk_halaman{i}.html">{i}</a>')
            else:
                html.append(f'            <a href="histogram_cpmk_halaman{i}.html">{i}</a>')
        
        if nomor_halaman < total_halaman:
            html.append(f'            <a href="histogram_cpmk_halaman{nomor_halaman+1}.html">Selanjutnya &raquo;</a>')
        html.append('        </div>')
        
        # Bagian Visualisasi
        html.append('        <div class="section">')
        html.append('            <h2>Visualisasi</h2>')
        html.append('            <div class="chart-container">')
        html.append(f'                {konten_svg}')
        html.append('            </div>')
        html.append('        </div>')
        
        # Bagian Statistik
        html.append('        <div class="section">')
        html.append('            <h2>Ringkasan Statistik CPMK</h2>')
        html.append('            <div class="stats-container">')
        
        # Buat kartu untuk setiap CPMK
        for nama_cpmk, statistik in statistik_cpmk.items():
            html.append('                <div class="stats-card">')
            html.append(f'                    <h3>{nama_cpmk}</h3>')
            html.append('                    <p><strong>Nilai Rata-rata:</strong> ' + str(statistik["rata_rata"]) + '</p>')
            html.append('                    <p><strong>Nilai Tertinggi:</strong> ' + str(statistik["maksimum"]) + '</p>')
            html.append('                    <p><strong>Nilai Terendah:</strong> ' + str(statistik["minimum"]) + '</p>')
            html.append('                    <p><strong>Tingkat Kelulusan:</strong> ' + str(statistik["mahasiswa_lulus"]) + 
                          ' dari ' + str(statistik["total_mahasiswa"]) + ' (' + str(statistik["persentase_lulus"]) + '%)</p>')
            html.append('                </div>')
        
        html.append('            </div>')
        
        # Tabel ringkasan semua CPMK
        html.append('            <h2>Perbandingan Seluruh CPMK</h2>')
        html.append('            <table>')
        html.append('                <tr><th>CPMK</th><th>Rata-rata</th><th>Tertinggi</th><th>Terendah</th><th>Tingkat Kelulusan</th></tr>')
        
        for nama_cpmk, statistik in statistik_cpmk.items():
            html.append('                <tr>')
            html.append(f'                    <td>{nama_cpmk}</td>')
            html.append(f'                    <td>{statistik["rata_rata"]}</td>')
            html.append(f'                    <td>{statistik["maksimum"]}</td>')
            html.append(f'                    <td>{statistik["minimum"]}</td>')
            html.append(f'                    <td>{statistik["persentase_lulus"]}%</td>')
            html.append('                </tr>')
        
        html.append('            </table>')
        html.append('        </div>')
        
        html.append('    </div>')
        html.append('</body>')
        html.append('</html>')
        
        konten_html = '\n'.join(html)
        berkas_html.append((f"histogram_cpmk_halaman{nomor_halaman}.html", konten_html))
    
    # Buat index.html yang mengarahkan ke halaman pertama
    index_html = [
        '<!DOCTYPE html>',
        '<html lang="id">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta http-equiv="refresh" content="0;url=histogram_cpmk_halaman1.html">',
        '    <title>Mengarahkan...</title>',
        '</head>',
        '<body>',
        '    <p>Mengarahkan ke <a href="histogram_cpmk_halaman1.html">Dashboard Manajemen Data CPMK</a>...</p>',
        '</body>',
        '</html>'
    ]
    berkas_html.append(("index.html", '\n'.join(index_html)))
    
    return berkas_html

# Simpan semua berkas HTML
berkas_html = buat_html_dengan_manajemen_data()
for nama_berkas, konten in berkas_html:
    with open(nama_berkas, "w") as f:
        f.write(konten)

print(f"Berhasil membuat {len(berkas_html)} berkas HTML:")
for nama_berkas, _ in berkas_html:
    print(f"  - {nama_berkas}")
print("Buka 'index.html' di browser Anda untuk melihat Dashboard Manajemen Data CPMK.")