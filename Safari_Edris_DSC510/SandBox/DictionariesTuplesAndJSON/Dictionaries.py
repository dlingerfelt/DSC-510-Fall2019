eng2sp = dict()
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {' one': 'uno', 'two': 'dos', 'three': 'tres'}

print(eng2sp)
print(eng2sp['two'])
try:
    print(eng2sp['four'])
except:
    print("oops!")

if 'one' in eng2sp:
    print("yes")
else:
    print("No")

eng2sp = {'word1': 5, 'word2': 3, 'word3': 5}
print(eng2sp)
print(eng2sp['word1'])
eng2sp['word1'] = eng2sp.get('word1',0) + 1
print(eng2sp)
print(eng2sp['word1'])

sentence = "You could create a dictionary with characters as keys and counters as the corresponding values. The first time you see a character, you would add an item to the dictionary. After that you would increment the value of an existing item."
print(sentence)