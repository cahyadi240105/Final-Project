# === Data Mahasiswa ===
data = [
    ["2101020014", 100, 90, 82, 80],
    ["2101020024", 100, 20, 66, 71],
    ["2101020048", 100, 90, 89, 73],
    ["2101020058", 100, 90, 83, 80],
    ["2101020074", 90, 60, 73, 64],
    ["2101020092", 100, 20, 71, 56],
    ["2101020103", 0, 0, 7.1, 15],
    ["2101020104", 90, 60, 64, 64],
    ["2101020117", 90, 60, 71, 64],
    ["2201020001", 100, 60, 76, 58],
    ["2201020002", 100, 80, 84, 71],
    ["2201020010", 100, 80, 94, 82],
    ["2201020014", 100, 60, 83, 65],
    ["2201020015", 100, 60, 80, 58],
    ["2201020018", 100, 70, 86, 80],
    ["2201020019", 100, 80, 93, 75],
    ["2201020022", 90, 20, 75, 45],
    ["2201020026", 100, 80, 84, 71],
    ["2201020032", 100, 80, 85, 67],
    ["2201020039", 100, 80, 82, 56],
    ["2201020041", 100, 80, 93, 75],
    ["2201020047", 100, 75, 64, 45],
    ["2201020048", 100, 70, 99, 80],
    ["2201020057", 100, 75, 72, 45],
    ["2201020063", 100, 76, 94, 80],
    ["2201020065", 100, 75, 89, 75],
    ["2201020066", 100, 60, 72, 53],
    ["2201020067", 100, 80, 92, 67],
    ["2201020070", 100, 75, 94, 84],
    ["2201020074", 100, 60, 62, 53],
    ["2201020075", 100, 80, 92, 75],
    ["2201020083", 100, 80, 88, 75],
    ["2201020086", 0, 0, 7.1, 0],
    ["2201020090", 100, 75, 97, 80],
    ["2201020091", 100, 80, 87, 75],
    ["2201020092", 100, 60, 76, 53],
    ["2201020093", 100, 75, 86, 72],
    ["2201020094", 100, 80, 92, 67],
    ["2201020095", 100, 75, 87, 72],
    ["2201020098", 100, 75, 69, 60],
    ["2201020099", 100, 80, 93, 82],
    ["2201020100", 100, 80, 86, 64],
    ["2201020103", 100, 70, 101, 80],
    ["2201020104", 100, 80, 86, 64],
    ["2201020105", 100, 70, 76, 60],
    ["2201020106", 90, 50, 67, 47],
    ["2201020109", 100, 80, 86, 64],
    ["2201020112", 90, 50, 69, 47],
    ["2201020116", 90, 50, 66, 40],
    ["2201020117", 100, 70, 73, 53],
    ["2201020118", 100, 80, 92, 82],
    ["2201020122", 100, 70, 71, 53],
    ["2201020123", 90, 20, 70, 53]
]


# === Visual Constants ===
CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 700
PADDING = 60
POINT_RADIUS = 4
COLORS = ["red", "blue", "green", "purple"]
CATEGORIES = ["CPMK012", "CPMK031", "CPMK071", "CPMK072"]

# --- Pagination Constants ---
page_size = 10  # Set jumlah data per halaman
total_pages = len(data) // page_size + (1 if len(data) % page_size > 0 else 0)

