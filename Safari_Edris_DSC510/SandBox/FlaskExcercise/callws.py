import requests
import json

employees = requests.get(' http://127.0.0.1:5002/employees')
print(employees.json())
print(employees.json()['employees'])

employees_name = requests.get(' http://127.0.0.1:5002/employees/1')
print(employees_name.json())


tracks = requests.get(' http://127.0.0.1:5002/tracks')
print(tracks.json()['data'])
print(tracks.json()['data'][0]['Composer'])
