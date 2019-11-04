txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
t2 = list()
for word in words:
    t.append((len(word), word))
    t2.append(word)
t.sort(reverse=True)
print(t)
print(t2)
res = list()
for length, word in t:
    res.append(word)

print(res)