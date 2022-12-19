import telebot
import config

bot1 = telebot.TeleBot(config.TOKEN)

@bot1.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot1.send_sticker(message.chat.id, sti)
    bot1.send_message(message.chat.id, "Шалом, {0.first_name}!\nЯ бот - <b>{1.first_name}</b>, бот созданный для того чтобы ты начал(а) смотреть Волчонка!".format(message.from_user, bot1.get_me()),
        parse_mode='html')

@bot1.message_handler(content_types=['text'])
def lalala(message):
    bot1.send_message(message.chat.id, message.text)

#RUN
bot1.polling(none_stop=True)