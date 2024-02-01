import requests
import json

r = requests.get('https://api.gwent.one/?key=data&version=11.7')
data = json.loads(r.text)
for elem in data['response']:
    for atr in ['id', 'attributes', 'name', 'category', 'ability', 'ability', 'ability_html', 'keyword_html', 'flavor']:
        print(data['response'][elem][atr])
    print()
