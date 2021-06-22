# -*- coding: utf-8 -*-
"""Weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMcHHH_O6fp0aWHBoL0XC9TJo_suynB7
"""

import requests

from datetime import datetime

api_key='40afd6c2a4afaad467fe27febe48f6c3'
location=input("Enter the city name: ")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp']) -273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wnd_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("--------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))
print("---------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity      :",humdt, '%')
print("Current wind speed    :",wind_spd,'kmph')