import telebot
import config
from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)
day = datetime.isoweekday(datetime.now())

@bot.message_handler(commands=['start'])
def send_schedule(message):
    bodia = open('images/bodia.png', 'rb')
    bot.send_message(message.chat.id, 'Жан Клод Богдан')
    bot.send_photo(message.chat.id, bodia)
    bot.send_message(message.chat.id, 'Готовий побачити що тебе сьогодні жде?!!!')
    bot.send_message(message.chat.id, 'Напиши "розклад" щоб отримати розклад на тиждень або "сьогодні"!')


@bot.message_handler(content_types=['text'])
def send_schedule(message):
    reaction = open('images/goraila_posle_uvidenogo.jpg', 'rb')
    if message.text == 'розклад':
        sch = open('images/schedule.jpg', 'rb')
        bot.send_photo(message.chat.id, sch)
        bot.send_photo(message.chat.id, reaction)
        bot.send_message(message.chat.id, 'Удачи!')
        bot.send_message(message.chat.id, 'Ахахахахахаха')
        bot.send_message(message.chat.id, 'Ахахахахахаха')
        bot.send_message(message.chat.id, 'Ахахахахахаха')
        bot.send_message(message.chat.id, 'Вам понравился бот? (Да Нет)')
    if message.text == 'сьогодні':
        today = open('images/days/d' + str(day) + '.png', 'rb')
        bot.send_photo(message.chat.id, today)
        if day != 6 or day != 7:
            bot.send_photo(message.chat.id, reaction)
        bot.send_message(message.chat.id, "Вам понравился бот? (Да Нет)")

    if message.text == 'Да':
        n1 = open('images/nrav.jpg', 'rb')
        bot.send_photo(message.chat.id, n1)

    if message.text == 'Нет':
        n2 = open('images/nenrav.jpg', 'rb')
        bot.send_photo(message.chat.id, n2)


bot.polling(none_stop=True)