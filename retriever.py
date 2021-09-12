import dweepy
import time
from slack_sdk.webhook import WebhookClient
import utils


def get_values(thing, t, h):
	url = dweepy.get_latest_dweet_for(thing)
	dict = url[0]
	utils.insert_valor(thing, dict['content'][str(t)], dict['content'][str(h)])

def make_calls_thecore(thing, t, h):
	get_values(thing, t, h)
	time.sleep(60)

def get_all_values():
	res = utils.get_all()
	url = "https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9"
	webhook = WebhookClient(url)
	response = webhook.send(text=res)
	assert response.status_code == 200
	#print("all values", res)

values = lambda thing, t, h: [make_calls_thecore(thing, t, h) if i < 15 else get_all_values() for i in range(16)]

values("thecore", 'temperature', 'humidity')

