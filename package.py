class ClassOne:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Hello from ClassOne! Name: {self.name}")

class ClassTwo:
    def __init__(self, age):
        self.age = age

    def display_age(self):
        print(f"Hello from ClassTwo! Age: {self.age}")

class PackageInit:
    @staticmethod
    def import_classes():
        return ClassOne, ClassTwo

ClassOne, ClassTwo = PackageInit.import_classes()

obj1 = ClassOne("Hema")
obj2 = ClassTwo(20)

obj1.display_name()
obj2.display_age()
