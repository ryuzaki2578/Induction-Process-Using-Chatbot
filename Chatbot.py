## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
bot_message=""
while bot_message !="Bye":
    message =input("")
    r= requests.post('http://localhost:5002/webhooks/rest/webhook',json={"message":message})
    for i in r.json():
        bot_message=i['text']
        print(f"{i['text']}")
