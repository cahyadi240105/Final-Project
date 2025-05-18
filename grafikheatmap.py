headers = ["ID", "CPMK 012", "CPMK 031", "CPMK 071", "CPMK 072"]
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


def warna_kategori(n):
    try:
        n = float(n)
    except:
        return "#ffffff"
    if n >= 90:
        return "#1a5276"  # Dark blue
    elif n >= 80:
        return "#2980b9"  # Medium blue
    elif n >= 70:
        return "#5dade2"  # Light blue
    elif n >= 60:
        return "#f1c40f"  # Yellow
    else:
        return "#e74c3c"  # Red

def teks_terbaca(r, g, b):
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    return "black" if brightness > 125 else "white"

def buat_svg(data_slice, page_number):
    col_width = 120
    row_height = 36
    padding_x = 40
    padding_y = 80
    table_x_offset = 40
    heatmap_width = len(headers) * col_width
    heatmap_height = (len(data_slice) + 1) * row_height
    legend_x = table_x_offset + heatmap_width + 40
    legend_y = padding_y + 60
    svg_width = table_x_offset + heatmap_width + 300
    svg_height = heatmap_height + 120

    # Background rectangle for the entire SVG
    background = f'<rect width="100%" height="100%" fill="#f9f9f9" rx="10" ry="10"/>'
    
    # Title and subtitle
    title = f'<text x="{svg_width/2}" y="40" font-size="22" font-weight="bold" text-anchor="middle" fill="#2c3e50">Heatmap Nilai CPMK Mahasiswa</text>'
    subtitle = f'<text x="{svg_width/2}" y="65" font-size="14" text-anchor="middle" fill="#7f8c8d">Halaman {page_number} dari {len(pages)}</text>'
    
    # Table header with styling
    header_elements = []
    for j, h in enumerate(headers):
        x = table_x_offset + col_width * j
        y = padding_y
        header_elements.append(
            f'<rect x="{x}" y="{y}" width="{col_width}" height="{row_height}" fill="#34495e" rx="5" ry="5"/>'
        )
        header_elements.append(
            f'<text x="{x + col_width/2}" y="{y + row_height/2 + 5}" font-size="12" font-weight="bold" text-anchor="middle" fill="white">{h}</text>'
        )

    # Table cells with hover effects
    cell_elements = []
    for i, row in enumerate(data_slice):
        y = padding_y + row_height * (i + 1)
        for j, val in enumerate(row):
            x = table_x_offset + col_width * j
            fill = "#ffffff" if j == 0 else warna_kategori(val)
            r = int(fill[1:3], 16) if j > 0 else 255
            g = int(fill[3:5], 16) if j > 0 else 255
            b = int(fill[5:7], 16) if j > 0 else 255
            text_color = teks_terbaca(r, g, b)
            
            cell_id = f'cell-{page_number}-{i}-{j}'
            cell_elements.append(
                f'<rect id="{cell_id}" x="{x}" y="{y}" width="{col_width}" height="{row_height}" fill="{fill}" stroke="#ddd" rx="3" ry="3"/>'
            )
            cell_elements.append(
                f'<text x="{x + col_width/2}" y="{y + row_height/2 + 5}" text-anchor="middle" font-size="11" fill="{text_color}">{val}</text>'
            )
            
            # Add hover effect
            if j > 0:
                cell_elements.append(f'''
                    <style>
                        #{cell_id}:hover {{ filter: brightness(1.1); stroke: #2c3e50; stroke-width: 1.5; }}
                    </style>
                ''')

    # Simplified legend (only score ranges and colors)
    legend_title = f'<text x="{legend_x}" y="{legend_y - 20}" font-size="14" font-weight="bold" fill="#2c3e50">Kategori Nilai</text>'
    legend_data = [
        ("90 - 100", "#1a5276"),
        ("80 - 89", "#2980b9"),
        ("70 - 79", "#5dade2"),
        ("60 - 69", "#f1c40f"),
        ("0 - 59", "#e74c3c"),
    ]
    legend_elements = [legend_title]
    legend_box_size = 20
    for i, (label, color) in enumerate(legend_data):
        y = legend_y + i * (legend_box_size + 12)
        legend_elements.append(f'<rect x="{legend_x}" y="{y}" width="{legend_box_size}" height="{legend_box_size}" fill="{color}" stroke="#bdc3c7" rx="3" ry="3"/>')
        legend_elements.append(f'<text x="{legend_x + legend_box_size + 10}" y="{y + legend_box_size/2 + 5}" font-size="12" fill="#2c3e50">{label}</text>')

    # Combine all elements
    svg_elements = [
        background,
        title,
        subtitle,
        *header_elements,
        *cell_elements,
        *legend_elements,
    ]

    svg = f'''
    <svg width="{svg_width}" height="{svg_height}" style="margin-bottom:40px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px;">
        {''.join(svg_elements)}
    </svg>
    '''
    return svg

