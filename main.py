import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = (
        "Привет! Я бот для конвертации валют.\n"
        "Формат запроса:\n"
        "<имя валюты> <в какую валюту> <количество>\n"
        "Пример: рубль доллар 100\n"
        "Чтобы посмотреть список доступных валют: /values"
    )
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
	text = 'Доступные валюты: '
	for key in keys.keys():
		text = '\n'.join((text, key, ))
	bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
	try:
		values = message.text.split(' ')
		if len(values) != 3:
			raise ConvertionException('Неверное количество параметров.')
		
		quots, base, amont = values

		total_base = CryptoConverter.convert(quots, base, amont)

	except ConvertionException as e:
		bot.reply_to(message, f'Ошибка пользователя \n {e}')
	except Exception as e:
		bot.reply_to(message, f'Не удалось обработать команду \n {e}')
	else:
		total_base = CryptoConverter.convert(quots, base, amont)
		text = f'Цена {amont} {quots} в {base} - {total_base}'
		bot.send_message(message.chat.id, text)
	
bot.infinity_polling()