# --- Fungsi untuk analisis data ---
def analyze_data():
    # Hitung rata-rata untuk setiap CPMK
    avg_cpmk = [0, 0, 0, 0]
    count_students = len(data)
    
    # Mahasiswa dengan nilai tertinggi dan terendah di setiap CPMK
    max_cpmk = [0, 0, 0, 0]
    min_cpmk = [100, 100, 100, 100]
    max_ids = ["", "", "", ""]
    min_ids = ["", "", "", ""]
    
    # Jumlah mahasiswa mencapai nilai di atas rata-rata
    above_avg_count = [0, 0, 0, 0]
    
    for row in data:
        for i in range(4):
            value = row[i+1]
            avg_cpmk[i] += value
            
            # Update max
            if value > max_cpmk[i]:
                max_cpmk[i] = value
                max_ids[i] = row[0]
            
            # Update min (hanya jika bukan 0, untuk menghindari mahasiswa yang tidak mengikuti)
            if 0 < value < min_cpmk[i]:
                min_cpmk[i] = value
                min_ids[i] = row[0]
    
    # Hitung rata-rata
    for i in range(4):
        avg_cpmk[i] = avg_cpmk[i] / count_students if count_students > 0 else 0
    
    # Hitung jumlah mahasiswa di atas rata-rata
    for row in data:
        for i in range(4):
            if row[i+1] > avg_cpmk[i]:
                above_avg_count[i] += 1
    
    # Kategori pencapaian
    cpmk_status = []
    for i in range(4):
        if avg_cpmk[i] >= 80:
            status = "Sangat Baik"
        elif avg_cpmk[i] >= 70:
            status = "Baik"
        elif avg_cpmk[i] >= 60:
            status = "Cukup"
        else:
            status = "Perlu Perbaikan"
        cpmk_status.append(status)
    
    return {
        "averages": avg_cpmk,
        "max_values": max_cpmk,
        "min_values": min_cpmk,
        "max_ids": max_ids,
        "min_ids": min_ids,
        "above_avg": above_avg_count,
        "total_students": count_students,
        "cpmk_status": cpmk_status
    }

# Analisis data
analysis_results = analyze_data()

# --- Fungsi untuk Generate Data Plot ---
def generate_svg(page_number):
    start = page_number * page_size
    end = min((page_number + 1) * page_size, len(data))
    page_data = data[start:end]
    
    # Hitung nilai min dan max untuk Y axis
    all_values = [val for row in page_data for val in row[1:]]
    max_y = max(all_values) if all_values else 100
    min_y = min(all_values) if all_values else 0
    
    # Jika min_y == max_y, set min_y = 0 untuk menghindari pembagian dengan nol
    if min_y == max_y:
        min_y = 0
    
    svg_elements = []

    # Axis Y
    svg_elements.append(f"<line x1='{PADDING}' y1='{PADDING}' x2='{PADDING}' y2='{CANVAS_HEIGHT - PADDING}' stroke='black' stroke-width='2' />")

    # Axis X
    svg_elements.append(f"<line x1='{PADDING}' y1='{CANVAS_HEIGHT - PADDING}' x2='{CANVAS_WIDTH - PADDING}' y2='{CANVAS_HEIGHT - PADDING}' stroke='black' stroke-width='2' />")

    # Label Y Axis
    for i in range(6):
        y_val = min_y + i * (max_y - min_y) / 5
        y_pos = CANVAS_HEIGHT - PADDING - i * (CANVAS_HEIGHT - 2 * PADDING) / 5
        svg_elements.append(f"<text x='{PADDING - 10}' y='{y_pos}' font-size='12' text-anchor='end'>{round(y_val, 1)}</text>")

    # Grid lines (horizontal)
    for i in range(1, 6):
        y_pos = CANVAS_HEIGHT - PADDING - i * (CANVAS_HEIGHT - 2 * PADDING) / 5
        svg_elements.append(f"<line x1='{PADDING}' y1='{y_pos}' x2='{CANVAS_WIDTH - PADDING}' y2='{y_pos}' stroke='#e0e0e0' stroke-width='1' stroke-dasharray='5,5' />")

    # Data points with interactive elements
    x_gap = (CANVAS_WIDTH - 2 * PADDING - 40) / (len(page_data) if len(page_data) > 0 else 1)
    
    # Define offsets for CPMK points to prevent overlapping
    cpmk_offsets = [-6, -2, 2, 6]  # Horizontal offsets in pixels for each CPMK
    
    for i, row in enumerate(page_data):
        student_id = row[0]
        x = PADDING + 20 + i * x_gap
        
        # Create clickable student ID
        svg_elements.append(f"""<text x='{x}' y='{CANVAS_HEIGHT - PADDING + 30}' 
                            transform='rotate(0 {x},{CANVAS_HEIGHT - PADDING + 30})' 
                            font-size='10' class='student-id' 
                            onclick='showStudentDetail("{student_id}", {row[1]}, {row[2]}, {row[3]}, {row[4]}, {x}, {CANVAS_HEIGHT - PADDING + 30})'
                            >{student_id}</text>""")
        
        # Draw data points with offset to prevent overlapping
        for j, value in enumerate(row[1:]):
            if max_y > min_y:  # Hindari pembagian dengan nol
                y_norm = (value - min_y) / (max_y - min_y)
                y = CANVAS_HEIGHT - PADDING - y_norm * (CANVAS_HEIGHT - 2 * PADDING)
                # Apply horizontal offset based on CPMK index
                x_offset = x + cpmk_offsets[j]
                svg_elements.append(f"<circle cx='{x_offset}' cy='{y}' r='{POINT_RADIUS}' fill='{COLORS[j]}' />")

    # Judul dan Label
    svg_elements.append(f"<text x='{CANVAS_WIDTH/2}' y='30' text-anchor='middle' font-size='16' font-weight='bold'>Pencapaian Nilai CPMK Mahasiswa</text>")
    svg_elements.append(f"<text x='{CANVAS_WIDTH/2}' y='{CANVAS_HEIGHT - 10}' text-anchor='middle' font-size='12'>ID Mahasiswa (klik untuk detail)</text>")
    svg_elements.append(f"<text x='20' y='{CANVAS_HEIGHT/2}' text-anchor='middle' font-size='12' transform='rotate(-90,20,{CANVAS_HEIGHT/2})'>Rentang Nilai</text>")

    # Legend
    legend_x = CANVAS_WIDTH - 150
    legend_y = 60
    for i, cat in enumerate(CATEGORIES):
        y = legend_y + i * 25
        svg_elements.append(f"<rect x='{legend_x}' y='{y}' width='15' height='15' fill='{COLORS[i]}' />")
        svg_elements.append(f"<text x='{legend_x + 20}' y='{y + 12}' font-size='12'>{cat}</text>")

    # Pagination Info
    svg_elements.append(f"<text x='{PADDING}' y='{PADDING - 20}' font-size='12'>Halaman {page_number + 1} dari {total_pages}</text>")

    # Gabungkan semua ke dalam SVG
    svg_content = ''.join(svg_elements)
    return svg_content

