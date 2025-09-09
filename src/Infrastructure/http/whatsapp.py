import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("+5511953513568")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number: str, code: str):
    try:
        message = client.messages.create(
            body=f"🔑 Seu código de ativação é: {code}",
            from_=TWILIO_WHATSAPP_NUMBER,
            to=f"whatsapp:{to_number}" if not to_number.startswith("whatsapp:") else to_number
        )
        return message.sid
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")
        return None
