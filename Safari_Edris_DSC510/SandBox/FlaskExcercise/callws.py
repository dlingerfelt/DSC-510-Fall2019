import requests
import json

employees = requests.get(' http://127.0.0.1:5002/employees')
print(employees.json())
print(employees.json()['employees'])
js = ''' + employees.json() + '''
data = json.loads(js)

tracks = requests.get(' http://127.0.0.1:5002/tracks')
print(tracks.json()['data'][0]['Composer'])
