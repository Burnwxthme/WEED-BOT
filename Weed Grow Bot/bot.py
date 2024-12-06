import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import start, button_handler

# Hauptprogramm
def main():
    try:
        application = ApplicationBuilder().token(BOT_TOKEN).build()

        # Handler hinzufügen
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_handler))

        print("Bot gestartet. Drücken Sie STRG+C, um den Bot zu stoppen.")
        application.run_polling()
    except Exception as e:
        print(f"Fehler beim Starten des Bots: {e}")

if __name__ == "__main__":
    main()
