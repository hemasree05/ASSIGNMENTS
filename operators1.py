def arithmetic_operations(a, b):
    # Addition
    addition = a + b
    print(f"Addition ({a} + {b}) = {addition}")

    # Subtraction
    subtraction = a - b
    print(f"Subtraction ({a} - {b}) = {subtraction}")

    # Multiplication
    multiplication = a * b
    print(f"Multiplication ({a} * {b}) = {multiplication}")

    # Division
    if b != 0:  # Check to avoid division by zero
        division = a / b
        print(f"Division ({a} / {b}) = {division}")
    else:
        print("Division by zero is not allowed.")

# Example usage
arithmetic_operations(10, 5)
