import telebot

bot = telebot.TeleBot("6775460441:AAHtVP5F9VPnCmu7e7b76apiw8-iv0wNM04")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Задайте свой вопрос")
    elif message.text == "Кто ты?":
        bot.send_message(message.from_user.id, "Я-бот, задача которого отвечать на ваши вопросы.")
    elif message.text == "Расписание":
        bot.send_message(message.from_user.id, "Расписание занятий вашей группы можно посмотреть в приложении:\n https://play.google.com/store/apps/details?id=com.appbstract.omstuhelper")
    elif message.text == "Преподаватели":
        bot.send_message(message.from_user.id,"Информацию о преподавательском составе можно найти на сайте ОмГТУ:\n https://www.omgtu.ru/sveden/employees/" )
    elif message.text == "Как не слететь со стипы?":
        bot.send_message(message.from_user.id,"Учиться, учиться и ещё раз учиться")
    elif message.text == "Контакты":
        bot.send_message(message.from_user.id,"Группа в ВК: https://vk.com/omskpoliteh\n Telegram:https://t.me/omgtu_live\n Наш сайт: https://omgtu.ru ",)
    elif message.text == "/help":
        bot.send_message(message.from_user.id,"Команды:\nКто ты?\nРасписание\nПреподаватели\nКонтакты\nКак не слететь со стипы?")
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши"/help"')


bot.polling(none_stop=True, interval=0)