import json
import requests
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup?'
parameters = {'upc': '786173903071'}
response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)