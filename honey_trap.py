import requests
import random
import string
from http.server import SimpleHTTPRequestHandler, HTTPServer

# --- CONFIGURATION ---
# Replace with your actual Discord Webhook URL for local use. 
# Keep as a placeholder for GitHub uploads.
# you customize the html how you need

WEBHOOK = "your webhook link" 
PORT = 8080 

def generate_obfuscation_metadata(lines=500):
    """Generates random comment blocks to bloat the HTML source code."""
    categories = ["DATABASE_REF", "INTERNAL_SESSION", "ENCRYPTED_KEY", "LOCAL_ROOT"]
    metadata = ""
    for _ in range(lines):
        cat = random.choice(categories)
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=42))
        metadata += f"/* {cat}: {token} */\n"
    return metadata

def build_deployment_frontend():
    """Generates a professional-looking DevLog index.html file."""
    obfuscated_data = generate_obfuscation_metadata()
    
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevLog | Technical Research & Labs</title>
    <style>
        :root {{ --primary: #00d2ff; --bg: #0f172a; --card: #1e293b; --text: #f8fafc; --accent: #ef4444; --success: #4ade80; }}
        body {{ background-color: var(--bg); color: var(--text); font-family: sans-serif; margin: 0; display: flex; flex-direction: column; min-height: 100vh; }}
        header {{ background: rgba(30, 41, 59, 0.9); padding: 30px 20px; text-align: center; border-bottom: 1px solid #334155; }}
        h1 {{ margin: 0; font-size: 2rem; color: var(--primary); }}
        .layout {{ display: grid; grid-template-columns: 1fr 300px; gap: 30px; max-width: 1100px; margin: 40px auto; padding: 0 20px; }}
        .card {{ background: var(--card); border: 1px solid #334155; padding: 25px; border-radius: 12px; margin-bottom: 25px; }}
        .card h2 {{ color: var(--primary); margin-top: 0; }}
        .sidebar {{ background: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 12px; border: 1px solid #334155; height: fit-content; }}
        .vault {{ background: #020617; border: 1px dashed var(--accent); padding: 15px; border-radius: 8px; margin-top: 20px; }}
        .status-dot {{ display: inline-block; width: 8px; height: 8px; background: var(--accent); border-radius: 50%; margin-right: 8px; }}
    </style>
</head>
<body>
    <header>
        <h1>Digital DevLog</h1>
        <div style="font-size: 0.8rem; color: #64748b; margin-top: 5px;">Systems Engineering | Security Research</div>
    </header>
    <div class="layout">
        <div class="content">
            <div class="card">
                <h2>Laboratory Update: Hardware Migration</h2>
                <p>Transitioning primary lab workloads to a high-performance workstation environment. Optimizing SSD arrays and secondary storage health monitoring.</p>
            </div>
            <div class="card">
                <h2>Technical Analysis: Network Traffic Patterns</h2>
                <p>Observing data-driven shifts in midfield transitions within modern sports analytics. The correlation between positioning and network flow is a significant area of study.</p>
            </div>
            <div class="card">
                <h2>Active Research</h2>
                <p>Currently reviewing Sandworm by Andy Greenberg and preparing for upcoming certification exams.</p>
                <div class="vault">
                    <div style="color: var(--accent); font-weight: bold; font-family: monospace; font-size: 0.8rem;">
                        <span class="status-dot"></span>[ ENCRYPTED_DATA_VAULT_01 ]
                    </div>
                    <div style="font-family: monospace; color: var(--success); font-size: 0.8rem; margin-top: 10px;">
                        >> INITIALIZING DECRYPTION...<br>
                        >> [ ACCESS GRANTED ]
                    </div>
                </div>
            </div>
        </div>
        <div class="sidebar">
            <h3>Statistics</h3>
            <ul>
                <li>Status: Active</li>
                <li>Location: Regional</li>
            </ul>
        </div>
    </div>
    <script>
        /* INTERNAL_METADATA_OVERRIDE: {obfuscated_data} */
    </script>
</body>
</html>
"""
    with open("index.html", "w") as f:
        f.write(html_template)
    print("Frontend deployment file generated.")

class SentinelHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """Monitors traffic and dispatches forensic alerts to Discord."""
        # Extract Real IP from Cloudflare or Proxy headers
        origin_ip = self.headers.get('CF-Connecting-IP')
        if not origin_ip:
            origin_ip = self.headers.get('X-Forwarded-For', self.client_address[0])
        
        origin_ip = origin_ip.split(',')[0].strip()
        user_agent = self.headers.get('User-Agent', 'Unknown Environment')
        
        # Filter favicon requests to avoid alert fatigue
        if "favicon" not in self.path:
            print(f"Log: Connection detected from {origin_ip}")
            
            alert_data = {
                "username": "Warning! Honey trap",
                "embeds": [{
                    "title": "Connection Detected",
                    "color": 15158332,
                    "description": f"**Origin IP:** `{origin_ip}`\\n**Environment:** {user_agent}",
                    "fields": [{"name": "Analysis", "value": f"https://ipinfo.io/{origin_ip}"}]
                }]
            }
            try:
                requests.post(WEBHOOK, json=alert_data, timeout=5)
                print("Alert dispatched to Discord.")
            except Exception as error:
                print(f"Dispatch Error: {error}")

        return super().do_GET()

if __name__ == "__main__":
    build_deployment_frontend()
    print(f"The Honey trap  active on Port {PORT}. Monitoring traffic...")
    server = HTTPServer(('0.0.0.0', PORT), SentinelHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nThe Honey trap  deactivated.")
