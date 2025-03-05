class Example:
    def show(self, a, b=None):
        if b is None:
            print(f"One Parameter: {a}")
        else:
            print(f"Two Parameters: {a}, {b}")

obj = Example()
obj.show(10)        
obj.show(10, 20) 
