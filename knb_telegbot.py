import telebot
from telebot import types
import secretnuy
import random
bot = telebot.TeleBot(token=secretnuy.botToken)

name = 'Капибара'

energy = 70
satiety = 20
happiness = 100

def feed():
    global satiety, energy
    satiety += 20
    energy += 20
def wrong_feed():
    global satiety, energy, happiness
    satiety -= 20
    energy -= 20
    happiness -= 20
def play():
    global satiety, energy, happiness
    happiness += 10
    satiety -= 5
    energy -= 5

def sleep():
    global satiety, energy, happiness
    energy = 70
    happiness += 5
    satiety -= 10

keyboard1 = types.InlineKeyboardMarkup()
but1 = types.InlineKeyboardButton("Тухлая рыба", callback_data='button1')
but2 = types.InlineKeyboardButton("Мясное Рагу", callback_data='button2')
but3 = types.InlineKeyboardButton("Тортик", callback_data='button3')
keyboard1.add(but1, but2, but3)


keyboard2 = types.ReplyKeyboardMarkup()
but4 = types.KeyboardButton("/stats")
but5 = types.KeyboardButton("/feed")
but6 = types.KeyboardButton("/play")
but7 = types.KeyboardButton("/sleep")
but8 = types.KeyboardButton("/setname")
but9 = types.KeyboardButton("/quotes")
but10 = types.KeyboardButton("/help")
keyboard2.add(but4, but5, but6, but7, but8, but9, but10)

citati = ["https://i.pinimg.com/originals/c4/5e/9d/c45e9d8b43a9038d7595ae18ebe1a37c.jpg", "https://i.pinimg.com/236x/77/aa/b6/77aab6325a0eec1c1a3c5787f69bca22.jpg", "https://cs11.pikabu.ru/images/big_size_comm/2020-02_5/1582536965136239521.jpg", "https://vse-frazi.ru/wp-content/uploads/2020/08/%D0%A6%D0%B8%D1%82%D0%B0%D1%82%D0%B0-%D0%BF%D1%80%D0%BE-%D0%B2%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2-%D0%BC%D0%B5%D0%BC-%E2%84%96-2.jpg"]


@bot.message_handler(commands=['help'])
def helper(message):
    bot.reply_to(message, f"Список доступных команд:\n /stats-состояние вашего героя\n /feed-покормить питомца\n /play-поиграть с питомцем\n /sleep-питомец поспит\n /setname-изменить имя питомца\n /quotes-цитаты с волками\n")



@bot.message_handler(commands=['quotes'])
def citatki(message):
    randomphoto = random.choice(citati)
    bot.send_photo(message.chat.id, randomphoto)

@bot.message_handler(commands=['setname'])
def setname(message):
    bot.send_message(message.chat.id, "Введите новое имя: ")
    bot.register_next_step_handler(message, newname)
def newname(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, f"Готово! Новое имя питомца: {name}")

@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id, f"Привет, я твой питомец: {name}", reply_markup=keyboard2)

@bot.message_handler(commands=['feed'])
def feedHandler(message):
    bot.send_message(message.chat.id, "Выберите чем покормить вашего питомца: 'Тухлая рыба', 'Мясное Рагу', 'Тортик'", reply_markup=keyboard1)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, "Ваш питомец отравился")
        wrong_feed()

    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, "Ваш питомец вкусно поел!")
        feed()

    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, "Ваш питомец вкусно поел!")
        feed()




# def food_types(message):
#     global keyboard
#     choice = message.text
#     if choice == 'Тухлая рыба':
#         bot.send_message(message.chat.id, "Ваш питомец отравился!")
#         wrong_feed()
#     elif choice == 'Мясное Рагу':
#         bot.send_message(message.chat.id, "Ваш питомец вкусно поел!")
#         feed()
#     elif choice == 'Тортик':
#         bot.send_message(message.chat.id, "Ваш питомец вкусно поел!")
#         feed()
#     check(message)


@bot.message_handler(commands=['stats'])
def stats(message):
    global satiety, energy, happiness
    bot.send_message(message.chat.id, f"Статистика Героя:\nЭнергия: {energy}\nСчастье: {happiness}\nСытость: {satiety}")




@bot.message_handler(commands=['sleep'])
def sleepHandler(message):
    sleep()
    bot.send_message(message.chat.id, "Ваш питомец отлично поспал!")
    check(message)

@bot.message_handler(commands=['play'])
def playHandler(message):
    play()
    bot.send_message(message.chat.id, f"Ваш питомец круто поиграл!")
    check(message)

def check(message):
    global satiety, energy, happiness

    if satiety <= 0:
        bot.reply_to(message, f"Ваш {name} умер от голода!")
    elif satiety >= 150:
        bot.reply_to(message, f"Ваш {name} переел!")

    if energy <= 0:
        bot.reply_to(message, f"Ваш {name} умер от нехватки сил!")
    elif energy >= 200:
        bot.reply_to(message, f"Ваш {name} получил бешенство!")

    if happiness <= 0:
        bot.reply_to(message, f"Ваш {name} умер от тоски! Нужно играть с питомцем!")
    elif happiness > 0:
        bot.reply_to(message, f"Ваш {name} счастлив как никогда!")

    print(f"S: {satiety}, E:{energy}, H{happiness}")

@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.send_message(message.chat.id, "Я вас не понял!")
    pass


bot.polling(none_stop=True)








