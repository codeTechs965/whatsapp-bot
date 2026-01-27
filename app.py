from flask import Flask, request
import requests
import os
app = Flask(__name__)

# VERIFY_TOKEN = "mywhatsappbot123"
# TOKEN = "EAATq4RblNQoBQkmU6IAsyDdt6wI8Q7i8rR5prP96Mmbr18HEYRuIfMqK2yUtoFzjohdMc76DSFCSmbaUZBRWOGzoOCjRfNAtjhItyMFSVzryx3q7R781ppG7owBGCjzALer6CPjW0ZA3Fz2Uto7LwnkzyYZAifhU6SI1LoScpQSkIx76MYKhNxngXfdxnDCi89oZAogBDgGqND3WvtD4P6O0lXk1hBZBU4irZBZBmH1omqNzLMKVYoZAKIh8Xlc8NlzPFQ4NtGKXQAisNkaT5HkM"
# PHONE_NUMBER_ID = "03206010205"

VERIFY_TOKEN = os.getenv("mywhatsappbot123")
WHATSAPP_TOKEN = os.getenv("EAATq4RblNQoBQkmU6IAsyDdt6wI8Q7i8rR5prP96Mmbr18HEYRuIfMqK2yUtoFzjohdMc76DSFCSmbaUZBRWOGzoOCjRfNAtjhItyMFSVzryx3q7R781ppG7owBGCjzALer6CPjW0ZA3Fz2Uto7LwnkzyYZAifhU6SI1LoScpQSkIx76MYKhNxngXfdxnDCi89oZAogBDgGqND3WvtD4P6O0lXk1hBZBU4irZBZBmH1omqNzLMKVYoZAKIh8Xlc8NlzPFQ4NtGKXQAisNkaT5HkM")
PHONE_NUMBER_ID = os.getenv("03206010205")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid token", 403

    data = request.json
    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
    except:
        return "ok", 200

    reply = "Hello 👋 Your WhatsApp bot is now LIVE!"

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

if __name__ == "__main__":
    app.run()
