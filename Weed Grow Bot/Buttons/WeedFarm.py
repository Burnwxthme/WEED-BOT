from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from Speicherstand.data import user_progress

async def plant_clicker_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    user_progress[user_id] = user_progress.get(user_id, {})
    user_progress[user_id]["plant_clicked"] = True

    keyboard = [
        [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")],
        [InlineKeyboardButton("Zurück zum Hauptmenü", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text="🌱 Du hast die Pflanze angeklickt! Jetzt kannst du ernten.",
        reply_markup=reply_markup
    )
