class Parent:
    def __init__(self):
        self.public_field = "Public Data"

    def public_method(self):
        print("This is a Public Method")


class SamePackage:
    def access_public(self):
        obj = Parent()
        print("Accessing Public Field in Same Package:", obj.public_field)
        obj.public_method()


class Child(Parent):
    def access_parent_public(self):
        print("Accessing Public Field from Child (Different Package Simulation):", self.public_field)
        self.public_method()


class DifferentPackage:
    def access_public(self):
        obj = Parent()
        print("Accessing Public Field from Different Package Simulation:", obj.public_field)
        obj.public_method()


if __name__ == "__main__":
    sp = SamePackage()
    sp.access_public()

    c = Child()
    c.access_parent_public()

    dp = DifferentPackage()
    dp.access_public()
