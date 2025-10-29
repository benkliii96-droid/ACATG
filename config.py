import requests
import json

values_ = {

}


TOKEN = "8231266170:AAFS9OD5rc04O4BqwYU5zVRaHmpSMO8nLus"
API_KEY = "575c79457fe7d66edb0b5830"
li = requests.get("https://v6.exchangerate-api.com/v6/575c79457fe7d66edb0b5830/latest/USD")
total = json.loads(li.content)
resp = total['conversion_rates']
for i in resp:
    values_[i] = i


