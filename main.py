import uuid
import telebot
import random
from PIL import Image
from telebot import types


picture = {}
token = '632107141:AAEy6F1g3ZxJj1q7-kqCv-ltuvsdw-HDXGk' 
bot = telebot.TeleBot(token=token)

def process(filename):
    my_filter = random.choice([image_one, image_two, image_three, image_four, image_five, image_six])
    return my_filter(filename)

def image_one(path):
        img = Image.open(path)

        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                a = (r+g+b) // 3
                pixels[i, j] = (a, a, a)
        img.save(path)
        img.close()
        return open(path, 'rb').read()

        

def image_two(path):
        img = Image.open(path)

        factor = 70
        pixels = img.load()


        for i in range(img.width):
             for j in range(img.height):
                 rand = random.randint(-factor, factor)
                 r = pixels[i, j][0] + rand
                 g = pixels[i, j][1] + rand
                 b = pixels[i, j][2] + rand
                 if (r < 0):
                     r = 0
                 if (g < 0):
                     g = 0
                 if (b < 0):
                     b = 0
                 if (r > 255):
                     r = 255
                 if (g > 255):
                     g = 255
                 if (b > 255):
                     b = 255
                 pixels[i, j] = (r, g, b)
        img.save(path)
        img.close()
        return open(path, 'rb').read()

        
def image_three(path):
        img = Image.open(path)

        factor = 70
        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                if (r < factor):
                    r = 0
                if (g < factor):
                    g = 0
                if (b < factor):
                    b = 0
                if (r > factor):
                    r = 255
                if (g > factor):
                    g = 255
                if (b > factor):
                    b = 255
                pixels[i, j] = (r, g, b)
        img.save(path)
        img.close()
        return open(path, 'rb').read()


        

def image_four(path):
        img = Image.open(path)

        factor = 70
        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                S = (r+g+b) // 3
                
                pixels[i, j] = (r, g, b)
        img.save(path)
        img.close()
        return open(path, 'rb').read()


        

def image_five(path):
        img = Image.open(path)

        factor = 70
        pixels = img.load()


        for i in range(img.width//2):
            for j in range(img.height//2):
                r, g, b = pixels[i, j]
                r = r + factor
                g = g - factor
                b = b - factor
                pixels[i, j] = (r, g, b)
        for i in range(img.width//2):
            for j in range(img.height//2,img.height):
                r, g, b = pixels[i, j]
                r = r - factor
                g = g + factor
                b = b - factor
                pixels[i, j] = (r, g, b)
        for i in range(img.width//2,img.width):
            for j in range(img.height//2,img.height):
                r, g, b = pixels[i, j]
                r = r - factor
                g = g - factor
                b = b + factor
                pixels[i, j] = (r, g, b)
        for i in range(img.width//2,img.width):
            for j in range(img.height//2):
                r, g, b = pixels[i, j]
                a = (r+g+b) // 3
                pixels[i, j] = (a, a, a)
        img.save(path)
        img.close()
        return open(path, 'rb').read()

        

def image_six(path):
        img = Image.open(path)

        pixels = img.load()
        for i in range(img.width//2):
            for j in range(img.height):
                r,g,b = pixels[i,j]
                pixels[img.width-1-i,j] = pixels[i,j]
        img.save(path)
        img.close()
        return open(path, 'rb').read()
                



@bot.message_handler(content_types=['photo'])
def photo(message):
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)
    user = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    extn = '.' + str(path.file_path).split('.')[-1]
    name = 'images/' + str(uuid.uuid4()) + extn
    picture[user] = name
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    
    button1 = types.InlineKeyboardButton(text="Серый", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Шум", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Случайный", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="Черно-белый", callback_data="button4")
    button5 = types.InlineKeyboardButton(text="Четыре цвета", callback_data="button5")
    button6 = types.InlineKeyboardButton(text="Кек", callback_data="button6")
    button7 = types.InlineKeyboardButton(text="Рандом!!", callback_data="button7")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button6)
    keyboard.add(button7)
    bot.send_message(message.chat.id, "Выбирите, что сделать с фото!", reply_markup=keyboard)
    
@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    
    
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Отправте фото")
    


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global picture
    user = call.message.chat.id
    if call.message:
        if call.data == "button1":
            bot.send_photo(call.message.chat.id, image_one(picture[user]))
        if call.data == "button2":
            bot.send_photo(call.message.chat.id, image_two(picture[user]))
        if call.data == "button3":
            bot.send_photo(call.message.chat.id, image_three(picture[user]))
        if call.data == "button4":
            bot.send_photo(call.message.chat.id, image_four(picture[user]))
        if call.data == "button5":
            bot.send_photo(call.message.chat.id, image_five(picture[user]))
        if call.data == "button6":
            bot.send_photo(call.message.chat.id, image_six(picture[user]))
        if call.data == "button7":
            bot.send_photo(call.message.chat.id, process(picture[user]))
bot.polling(none_stop=True)
