
import time
import requests
import telegram
from bs4 import BeautifulSoup

# 🔐 ВСТАВ СВІЙ ТОКЕН НИЖЧЕ
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = 7178838399

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def check_exam_slot():
    url = "https://eq.hsc.gov.ua/cabinet/queue"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("Помилка завантаження сторінки")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        if "Чернігів" in soup.text and "31.05.2025" in soup.text and "практичний іспит" in soup.text:
            message = "🔔 З'явився квиток на практичний іспит у Чернігові на 31 травня!"
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
            print("✅ Надіслано повідомлення!")
        else:
            print("❌ Немає квитків. Перевірка...")

    except Exception as e:
        print(f"Помилка при перевірці: {e}")

if __name__ == "__main__":
    while True:
        check_exam_slot()
        time.sleep(60)  # перевірка кожні 60 секунд
