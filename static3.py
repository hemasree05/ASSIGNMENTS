class MyClass:
    static_var = 10 
obj = MyClass()
obj.static_var = 20  
print("Instance variable:", obj.static_var)
print("Class variable:", MyClass.static_var)
