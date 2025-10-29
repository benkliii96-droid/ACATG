from config import TOKEN, values_
import extensions
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def instruction(message):
    text = ("Бот переводит валюты. Принимает данные в виде:\n<имя валюты, цену которой ты хочешь узнать>"
            "\n<имя валюты, в которой надо узнать цену первой валюты>\n<количество первой валюты>.\nУзнать список всех"
            "доступных валют: /values")
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message):
    bot.send_message(message.chat.id, "Список всех доступных валют:")
    for i in sorted(values_):
        bot.send_message(message.chat.id, i)


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        mes = message.text.split()

        if len(mes) != 3:
            raise extensions.APIException("Нужно 3 параметра.")

        base, quote, amount = mes
        total = extensions.API.get_price(base, quote, amount)
    except extensions.APIException as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось выполнить.\n{e}")
    else:
        text = f"Цена {amount} {base} в {quote} - {total}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
