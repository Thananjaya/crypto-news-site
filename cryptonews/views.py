from django.shortcuts import render
import requests
import json

def home(request):
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	data = json.loads(news_request.content)
	return render(request, 'cryptonews/home.html', {'request': data})


def costs(request):
	no_content = False
	if request.method == 'POST':
		crypto = request.POST['crypto']
		crypto = crypto.upper() 
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + crypto + "&tsyms=USD")
		data = json.loads(crypto_request.content)
		return render(request, 'cryptonews/costs.html', {'request': data, 'no_content': no_content})
	else:
		no_content = True
		return render(request, 'cryptonews/costs.html', {'no_content': no_content, 'message': 'Not found'})

