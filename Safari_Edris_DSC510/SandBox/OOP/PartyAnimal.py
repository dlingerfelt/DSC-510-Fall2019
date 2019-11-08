class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def __del__(self):
        print('I am destrcuted ', self.x)

    def party(self):
        self.x = self.x + 1
        print('So far :', self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
an = 42
print('an contains', an)
an.party()
