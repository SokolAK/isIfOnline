import requests

TELEGRAM_BOT_TOKEN = '5525701166:AAGUZcYISfLyJiRs-EcwUeAnz6ZRN0Up-yY'
params = {
    'chat_id': '-615666237',
    'text': 'elo'
}
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
r = requests.post(url, params=params)
