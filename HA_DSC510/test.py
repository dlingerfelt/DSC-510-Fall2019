import requests

# r = requests.get('https://api.github.com/events')
# print(r.text)


r = requests.post('https://httpbin.org/post', data={'First name': 'James',
                                                    'Last name': 'Ha',
                                                    'Phone': ['999-999-9999', '000-000-0000']})
print(r.text)

r = requests.delete('https://httpbin.org/delete')
print(r.text)

r = requests.get('https://httpbin.org/get')
print(r.text)

r = requests.options('https://httpbin.org/get')
print(r.text)

