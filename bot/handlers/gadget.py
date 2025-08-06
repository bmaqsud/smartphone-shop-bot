from telegram import Update
from telegram.ext import CallbackContext
from ..db import user_db, smartphone_db
from ..keyboards.reply import get_gadget_keyboard, get_telefon_keyboard, get_apple_telefon_keyboard


def send_gadgets(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.message.from_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Gadget Turlari",
            reply_markup=get_gadget_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Главное меню:",
            reply_markup=get_gadget_keyboard("Русский")
        )


def send_telefonlar(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_telefon_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_telefon_keyboard("Русский")
        )


def send_apple_telefonlar(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Apple Telefonlar",
            reply_markup=get_apple_telefon_keyboard("O'zbekcha")
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Telefonlar",
            reply_markup=get_apple_telefon_keyboard("Русский")
        )

def send_apple_telefon(update: Update, context: CallbackContext) -> None:
    user_data = user_db.get_user(str(update.effective_user.id))

    if 'language' not in user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Iltimos, avval tilni tanlang.")
        return

    language = user_data['language']
    
    if language == "O'zbekcha":
            for phone in smartphone_db.get_iphone_x():
                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=phone['image_url'],
                    caption=f"""📱 <b><u>iPhone X</u></b>
                    💵 price: {phone['price']}
                    🎨 color: {phone['color']}
                    🔋 Batareya holati: {phone['yomkus']}
                    💾 Xotira: {phone['xotira']}
 
                """,
                   parse_mode="HTML"
                )
    else:
         for phone in smartphone_db.get_iphone_x():
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=phone['image_url'],
                caption=f"""📱  <b><u>iPhone X</u></b>
                💵 Цена: {phone['price']}
                🎨 Цвет: {phone['color']}
                🔋 Состояние батареи: {phone['yomkus']}
                💾 Память: {phone['xotira']}
                """,
                parse_mode="HTML"
            )

    if language == "O'zbekcha":
            for phone in smartphone_db.get_iphone_11():
                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=phone['image_url'],
                    caption=f"""📱 <b><u>iPhone 11</u></b>
                    💵 price: {phone['price']}
                    🎨 color: {phone['color']}
                    🔋 Batareya holati: {phone['yomkus']}
                    💾 Xotira: {phone['xotira']}
 
                """,
                )
    else:
          for phone in smartphone_db.get_iphone_x():
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=phone['image_url'],
                caption=f"""📱  <b><u>iPhone 11</u></b>
                💵 Цена: {phone['price']}
                🎨 Цвет: {phone['color']}
                🔋 Состояние батареи: {phone['yomkus']}
                💾 Память: {phone['xotira']}
                """,
                parse_mode="HTML"
            )