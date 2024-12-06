# handlers.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

import sys
sys.path.append(r'c:\Users\Administrator\PythonPojects\Weed_Grow\Weed Grow Bot')
from handlers import start, button_handler



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

# Callback-Handler für Buttons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "plant_clicker":
        await query.edit_message_text("🌱 Du hast die Pflanze angeklickt!")
    elif query.data == "harvest":
        await query.edit_message_text("Du hast +3 Buds erhalten! 🌿")
