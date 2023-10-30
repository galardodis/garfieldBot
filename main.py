import telebot
from tokens import TELE_TOKEN
from search import search

bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = '*Вас приветствует зоомагазин Garfield\!*\n\n' \
           'Введите название искомого товара или его артикул и посмотрите какие предложения есть в нашем магазине\n\n' \
           'Помощь через команду /help'
    bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Для того чтобы найти товар введите название искомого товара или его артикул'

    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    text = message.text
    products = search(text)
    if products:
        for pr in products:
            try:
                bot.send_photo(message.chat.id,
                               photo=pr["img"],
                               caption=f'{pr["name"]}\n'
                                       f'_{pr["art"]}_\n'
                                       f'*Стоимость {pr["prise"]}*\n'
                                       f'[Заказать]({pr["href"]})',
                               parse_mode='MarkdownV2'
                               )
            except Exception as e:
                print('-' * 1000)
                print(f'{e}\n{pr["href"]}')
                print(len(pr['img']))
                print(f'{pr["img"]}\n'
                      f'{pr["name"]}\n'
                      f'_{pr["art"]}_\n'
                      f'*Стоимость {pr["prise"]}*\n'
                      f'[Заказать]({pr["href"]})', )
                bot.send_message(message.chat.id, 'ERROR')
                continue
    else:
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено :(')


bot.polling()
