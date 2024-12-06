import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data import user_progress
from Inventory_data import user_inventory

async def harvest_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        user_id = query.from_user.id

        # Überprüfen, ob der Nutzer "Plant Clicker" vorher gedrückt hat
        if not user_progress.get(user_id, {}).get("plant_clicked", False):
            await query.edit_message_text(
                text="❌ Du musst zuerst die Pflanze anklicken, bevor du ernten kannst!"
            )
            return

        # Nachricht anzeigen, dass die Ernte beginnt
        await query.edit_message_text(
            text="🌾 Ernte läuft... Bitte warte 2 Sekunden."
        )

        # 2 Sekunden warten
        await asyncio.sleep(2)

        # Buds hinzufügen
        user_inventory[user_id] = user_inventory.get(user_id, {"buds": 0})
        user_inventory[user_id]["buds"] += 3

        # Buttons für erneutes Ernten oder Zurückgehen
        keyboard = [
            [InlineKeyboardButton("Harvest! 🌾", callback_data="harvest")],
            [InlineKeyboardButton("Zurück zum Hauptmenü", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Nachricht mit Erfolg anzeigen
        await query.edit_message_text(
            text=f"✅ Du hast +3 Buds erhalten! 🌿 Insgesamt: {user_inventory[user_id]['buds']} Buds.",
            reply_markup=reply_markup
        )
        print(f"User {query.from_user.username} hat geerntet. Gesamte Buds: {user_inventory[user_id]['buds']}")

    except Exception as e:
        print(f"Fehler beim Verarbeiten des Harvest-Buttons: {e}")
