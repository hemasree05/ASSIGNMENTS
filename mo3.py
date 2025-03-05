class Example:
    def test(self, *args):
        print(f"Method with {len(args)} arguments: {args}")

obj = Example()
obj.test(10, 20) 
