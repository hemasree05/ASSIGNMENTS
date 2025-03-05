class Example:
    def display(self, a):
        if isinstance(a, int):
            print(f"Integer Parameter: {a}")
        elif isinstance(a, str):
            print(f"String Parameter: {a}")

obj = Example()
obj.display(100)       
obj.display("Hello") 
