# Defining a global variable
x = "Global Variable"

def ex_func():
    # Defining a local variable with the same name
    x = "Local Variable"
    print("Inside the function, x is:", x)  # This will print the local variable

# Calling the function
ex_func()

# Printing the global variable
print("Outside the function, x is:", x)  # This will print the global variable
