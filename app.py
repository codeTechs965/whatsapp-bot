import streamlit as st
from flask import Flask, request
import requests
import threading

TOKEN = "PASTE_YOUR_TOKEN"
PHONE_NUMBER_ID = "PASTE_PHONE_NUMBER_ID"

flask_app = Flask(__name__)

@flask_app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
    except:
        return "ok", 200

    reply = "Hello 👋 I am your Streamlit WhatsApp agent!"

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

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask).start()

st.title("✅ WhatsApp Bot Running")
st.write("Your WhatsApp agent is live!")
