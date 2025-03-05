def even_odd(num):
    switch = {
        0: "EVEN",
        1: "ODD"
    }
    return switch[num % 2]

num = int(input("Enter a number: "))
print(f"The number is {even_odd(num)}")
