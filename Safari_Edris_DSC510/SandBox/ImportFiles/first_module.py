


def main():
    print("First Module's name: {}".format(__name__))


if __name__ == '__main__':
    main()
else:
    print("This Module's name is :" + __name__)
