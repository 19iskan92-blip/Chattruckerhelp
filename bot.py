import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

SYSTEM_PROMPT = """Sen trucker (yuk mashina haydovchi) larga yordam beruvchi AI assistentsan. 
Faqat trucking, yo'l, yuk tashish, hujjatlar, qoidalar haqida savollarga javob ber.
Javoblarni qisqa va aniq yoz. O'zbek va Rus tillarini tushunasen."""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_text = message.text
        response = model.generate_content(SYSTEM_PROMPT + "\n\nSavol: " + user_text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi. Qaytadan urinib ko'ring.")

bot.polling()

