import os
from flask import Flask, jsonify

application = Flask(__name__)

APP_ENV = os.environ.get("APP_ENV", "production")
APP_VERSION = os.environ.get("APP_VERSION", "1.0")

@application.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Elastic Beanstalk CI/CD</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #eef2f7; text-align: center; padding: 70px 20px; }}
            .container {{ background: white; max-width: 600px; margin: auto; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a73e8; }}
            p {{ color: #555; }}
            .badge {{ display: inline-block; padding: 5px 12px; background: #28a745; color: white; border-radius: 20px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AWS Elastic Beanstalk Deployment</h1>
            <p class="badge">Health: OK</p>
            <p>Successfully deployed via AWS CodePipeline!</p>
            <p>Environment: <strong>{APP_ENV}</strong></p>
            <p>Deployment Version: <strong>{APP_VERSION}</strong></p>
        </div>
    </body>
    </html>
    """

@application.route("/health")
def health():
    return jsonify(status="UP", environment=APP_ENV, version=APP_VERSION), 200

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
