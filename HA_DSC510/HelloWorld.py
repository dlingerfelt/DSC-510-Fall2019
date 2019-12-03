class HelloWorld:
    def __init__(self):
        self.text = "Hello World!"

    def sayIt(self):
        print(self.text)


if __name__ == '__main__':
    speak = HelloWorld()
    speak.sayIt()
