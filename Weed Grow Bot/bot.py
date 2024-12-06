# bot.py: Hauptprogramm
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from handlers import start, button_handler  




import sys
print("Python-Suchpfad:", sys.path)
sys.path.append(r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot')


import os
print("Aktuelles Arbeitsverzeichnis:", os.getcwd())

os.chdir(r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot')


# Hauptfunktion
def main():
    try:
        application = ApplicationBuilder().token(BOT_TOKEN).build()

        # CommandHandler für /start
        application.add_handler(CommandHandler("start", start))

        # CallbackQueryHandler für Buttons
        application.add_handler(CallbackQueryHandler(button_handler))

        print("Bot gestartet. Drücken Sie STRG+C, um den Bot zu stoppen.")
        logger.info("Bot wurde erfolgreich gestartet.")
        application.run_polling()
    except Exception as e:
        logger.critical(f"Bot konnte nicht gestartet werden: {e}")

if __name__ == "__main__":
    main()
