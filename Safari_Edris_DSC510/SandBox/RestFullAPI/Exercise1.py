import requests

#r1 = requests.get('https://xkcd.com/353/')
#r2 = requests.get('https://api.chucknorris.io/jokes/random')
#r3 = requests.get('https://imgs.xkcd.com/comics/python.png')
#r4 = requests.get('https://httpbin.org/get')
r4 = requests.get("http://127.0.0.1:5002/get")
#print(r1.headers)
#print(r2.text)
#print(r3.headers)
print(r4.text)
