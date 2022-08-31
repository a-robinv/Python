import requests
baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
# lat = '14.6442597'
# lon = '120.9698528'
# appid = 'e80e8ce1d52b14f5bcebf62de5ac430a'
parameters = {'lat':'14','lon':'120','appid':'e80e8ce1d52b14f5bcebf62de5ac430a'}
response = requests.get(baseUrl, params=parameters)
print(response.content)