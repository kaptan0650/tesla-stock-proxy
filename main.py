# Deploy tetikleme - tarih: 07.07.2025
import os
import httpx
import asyncio

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

async def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)

# Test mesajı
if __name__ == "__main__":
    asyncio.run(send_message("@slymnoz", "🚗 Test: Model Y SR (Siyah İç) Tesla envantere eklendi!"))
