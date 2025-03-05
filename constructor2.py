class Parent:
    def __init__(self, msg="Parent Constructor"):
        print(msg)

class Child(Parent):
    def __init__(self):
        super().__init__("Calling Parent Constructor from Child")
        print("Child Constructor Called")
obj = Child()
