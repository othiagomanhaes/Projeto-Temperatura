import requests
import json


lat = float(input('Diga-me sua Latitude: '))
lon = float(input('Diga-me sua Longittude: '))
APIkey = '0171b43cbe89768af1f26188e66bea16'
temperatura = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}')
temperatura = temperatura.json()
print(f"{temperatura['name']} = {(temperatura['main']['temp'] - 273.15):.2f}ºC")
