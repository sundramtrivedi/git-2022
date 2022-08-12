import requests
import json

URL = 'https://sleepy-island-07017.herokuapp.com/sensor'
data = open('app.env','r')
lines = list(data)
data.close()
Line1 = lines[0].split('=')
Line2 = lines[1].split('=')

API_KEY = Line1[1].replace('\n','')
TOKEN = Line2[1].replace('\n','')

if __name__ == "__main__":
	body =  { 
			"API_KEY" : API_KEY,
			"type" : "Kitchen",
			"tag" : "STM32",
			"value" : 20,
			"unit" : "C"
		}

def sendRequest(body):
	body['API_KEY'] = API_KEY
	payload = json.dumps(body)
	auth = {'Content-Type':'application/json','Authorization':'Bearer '+TOKEN}
	result = requests.post(URL,data=payload,headers=auth)
	print(result)


sendRequest(body)
