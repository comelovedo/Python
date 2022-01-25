# Телеграм Бот

# Content types:
# audio — аудиозапись;
# photo — фотография, картинка;
# voice — голосовое сообщение;
# video — видеозапись;
# video_note - видео заметки
# document — документ;
# text — текстовое сообщение;
# location — геолокация;
# contact — контакт;
# sticker — стикер.
# new_chat_member,
# new_chat_photo
# delete_chat_photo
# group_chat_created,
# supergroup_chat_created
# channel_chat_created,
# migrate_to_chat_id
# migrate_from_chat_id
# pinned_message


# import telebot
#
# TOKEN = "5263070884:AAGRUPhMy68le_bYaj_9XHMyUB8DlMFmdLY"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(content_types=['voice'])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "Обернись, сзади Досманова!")
#
#
# bot.polling(none_stop=True)


import telebot

TOKEN = "5263070884:AAGRUPhMy68le_bYaj_9XHMyUB8DlMFmdLY"
bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.reply_to(message, f"Иди ты в баню, {message.chat.username}")


# Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD»
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)




