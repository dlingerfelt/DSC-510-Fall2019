import requests
import json

url = 'https://w3schools.com/python/demopage.php'

# demonstrate how to use the 'params' parameter:
response = requests.get(url)

if response.status_code != 200:
    print('Error requesting Get ' + str(response.status_code))
    exit(response.status_code)
else:
    print('Success in getting web service ' + str(response.status_code))

print(response.text)
print(response.json())

# current_reply = json.loads(response.json())
