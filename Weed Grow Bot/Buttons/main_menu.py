from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")],
        [InlineKeyboardButton("Inventar", callback_data="inventory")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Willkommen beim Plant Clicker Bot! Wähle eine Option:",
        reply_markup=reply_markup
    )

async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Plant Clicker", callback_data="plant_clicker")],
        [InlineKeyboardButton("Inventar", callback_data="inventory")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query = update.callback_query
    await query.edit_message_text(
        text="Du bist zurück im Hauptmenü. Wähle eine Option:",
        reply_markup=reply_markup
    )