# --- Generate SVG untuk semua halaman ---
all_svgs = []
for i in range(total_pages):
    all_svgs.append(generate_svg(i))


# --- Format Kesimpulan ---
conclusion_html = f"""
<div class="conclusion">
    <h2>Kesimpulan Analisis Data</h2>
    
    <div class="summary">
        <h3>Rata-rata Pencapaian CPMK</h3>
        <table class="data-table">
            <tr>
                <th>CPMK</th>
                <th>Rata-rata</th>
                <th>Status</th>
                <th>Mahasiswa di Atas Rata-rata</th>
            </tr>
            <tr>
                <td>CPMK012</td>
                <td>{analysis_results['averages'][0]:.2f}</td>
                <td>{analysis_results['cpmk_status'][0]}</td>
                <td>{analysis_results['above_avg'][0]} ({(analysis_results['above_avg'][0]/analysis_results['total_students']*100):.1f}%)</td>
            </tr>
            <tr>
                <td>CPMK031</td>
                <td>{analysis_results['averages'][1]:.2f}</td>
                <td>{analysis_results['cpmk_status'][1]}</td>
                <td>{analysis_results['above_avg'][1]} ({(analysis_results['above_avg'][1]/analysis_results['total_students']*100):.1f}%)</td>
            </tr>
            <tr>
                <td>CPMK071</td>
                <td>{analysis_results['averages'][2]:.2f}</td>
                <td>{analysis_results['cpmk_status'][2]}</td>
                <td>{analysis_results['above_avg'][2]} ({(analysis_results['above_avg'][2]/analysis_results['total_students']*100):.1f}%)</td>
            </tr>
            <tr>
                <td>CPMK072</td>
                <td>{analysis_results['averages'][3]:.2f}</td>
                <td>{analysis_results['cpmk_status'][3]}</td>
                <td>{analysis_results['above_avg'][3]} ({(analysis_results['above_avg'][3]/analysis_results['total_students']*100):.1f}%)</td>
            </tr>
        </table>
    </div>
    
    <div class="highlight">
        <h3>Pencapaian Tertinggi dan Terendah</h3>
        <table class="data-table">
            <tr>
                <th>CPMK</th>
                <th>Nilai Tertinggi</th>
            </tr>
            <tr>
                <td>CPMK012</td>
                <td>{analysis_results['max_values'][0]}</td>
            </tr>
            <tr>
                <td>CPMK031</td>
                <td>{analysis_results['max_values'][1]}</td>
            </tr>
            <tr>
                <td>CPMK071</td>
                <td>{analysis_results['max_values'][2]}</td>
           </tr>
            <tr>
                <td>CPMK072</td>
                <td>{analysis_results['max_values'][3]}</td>
            </tr>
        </table>
    </div>
    
    <div class="recommendations">
        <h3>Rekomendasi Pengembangan</h3>
        <ul>
            <li>CPMK031 memiliki nilai rata-rata {analysis_results['averages'][1]:.2f} yang {analysis_results['cpmk_status'][1].lower()}. Perlu adanya perhatian khusus untuk peningkatan pencapaian pada CPMK ini.</li>
            <li>Terdapat {analysis_results['total_students'] - analysis_results['above_avg'][0]} mahasiswa yang berada di bawah rata-rata pada CPMK012 (nilai di bawah {analysis_results['averages'][0]:.2f}).</li>
            <li>Pada CPMK071 dan CPMK072, sekitar {(analysis_results['above_avg'][2]/analysis_results['total_students']*100):.1f}% mahasiswa telah mencapai nilai di atas rata-rata.</li>
        </ul>
    </div>
</div>
"""

