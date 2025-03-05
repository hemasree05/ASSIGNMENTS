try:
    print(10 / 2)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always executes, whether an exception occurs or not.")
