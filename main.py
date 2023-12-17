import telebot
import scanner
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
KM_LIMITATION = 50

bot = telebot.TeleBot(TOKEN)
scanner = scanner.Scanner()


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text="Привет, скинь локацию")


@bot.message_handler(content_types=["text"])
def generic_reply(message):
    bot.send_message(message.chat.id, text='Скинь локацию')


@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        user_lat = message.location.latitude
        user_lon = message.location.longitude

        scanner.closest_dest = float
        scanner.user_coord = (user_lat, user_lon)
        scan_for_toilets = scanner.toilet_parse()

        if int(scanner.closest_dest) < KM_LIMITATION:
            reply_scanner = f'Туалет всего-то в *{round(scanner.closest_dest, 3)}* км от вас!\n\n*Адрес(можно скопировать):* `{scanner.closest_adress}`\n*Тип:* {scanner.closest_type}\n*Часы работы:* {scanner.closest_timework}\n*Забавный факт:* {scanner.closest_content}'
            bot.send_message(message.chat.id, text=reply_scanner, parse_mode='Markdown')
            bot.send_location(message.chat.id,
                              latitude=scanner.closest_lat,
                              longitude=scanner.closest_lon)

            print(scanner.user_coord)
            print(scanner.closest_adress)
            print(scanner.closest_lat, scanner.closest_lon)
            print(round(scanner.closest_dest, 3))
        else:
            bot.send_message(message.chat.id,
                             text=f'Извините, но ближайший туалет от вас больше, чем в {KM_LIMITATION} км! Придется потерпеть..')
            print(f'TOO FAR: {scanner.closest_dest}')


bot.infinity_polling()
