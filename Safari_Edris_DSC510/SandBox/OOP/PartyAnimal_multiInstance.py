class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, ' Constructed')

    def __del__(self):
        print(self.x, self.name, ' Destructed ')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far :', self.x)


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, " points ", self.points)


sally = PartyAnimal('Sally')
sally.party()
jim = CricketFan('Jim')
jim.party()
jim.six()
jim.six()