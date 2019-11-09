class Shark:
    # Class Variables
    animal_type = "fish"
    location = "ocean"
    followers = "5"

    # Constructor method with instance variables name , and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        self.followers = followers
        print('This shark has ' + str(followers) + ' followers')


new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)
print(new_shark.animal_type)
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)
new_shark.set_followers(77)
print(new_shark.followers)
