# Content types:
# audio — аудиозапись;
# photo — фотография, картинка;
# voice — голосовое сообщение;
# video — видеозапись;
# document — документ;
# text — текстовое сообщение;
# location — геолокация;
# contact — контакт;
# sticker — стикер.

import telebot

TOKEN = "5263070884:AAGRUPhMy68le_bYaj_9XHMyUB8DlMFmdLY"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Обернись, сзади Юлька!")


bot.polling(none_stop=True)
