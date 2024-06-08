import requests

response=requests.get('http://api.open-notify.org/astros.json')
names_json=response.json()

# print(names_json)
for person in names_json['people']:
    print(person['name'])