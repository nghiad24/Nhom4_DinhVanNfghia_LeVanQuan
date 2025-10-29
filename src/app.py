# Tạo web hiển thị các biểu đồ
# src chính: "https://unjudged-hydrocinnamyl-vilma.ngrok-free.dev/"
import nbformat
from nbconvert import HTMLExporter
from flask import Flask, render_template_string
from pyngrok import ngrok
import os


NOTEBOOK_PATH = "/content/drive/MyDrive/Bao_cao_KPDL/Roosman_sales_charts_only.ipynb"


with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)


html_exporter = HTMLExporter()
html_exporter.template_name = 'classic'
(body, resources) = html_exporter.from_notebook_node(notebook)


app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>📊 Roosman Sales Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body { background-color: #f8f9fa; font-family: Verdana, sans-serif; }
        .container { margin-top: 40px; }
        iframe, .output_png { border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h1, h2, h3 { color: #ff6600; }
    </style>
</head>
<body>
<div class="container">
    <h1 class="text-center mb-4">📈 Roosman Sales Dashboard</h1>
    <div class="card p-4 shadow-sm">
        {{ body|safe }}
    </div>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, body=body)

if __name__ == "__main__":
    port = 9090
    NGROK_AUTH_TOKEN = "34jIPulFT5p4J2uHhnGINhXiWdJ_3UvtWKu8xMhz1kbMVkFQM"

    ngrok.set_auth_token(NGROK_AUTH_TOKEN)


    public_url = ngrok.connect(port)
    print(f"🌍 Public URL: {public_url}")


    app.run(host="0.0.0.0", port=port, debug=False)
