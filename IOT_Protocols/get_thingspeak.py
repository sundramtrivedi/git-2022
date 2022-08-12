import requests
import json
URL = 'https://api.thingspeak.com/update'
data = open('app.env1','r')
lines = list(data)
data.close()
Line1 = lines[0].split('=')
Line2 = lines[1].split('=')

api_key = Line1[1].replace('\n','')
field1 = Line2[1].replace('\n','')

auth = {'Content-Type':'application/json','Authorization':'Bearer '+field1}
result = requests.get(URL,headers=auth)
print(json.loads(result.content))

requests.get('https://api.thingspeak.com/update', params=payload)
