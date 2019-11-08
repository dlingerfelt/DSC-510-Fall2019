import json
import requests

from urllib.request import urlopen
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "562-542-5689",
            "emails": ["abd@email1.com","abs@email2.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "985-568-4715",
            "emails": ["jane@email1.com", "ajd@email2.com"],
            "has_license": true
        }
    ]
} '''
data = json.loads(people_string)
print(data)

response = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrentcies/quote?format=jason")


print(response)
