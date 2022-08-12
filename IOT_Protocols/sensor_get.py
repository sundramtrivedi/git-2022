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

 


auth = {'Content-Type':'application/json','Authorization':'Bearer '+TOKEN}
result = requests.get(URL,headers=auth)
print(json.loads(result.content))
 



