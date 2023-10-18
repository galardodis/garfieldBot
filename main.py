import telebot
from token import TELE_TOKEN
from search import search
from extension import CryptoConverter, APIException

# from background import keep_alive  #постоянный онлайн

# import bot_app_world

bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Привет! Я Бот-Конвертер валют и я могу:  \n\n' \
           '- Показать список доступных валют и их кодов через команду: /values' \
           '\n\n- Показать курсы валют на сегодня по отношению к белорусскрму рублю через команду /course' \
           '\n\n- Вывести конвертацию валюты через команду:\n' \
           '<Количество переводимой валюты>  ' \
           '<Код валюты для перевода>  ' \
           '<Код валюты в кототую нужно перевести>  ' \
           '\n\nПример ввода: 10 USD BYN' \
           '\n\n' \
           'Напомнить, что я могу через команду: /help'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def helpp(message: telebot.types.Message):
    text = 'Я могу:  \n\n' \
           '- Показать список доступных валют и их кодов через команду: /values' \
           '\n\n- Показать курсы валют на сегодня по отношению к белорусскрму рублю через команду /course' \
           '\n\n- Вывести конвертацию валюты через команду:\n' \
           '<Количество переводимой валюты>  ' \
           '<Код валюты для перевода>  ' \
           '<Код валюты в кототую нужно перевести>  ' \
           '\n\nПример ввода: 10 USD BYN' \
           '\n\n' \
           'Напомнить, что я могу через команду: /help'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    text = message.text.split()
    products = search(text)
    for i in products:
        bot.send_message(message.chat.id, i)

# try:
    #     values = message.text.split(' ')
    #
    #     if len(values) > 3:
    #         raise APIException('Слишком много параметров, '
    #                            'Попробуй ешё раз\n\nПример ввода: 10 USD BYN')
    #
    #     elif len(values) < 3:
    #         raise APIException('Слишком мало параметров, '
    #                            'Попробуй ешё раз\n\nПример ввода: 10 USD BYN')
    #
    #     amount, quote, base = values[0], values[1].upper(), values[2].upper()
    #     total_base = CryptoConverter.get_price(quote, base, amount)
    #
    # except APIException as e:
    #     bot.reply_to(message, f'Ты ошибся с вводом\n{e}')
    #
    # except Exception as e:
    #     bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    # else:
    #     text = f'{amount} {quote} = {total_base} {base}\n' \
    #            f'По курсу НБ РБ на {time.strftime("%d %b %Y %H:%M:%S")}'
    #     bot.send_message(message.chat.id, text)


# keep_alive() #постоянный онлайн
# if __name__ == '__main__':
bot.polling()
