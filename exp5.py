def check_number(num):
    if num < 0:
        raise ValueError("Number cannot be negative!")

try:
    check_number(-5)
except ValueError as e:
    print("Error:", e)
