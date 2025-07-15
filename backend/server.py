from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/approve", methods=["POST"])
def approve():
    data = request.get_json()
    print("✅ [APPROVE] PaymentId:", data.get("paymentId"))
    return jsonify({"success": True})

@app.route("/complete", methods=["POST"])
def complete():
    data = request.get_json()
    print("✅ [COMPLETE] PaymentId:", data.get("paymentId"), "TxID:", data.get("txid"))
    return jsonify({"success": True})

@app.route("/")
def home():
    return "✅ Backend i GlobalLottoPI është aktiv!"

import os

port = int(os.environ.get("PORT", 10000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
