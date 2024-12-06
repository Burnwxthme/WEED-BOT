# handlers.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from logger import logger  # Stelle sicher, dass logger korrekt importiert wird

# Start-Befehl
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")],
        [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Willkommen beim Plant Clicker Bot! Wähle eine Aktion aus:",
        reply_markup=reply_markup
    )
    logger.info(f"User {update.effective_user.username} hat /start benutzt.")

# Callback-Handler für Buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plant_clicker":
        await query.edit_message_text("🌱 Du hast die Pflanze angeklickt!")
        logger.info(f"User {update.effective_user.username} hat 'Plant Clicker' gedrückt.")
    elif query.data == "harvest":
        await query.edit_message_text("Du hast +3 Buds erhalten! 🌿")
        logger.info(f"User {update.effective_user.username} hat 'Harvest!' gedrückt.")
