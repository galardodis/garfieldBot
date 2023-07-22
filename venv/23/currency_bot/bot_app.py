import telebot
import time
from tokens import TELE_TOKEN
from extensions import CryptoConverter, APIException, ls

bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите мне команду в формате: \n\n' \
           '<имя валюты для перевода>  ' \
           '<имя валюты в кототую нужно перевести>  ' \
           '<количество переводимой валюты>' \
           '\n\nПример ввода: Доллар Рубль 10' \
           '\n\nДля получения списка валют введите: /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in ls.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=[])
def help(message: telebot.types.Message):
    raise APIException('Я не знаю такой команды')


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise APIException('Слишком много параметров :( '
                               '\n\nПопробуй ешё раз\nПример ввода: Доллар Рубль 10')

        elif len(values) < 3:
            raise APIException('Слишком мало параметров :( '
                               '\n\nПопробуй ешё раз\nПример ввода: Доллар Рубль 10')

        quote, base, amount = map(str.capitalize, values)
        total_base = CryptoConverter.get_price(quote, base, amount)

    except APIException as e:
        bot.reply_to(message, f'Ты ошибся с вводом\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')

    else:
        text = f'{amount} {quote} = {total_base} {base}\n' \
               f'Согласно сайту www.cryptocompare.com на {time.strftime("%d %b %Y %H:%M:%S")}'
        bot.send_message(message.chat.id, text)


bot.polling()
