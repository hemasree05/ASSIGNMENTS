
class A:
    def __init__(self):
        self.value = "Value from Class A"

    def methodA1(self):
        print("Method A1: Specific to Class A")

    def methodA2(self):
        print("Method A2: Specific to Class A")

    def show(self):
        print("Overridden Method in Class A")


class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class B"

    def methodB1(self):
        print("Method B1: Specific to Class B")

    def methodB2(self):
        print("Method B2: Specific to Class B")

    def show(self):
        print("Overridden Method in Class B")


class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class C"

    def methodC1(self):
        print("Method C1: Specific to Class C")

    def methodC2(self):
        print("Method C2: Specific to Class C")

    def show(self):
        print("Overridden Method in Class C")


if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()

    print("\nCalling methods using individual objects:")
    objA.methodA1()
    objA.methodA2()
    objA.show()
    
    objB.methodA1()
    objB.methodA2()
    objB.methodB1()
    objB.methodB2()
    objB.show()
    
    objC.methodA1()
    objC.methodA2()
    objC.methodB1()
    objC.methodB2()
    objC.methodC1()
    objC.methodC2()
    objC.show()

    print("\nCalling overridden method using superclass reference:")
    ref1 = A()
    ref2 = B()
    ref3 = C()
    
    ref1.show()
    ref2.show()
    ref3.show()

    print("\nRuntime Polymorphism with Data Members:")
    refA = A()
    refB = B()
    refC = C()

    print(refA.value)
    print(refB.value)
    print(refC.value)
