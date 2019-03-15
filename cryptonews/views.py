from django.shortcuts import render
import requests
import json

def home(request):
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	data = json.loads(news_request.content)
	return render(request, 'cryptonews/home.html', {'request': data})


def costs(request):
	if request.method == 'POST':
		crypto = request.POST['crypto']
		crypto = crypto.upper() 
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + crypto + "&tsyms=USD")
		data = json.loads(crypto_request.content)
		return render(request, 'cryptonews/costs.html', {'request': data})
	else:
		price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
		price = json.loads(price_request.content)
		return render(request, 'cryptonews/costs.html', {'price': price})

