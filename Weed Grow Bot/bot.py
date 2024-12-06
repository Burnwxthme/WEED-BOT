from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from Buttons.main_menu import start, main_menu_handler
from Buttons.Plant_clicker import plant_clicker_handler
from Buttons.inventory import inventory_handler
from Buttons.Harvest import harvest_handler




import os
print("Aktuelles Arbeitsverzeichnis:", os.getcwd())
os.chdir(r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot')


def main():
    try:
        application = ApplicationBuilder().token(BOT_TOKEN).build()

        # CommandHandler für /start
        application.add_handler(CommandHandler("start", start))

        # CallbackQueryHandler für alle Buttons
        application.add_handler(CallbackQueryHandler(main_menu_handler, pattern="main_menu"))
        application.add_handler(CallbackQueryHandler(plant_clicker_handler, pattern="plant_clicker"))
        application.add_handler(CallbackQueryHandler(inventory_handler, pattern="inventory"))
        application.add_handler(CallbackQueryHandler(harvest_handler, pattern="harvest"))

        print("Bot gestartet. Drücken Sie STRG+C, um den Bot zu stoppen.")
        application.run_polling()
    except Exception as e:
        print(f"Fehler beim Starten des Bots: {e}")

if __name__ == "__main__":
    main()
