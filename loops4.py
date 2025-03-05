s = int(input("Enter the starting number: "))
e = int(input("Enter the ending number: "))

for num in range(s, e + 1):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
