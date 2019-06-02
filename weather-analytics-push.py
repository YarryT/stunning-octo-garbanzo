import pyowm
import requests
import time
owm = pyowm.OWM('0cfd27a64b52acac21747f6a2fa001b1')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
# while True:
observation = owm.weather_at_place('Glasgow,GB')
w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,

w.get_wind()
w.get_humidity()
temperature = w.get_temperature('celsius')
temperature_current = temperature['temp']

wing = str(w)
weather_list = wing.split(",")

basic_weather = weather_list[1].replace("status=","").strip()
detailed_weather = weather_list[2].replace("detailed status=","").rstrip('>').strip()

# print("The weather in Glasgow is"+detailed_weather+", and the temperature is currently "+str(temperature['temp'])+" degrees celsius.")

request = requests.get('https://www.google-analytics.com/collect?v=1&t=event&tid=UA-38347511-1&cid=7ee1a230-f784-44ea-8ad8-7c31bb0dd086&ec=weather&ea=update&el='+basic_weather+', '+detailed_weather)
request = requests.get('https://www.google-analytics.com/collect?v=1&t=event&tid=UA-38347511-1&cid=7ee1a230-f784-44ea-8ad8-7c31bb0dd086&ec=temperature&ea=update&el='+str(round(temperature_current))+' Degrees Celsius')
# time.sleep(3600)
