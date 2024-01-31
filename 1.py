import requests
import json

r = requests.get('https://api.gwent.one/?key=data&version=11.7')
data = json.loads(r.text)

print(data['response']['0']['name'])
