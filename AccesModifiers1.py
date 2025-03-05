class Parent:
    def __init__(self):
        self.__private_field = "Private Data"

    def __private_method(self):
        print("This is a Private Method")

    def display_private(self):
        print("Accessing Private Field in Parent:", self.__private_field)
        self.__private_method()


class Child(Parent):
    def try_access_private(self):
        print("Cannot access private fields/methods from subclass")


if __name__ == "__main__":
    p = Parent()
    p.display_private()

    c = Child()
    c.try_access_private()
