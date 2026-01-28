from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@app.get("/webhook")
async def verify_webhook(
    hub_mode: str = None,
    hub_challenge: str = None,
    hub_verify_token: str = None
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return {"error": "Verification failed"}


@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        entry = data["entry"][0]
        change = entry["changes"][0]
        value = change["value"]
        message = value["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]

        send_message(sender, f"You said: {text}")

    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}


def send_message(to, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=payload)
