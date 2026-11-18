import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Container on AWS</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #0f172a; color: white; text-align: center; padding: 70px 20px; }}
            .container {{ background: #1e293b; max-width: 600px; margin: auto; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
            h1 {{ color: #38bdf8; }}
            p {{ color: #94a3b8; }}
            .badge {{ display: inline-block; padding: 6px 14px; background: #0ea5e9; color: white; border-radius: 20px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">Amazon ECR &bull; Docker Containerized</span>
            <h1>Flask Microservice in Docker</h1>
            <p>Successfully built with CodeBuild in Privileged Mode and pushed to Amazon ECR!</p>
            <p>Container Hostname: <code>{socket.gethostname()}</code></p>
            <p>Status: <strong>Running &bull; 200 OK</strong></p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="HEALTHY", container_id=socket.gethostname()), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
