# bot.py: Hauptlogik für den Telegram-Bot
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Button erstellen
    keyboard = [[InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Antwort mit dem Button senden
    await update.message.reply_text("Willkommen beim Plant Clicker Bot! Klicke auf den Button, um loszulegen.", reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # CommandHandler für /start
    application.add_handler(CommandHandler("start", start))

    print("Bot gestartet. Drücken Sie STRG+C, um den Bot zu stoppen.")
    application.run_polling()

if __name__ == "__main__":
    main()
