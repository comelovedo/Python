import telebot
from Config import keys, Currencies, TOKEN
from Extentions import CryptoConvector, APIException

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_help(message: telebot.types.Message, ):
    text = 'Чтобы начать работу, введите комманду в следующем формате: \b<Какую валюту хотите конвектировать>  \
     <В какую валюту хотите конвектировать> \
     <Сумма конвектируемой валюты\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


# По комманде value  выдает все допустимые валюты
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in Currencies.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException("Слишком много параметров либо некорректные данные попробуйте /values для "
                               "уточнения параметров и /help для помощи")

        # quote - валюта которую хотим конвектировать base - валюта в которую хотим конвектировать, amount - кол-во
        # валюты
        quote, base, amount = values
        total_base = CryptoConvector.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать комманду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
