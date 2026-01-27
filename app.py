from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "EAATq4RblNQoBQlPsfpabIOicgcg1ClgqTmsZBMW3YNDi3WRqgRMkSilNZBuZCeUES7r8koJGVfW3BPcCzPxu3vYvRvizkFSY5iHwQY0681Hl6ZCAnLl61QrV4iqp5SmPRpeBKhgZCrlvyv8Xh617NSH10G6BIo6BDqpSwwif8EZBdfPen4gfQMusDwrH8nEb53vB5q4OK4ugVENOUgepWulojEnfu6R2Fj8sfdaZCTVK8NFLmrxEUZA7BP38bTnbmMWwUdLez6cE93biXwfSboOA"
PHONE_NUMBER_ID = "03206010205"

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
