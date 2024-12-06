from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from Speicherstand.Inventory import user_inventory

async def inventory_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    buds = user_inventory.get(user_id, {}).get("buds", 0)

    keyboard = [
        [InlineKeyboardButton("Zurück zum Hauptmenü", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=f"📦 Dein Inventar:\n\n🌿 Buds: {buds}",
        reply_markup=reply_markup
    )
