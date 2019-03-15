from django.shortcuts import render
import requests
import json

def home(request):
	news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	data = json.loads(news_request.content)
	return render(request, 'cryptonews/home.html', {'request': data})
