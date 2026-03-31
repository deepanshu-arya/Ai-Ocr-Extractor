import requests

def send_whatsapp(number, message):
    url = "https://graph.facebook.com/v18.0/YOUR_PHONE_ID/messages"

    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": message}
    }

    headers = {
        "Authorization": "Bearer YOUR_TOKEN",
        "Content-Type": "application/json"
    }

    requests.post(url, json=data, headers=headers)