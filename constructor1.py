class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One Argument Constructor Called: {arg1}")
        else:
            print(f"Two Argument Constructor Called: {arg1}, {arg2}")
obj1 = MyClass()
obj2 = MyClass("Hello")
obj3 = MyClass("Hello", "World")
