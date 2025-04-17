import requests
import json
from config import keys, TOKEN

class ConvertionException(Exception):
	pass

class CryptoConverter:
	@staticmethod
	def convert(quots: str, base: str, amont: str):
		if quots == base:
			raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
		
		try:
			quote_tickers = keys[quots]
		except KeyError:
			raise ConvertionException(f'Не удалось обработать валюту {quots}')
		
		try:
			base_ticker = keys[base]
		except KeyError:
			raise ConvertionException(f'Не удалось обработать валюту {quots}')
		
		try:
			amont = float(amont)
		except ValueError:
			raise ConvertionException(f'Не удалось обработать количество {amont}')
		
		r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tickers}&tsyms={base_ticker}')
		rate = json.loads(r.content)[base_ticker]
		total = rate * amont
		return round(total, 2)
