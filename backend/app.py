from flask import Flask, jsonify
from config import API_URL, MAPS_API_KEY
import json
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "destinations.json"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/destinations")
def destinations():
    with open(DATA_FILE, encoding="utf-8") as handle:
        data = json.load(handle)
    return jsonify(data)

@app.get("/api/config")
def config():
    return jsonify({
        "api_url": API_URL,
        "maps_enabled": bool(MAPS_API_KEY)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
