import telebot
import time
from tokens import TELE_TOKEN
from extensions_mod import CryptoConverter, APIException, currencie

bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите мне команду в формате: \n\n' \
           '<Код валюты для перевода>  ' \
           '<Код валюты в кототую нужно перевести>  ' \
           '<количество переводимой валюты>' \
           '\n\nПример ввода: USD RUB 10' \
           '\n\nДля получения списка поддерживаемых валют и их кодов введите: /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in dict(sorted(currencie.items())):
        text = '\n'.join((text, f'{key} - {currencie[key]}'))
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
                               '\n\nПопробуй ешё раз\nПример ввода: USD RUB 10')

        elif len(values) < 3:
            raise APIException('Слишком мало параметров :( '
                               '\n\nПопробуй ешё раз\nПример ввода: USD RUB 10')

        quote, base, amount = values[0].upper(), values[1].upper(), values[2]
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
