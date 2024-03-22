import time
import telebot

token = '6660330975:AAGYreRR3BacC4s2u6NtniW20KKU145qjyY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text='Как твои дела? Чем я могу помочь?')


@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)


@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, text=f'***{text.upper()}!***')


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_id = 'CAACAgIAAxkBAANFZf3CkvqswA3fdkLtLskRSXoa8D0AAgIAA_NjxCynZhNyRnyTrjQE'
    bot.send_sticker(message.chat.id, file_id)


@bot.message_handler(content_types=['text'])
def revers_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, text='Текст содержит слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)


bot.polling()