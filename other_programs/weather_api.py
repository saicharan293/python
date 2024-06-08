import requests

city=input("Enter your city name: ")
url='http://api.weatherapi.com/v1/current.json?key=4aa985932efe46b7ba093212241302&q='+city+'&aqi=no'
response=requests.get(url)

weather_json=response.json()

temp=weather_json.get('current').get('temp_c')
description=weather_json.get('current').get('condition').get('text')
# print(temp)
print('Your city',city,'has',description,'weather with',temp,'degrees temperature')