"""
Gaikwad411 Greet

"""


def greet():
    return 'Hello World!'


def main():  # type: () -> None
    """Calls greet function"""
    print('*'*100)
    print(greet())
    print('*' * 100)


if __name__ == "__main__":
    main()
