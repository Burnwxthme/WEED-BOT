from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Variable, um den Zustand zu verfolgen
user_progress = {}

# Start-Befehl
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        user_progress[user_id] = {"plant_clicked": False}  # Fortschritt initialisieren

        # Hauptmenü anzeigen
        keyboard = [[InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "Willkommen beim Plant Clicker Bot! Drücke auf 'Plant Clicker', um zu starten.",
            reply_markup=reply_markup
        )
        print(f"User {update.effective_user.username} hat /start benutzt.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten des /start-Kommandos: {e}")

# Callback-Handler für Buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        user_id = query.from_user.id
        await query.answer()

        # Wenn der Nutzer auf "Plant Clicker" klickt
        if query.data == "plant_clicker":
            user_progress[user_id]["plant_clicked"] = True

            # "Harvest!"-Button anzeigen
            keyboard = [
                [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")],
                [InlineKeyboardButton("Back to Main Menu", callback_data="back_to_main")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            await query.edit_message_text(
                text="🌱 Du hast die Pflanze angeklickt! Jetzt kannst du ernten.",
                reply_markup=reply_markup
            )
            print(f"User {query.from_user.username} hat 'Plant Clicker' gedrückt.")

        # Wenn der Nutzer auf "Harvest!" klickt
        elif query.data == "harvest":
            if user_progress.get(user_id, {}).get("plant_clicked", False):
                # "Harvest!"-Button erneut anzeigen
                keyboard = [
                    [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")],
                    [InlineKeyboardButton("Back to Main Menu", callback_data="back_to_main")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await query.edit_message_text(
                    text="Du hast +3 Buds erhalten! 🌿",
                    reply_markup=reply_markup
                )
                print(f"User {query.from_user.username} hat 'Harvest!' gedrückt.")
            else:
                await query.edit_message_text(
                    text="Du musst zuerst auf 'Plant Clicker' klicken, bevor du ernten kannst!"
                )
                print(f"User {query.from_user.username} hat versucht zu ernten, ohne 'Plant Clicker' zu drücken.")

        # Wenn der Nutzer auf "Back to Main Menu" klickt
        elif query.data == "back_to_main":
            # Hauptmenü anzeigen
            keyboard = [[InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            await query.edit_message_text(
                text="Du bist zurück im Hauptmenü. Wähle eine Option.",
                reply_markup=reply_markup
            )
            print(f"User {query.from_user.username} ist zurück zum Hauptmenü gegangen.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten eines Buttons: {e}")
