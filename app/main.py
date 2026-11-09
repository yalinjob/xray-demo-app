"""Small Flask service that exercises each pinned dependency.

The application code itself is safe; the vulnerabilities live only in the
outdated third-party packages listed in requirements.txt.
"""
import os
from importlib.metadata import version as flask_version

import certifi
import requests
from cryptography.fernet import Fernet
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
FERNET = Fernet(Fernet.generate_key())

PAGE = "<h1>{{ title }}</h1><p>Demo app for JFrog Xray. Version {{ version }}.</p>"


@app.get("/")
def index():
    return render_template_string(PAGE, title="Xray Demo App", version=os.getenv("APP_VERSION", "dev"))


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/versions")
def versions():
    return jsonify(
        requests=requests.__version__,
        certifi=certifi.__version__,
        flask=flask_version("flask"),
    )


@app.get("/encrypt/<text>")
def encrypt(text):
    token = FERNET.encrypt(text.encode()).decode()
    return jsonify(token=token, roundtrip=FERNET.decrypt(token.encode()).decode())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
