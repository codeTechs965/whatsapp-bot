from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "YOUR_ACCESS_TOKEN"
PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    msg = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
    sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

    reply = "Hello! 👋 I am your WhatsApp agent."

    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": sender,
        "text": {"body": reply}
    }

    requests.post(url, json=payload, headers=headers)
    return "ok", 200

app.run(port=5000)