# --- Fungsi untuk Menghasilkan HTML ---
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Scatterplot CPMK Mahasiswa with Details</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f5f5f5;
        }}
        h1, h2, h3 {{ 
            color: #333;
            text-align: center; 
        }}
        .container {{
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .button {{ 
            font-size: 14px; 
            padding: 10px 20px; 
            cursor: pointer; 
            margin: 0 5px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
        }}
        .button:disabled {{ 
            background-color: #ccc; 
        }}
        .controls {{ 
            margin: 20px 0; 
            display: flex; 
            align-items: center;
            justify-content: center;
        }}
        .page-info {{ 
            margin-right: 15px; 
            font-weight: bold;
        }}
        .chart-container {{
            display: flex;
            justify-content: center;
            margin: 20px 0;
            position: relative;
        }}
        .conclusion {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            border-left: 5px solid #4CAF50;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        .data-table th, .data-table td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }}
        .data-table th {{
            background-color: #f2f2f2;
        }}
        .data-table tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .summary, .highlight, .recommendations {{
            margin-top: 20px;
        }}
        .recommendations ul {{
            text-align: left;
        }}
        .student-detail {{
            position: absolute;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            z-index: 100;
            display: none;
        }}
        .student-detail table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .student-detail th, .student-detail td {{
            border: 1px solid #ddd;
            padding: 5px;
            text-align: center;
        }}
        .student-detail th {{
            background-color: #f2f2f2;
        }}
        .student-id {{
            cursor: pointer;
            text-decoration: underline;
            fill: blue;
        }}
        .close-btn {{
            position: absolute;
            top: 5px;
            right: 5px;
            cursor: pointer;
            font-size: 16px;
            color: #777;
        }}
        .close-btn:hover {{
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Grafik Pencapaian Nilai CPMK Mahasiswa</h1>
        
        <div class="controls">
            <span id="pageInfo" class="page-info">Halaman 1 dari {total_pages}</span>
            <button id="prevBtn" class="button" onclick="changePage(-1)">Previous</button>
            <button id="nextBtn" class="button" onclick="changePage(1)">Next</button>
        </div>
        
        <div class="chart-container">
            <svg id="chart" width="1100" height="700" style="border:1px solid #ccc; box-shadow: 0 0 5px rgba(0,0,0,0.1);">
                {all_svgs[0]}
            </svg>
            <div id="studentDetail" class="student-detail">
                <span class="close-btn" onclick="hideStudentDetail()">×</span>
                <h3 id="studentIdTitle">Detail Mahasiswa</h3>
                <table>
                    <tr>
                        <th>CPMK</th>
                        <th>Nilai</th>
                        <th>Status</th>
                    </tr>
                    <tr id="cpmk012Row">
                        <td>CPMK012</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr id="cpmk031Row">
                        <td>CPMK031</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr id="cpmk071Row">
                        <td>CPMK071</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr id="cpmk072Row">
                        <td>CPMK072</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                </table>
                <p id="studentAvg"></p>
            </div>
        </div>
        
        {conclusion_html}
    </div>
    
    <script>
        // Data SVG untuk semua halaman dalam bentuk array JavaScript
        const allSvgs = [
            {','.join([f'`{svg}`' for svg in all_svgs])}
        ];
        
        // Data mahasiswa
        const studentData = {str(data).replace("'", '"')};
        
        let currentPage = 0;
        const totalPages = {total_pages};
        const svgElement = document.getElementById('chart');
        const pageInfoElement = document.getElementById('pageInfo');
        const studentDetailElement = document.getElementById('studentDetail');

        function changePage(direction) {{
            currentPage += direction;
            if (currentPage < 0) currentPage = 0;
            if (currentPage >= totalPages) currentPage = totalPages - 1;
            
            // Perbarui SVG dengan konten halaman yang sesuai
            svgElement.innerHTML = allSvgs[currentPage];
            
            // Sembunyikan detail mahasiswa saat pindah halaman
            hideStudentDetail();
            
            // Perbarui status dan info halaman
            updateButtonState();
            pageInfoElement.textContent = `Halaman ${{currentPage + 1}} dari ${{totalPages}}`;
        }}

        function updateButtonState() {{
            document.getElementById('prevBtn').disabled = currentPage === 0;
            document.getElementById('nextBtn').disabled = currentPage === totalPages - 1;
        }}

        function getStatusFromValue(value) {{
            if (value >= 80) return "Sangat Baik";
            if (value >= 70) return "Baik";
            if (value >= 60) return "Cukup";
            if (value > 0) return "Perlu Perbaikan";
            return "Tidak Mengikuti";
        }}

        function getStatusColor(status) {{
            switch(status) {{
                case "Sangat Baik": return "#4CAF50";
                case "Baik": return "#2196F3";
                case "Cukup": return "#FF9800";
                case "Perlu Perbaikan": return "#F44336";
                default: return "#9E9E9E";
            }}
        }}

        function showStudentDetail(studentId, cpmk012, cpmk031, cpmk071, cpmk072, x, y) {{
            // Set judul
            document.getElementById('studentIdTitle').textContent = `Detail Mahasiswa: ${{studentId}}`;
            
            // Set nilai CPMK
            const cpmkValues = [cpmk012, cpmk031, cpmk071, cpmk072];
            const cpmkRows = ['cpmk012Row', 'cpmk031Row', 'cpmk071Row', 'cpmk072Row'];
            
            for (let i = 0; i < 4; i++) {{
                const row = document.getElementById(cpmkRows[i]);
                const cells = row.getElementsByTagName('td');
                const value = cpmkValues[i];
                const status = getStatusFromValue(value);
                
                cells[1].textContent = value;
                cells[2].textContent = status;
                cells[2].style.color = getStatusColor(status);
            }}
            
            // Hitung rata-rata
            const validValues = cpmkValues.filter(val => val > 0);
            const avg = validValues.length > 0 ? 
                validValues.reduce((sum, val) => sum + val, 0) / validValues.length : 0;
            
            document.getElementById('studentAvg').textContent = 
                `Rata-rata: ${{avg.toFixed(2)}} (${{getStatusFromValue(avg)}})`;
            
            // Posisikan dan tampilkan detail
            const detailElement = document.getElementById('studentDetail');
            
            // Posisikan di dekat ID mahasiswa
            const chartRect = svgElement.getBoundingClientRect();
            const containerRect = document.querySelector('.chart-container').getBoundingClientRect();
            
            const leftPosition = x - detailElement.offsetWidth / 2;
            const topPosition = y - detailElement.offsetHeight - 10;
            
            detailElement.style.left = `${{Math.max(0, Math.min(chartRect.width - detailElement.offsetWidth, leftPosition))}}px`;
            detailElement.style.top = `${{Math.max(0, topPosition)}}px`;
            detailElement.style.display = 'block';
        }}

        function hideStudentDetail() {{
            document.getElementById('studentDetail').style.display = 'none';
        }}

        // Initial button state
        updateButtonState();
        
        // Close detail when clicking outside
        document.addEventListener('click', function(event) {{
            if (!event.target.closest('#studentDetail') && 
                !event.target.classList.contains('student-id')) {{
                hideStudentDetail();
            }}
        }});
    </script>
</body>
</html>
"""

# Simpan hasil ke file
with open("scatterplot.html", "w", encoding="utf-8") as f:
    f.write(html_content)


print("Berhasil membuat halaman HTML dengan detail data mahasiswa: scatterplot.html")