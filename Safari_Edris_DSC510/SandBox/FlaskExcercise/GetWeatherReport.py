import requests
import json

#weather_report = requests.get(' http://127.0.0.1:5009/78133')
#print(weather_report.json())
hello_world = requests.get('http://127.0.0.1:5001/')
print(hello_world)