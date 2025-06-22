import subprocess
from datetime import datetime

scripts = ["script1.py", "script2.py", "script3.py", "script4.py"]

html_lines = []
html_lines.append("<html><head><title>Execution Report</title>")
html_lines.append("<style>")
html_lines.append("""
  body { font-family: Arial, sans-serif; }
  .success { color: green; }
  .failure { color: red; }
  .log-box { background: #f9f9f9; border: 1px solid #ddd; padding: 10px; margin: 10px 0; white-space: pre-wrap; }
""")
html_lines.append("</style></head><body>")
html_lines.append(f"<h2>🗓️ Execution Report</h2>")
html_lines.append(f"<p><strong>Start Time:</strong> {datetime.utcnow()} UTC</p>")

for script in scripts:
    html_lines.append(f"<h3>▶️ Running: {script}</h3>")
    try:
        result = subprocess.run(
            ["python", script],
            text=True,
            capture_output=True,
            check=True
        )
        html_lines.append(f"<p class='success'>✅ {script} succeeded</p>")
        html_lines.append(f"<div class='log-box'>{result.stdout}</div>")
    except subprocess.CalledProcessError as e:
        html_lines.append(f"<p class='failure'>❌ {script} failed</p>")
        html_lines.append(f"<div class='log-box'><strong>STDOUT:</strong><br>{e.stdout}<br><strong>STDERR:</strong><br>{e.stderr}</div>")

html_lines.append(f"<p><strong>End Time:</strong> {datetime.utcnow()} UTC</p>")
html_lines.append("</body></html>")

with open("final_report.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines))
