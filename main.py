from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Tüm istemcilere açık

@app.route("/stok-kontrol", methods=["GET"])
def kontrol():
    try:
        url = request.args.get("url")
        if not url:
            return jsonify({"error": "URL parametresi eksik"}), 400
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
