class Example:
    def __init__(self):  
        print("Public Constructor Called")

    def _protected_init(self):  
        print("Protected Constructor Called")

    def __private_init(self): 
        print("Private Constructor Called")

obj = Example()
obj._protected_init() 
