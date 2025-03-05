def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero!")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Exception caught:", e)