# Pagination
per_page = 12
pages = [data[i:i+per_page] for i in range(0, len(data), per_page)]

# HTML Output with improved styling
html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Heatmap CPMK - Visualisasi Interaktif</title>
  <style>
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f5f7fa;
      margin: 0;
      padding: 20px;
      color: #2c3e50;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
    }}
    header {{
      text-align: center;
      margin-bottom: 30px;
    }}
    h1 {{
      color: #2c3e50;
      margin-bottom: 5px;
    }}
    .subtitle {{
      color: #7f8c8d;
      margin-top: 0;
    }}
    .page {{
      display: none;
      background: white;
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 30px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }}
    .page.active {{
      display: block;
      animation: fadeIn 0.5s;
    }}
    .nav-container {{
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 20px 0;
    }}
    .nav-buttons button {{
      background-color: #3498db;
      color: white;
      border: none;
      padding: 10px 20px;
      margin: 0 10px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.3s;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }}
    .nav-buttons button:hover {{
      background-color: #2980b9;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    .nav-buttons button:disabled {{
      background-color: #bdc3c7;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
    }}
    .page-info {{
      margin: 0 20px;
      font-weight: bold;
      min-width: 100px;
      text-align: center;
    }}
    footer {{
      text-align: center;
      margin-top: 40px;
      color: #7f8c8d;
      font-size: 12px;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    .tooltip {{
      position: absolute;
      padding: 8px;
      background: rgba(0, 0, 0, 0.8);
      color: white;
      border-radius: 4px;
      font-size: 12px;
      pointer-events: none;
      z-index: 100;
      display: none;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Visualisasi Heatmap Nilai CPMK</h1>
      <p class="subtitle">Analisis performa mahasiswa berdasarkan capaian CPMK</p>
    </header>

    <div id="heatmap-container">
      {''.join(f'<div class="page" id="page-{i+1}">{buat_svg(p, i+1)}</div>' for i, p in enumerate(pages))}
    </div>

    <div class="nav-container">
      <div class="nav-buttons">
        <button onclick="prevPage()" id="prev-btn"><< Sebelumnya</button>
        <span class="page-info" id="page-info">Halaman 1 dari {len(pages)}</span>
        <button onclick="nextPage()" id="next-btn">Selanjutnya >></button>
      </div>
    </div>
  </div>

  <div class="tooltip" id="tooltip"></div>

  <script>
    let currentPage = 1;
    const totalPages = {len(pages)};

    function showPage(page) {{
      // Update buttons state
      document.getElementById("prev-btn").disabled = page <= 1;
      document.getElementById("next-btn").disabled = page >= totalPages;
      
      // Hide all pages and show current one
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.getElementById(`page-${{page}}`).classList.add('active');
      document.getElementById("page-info").textContent = `Halaman ${{page}} dari ${{totalPages}}`;
      
      // Smooth scroll to top
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function prevPage() {{
      if (currentPage > 1) {{
        currentPage--;
        showPage(currentPage);
      }}
    }}

    function nextPage() {{
      if (currentPage < totalPages) {{
        currentPage++;
        showPage(currentPage);
      }}
    }}

    // Initialize
    showPage(currentPage);

    // Add keyboard navigation
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowLeft') prevPage();
      if (e.key === 'ArrowRight') nextPage();
    }});

    // Tooltip functionality
    const tooltip = document.getElementById('tooltip');
    document.querySelectorAll('rect[id^="cell-"]').forEach(rect => {{
      rect.addEventListener('mouseover', (e) => {{
        const [_, page, row, col] = e.target.id.split('-');
        const headers = {headers};
        const data = {data};
        const rowData = data[(page-1)*{per_page}+parseInt(row)];
        
        if (col > 0) {{
          const header = headers[col];
          const value = rowData[col];
          const studentId = rowData[0];
          
          tooltip.style.display = 'block';
          tooltip.innerHTML = `
            <div><strong>Mahasiswa:</strong> ${{studentId}}</div>
            <div><strong>CPMK:</strong> ${{header}}</div>
            <div><strong>Nilai:</strong> ${{value}}</div>
          `;
          
          // Position tooltip near cursor
          tooltip.style.left = `${{e.pageX + 10}}px`;
          tooltip.style.top = `${{e.pageY + 10}}px`;
        }}
      }});
      
      rect.addEventListener('mouseout', () => {{
        tooltip.style.display = 'none';
      }});
    }});
  </script>
</body>
</html>
'''

with open("heatmap_graph.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ File 'heatmap_graph.html' berhasil dibuat dengan legenda yang disederhanakan!")