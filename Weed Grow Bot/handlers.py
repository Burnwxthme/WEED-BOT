from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Start-Befehl
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            [InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")],
            [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "Willkommen beim Plant Clicker Bot! Wähle eine Aktion aus:",
            reply_markup=reply_markup
        )
        print(f"User {update.effective_user.username} hat /start benutzt.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten des /start-Kommandos: {e}")

# Callback-Handler für Buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()

        if query.data == "plant_clicker":
            await query.edit_message_text("🌱 Du hast die Pflanze angeklickt!")
            print(f"User {update.effective_user.username} hat 'Plant Clicker' gedrückt.")
        elif query.data == "harvest":
            await query.edit_message_text("Du hast +3 Buds erhalten! 🌿")
            print(f"User {update.effective_user.username} hat 'Harvest!' gedrückt.")
    except Exception as e:
        print(f"Fehler beim Verarbeiten eines Buttons: {e}")
