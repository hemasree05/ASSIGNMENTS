class Parent:
    def __init__(self):
        self._protected_field = "Protected Data"

    def _protected_method(self):
        print("This is a Protected Method")


class SamePackage:
    def access_protected(self):
        obj = Parent()
        print("Accessing Protected Field in Same Package:", obj._protected_field)
        obj._protected_method()


class Child(Parent):
    def access_parent_protected(self):
        print("Accessing Protected Field from Child (Different Package Simulation):", self._protected_field)
        self._protected_method()


class DifferentPackage:
    def access_protected(self):
        obj = Parent()
        print("Accessing Protected Field from Different Package Simulation:", obj._protected_field)
        obj._protected_method()


if __name__ == "__main__":
    sp = SamePackage()
    sp.access_protected()

    c = Child()
    c.access_parent_protected()

    dp = DifferentPackage()
    dp.access_protected()
