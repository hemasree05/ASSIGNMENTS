n = int(input("Enter a number: "))
temp = n
d = 0
while n > 0:
    n //= 10
    d += 1
n = temp
sum = 0
while n > 0:
    digit = n % 10
    sum += digit ** d
    n //= 10

if sum == temp:
    print(f"{temp} is an Armstrong number.")
else:
    print(f"{temp} is not an Armstrong number.")
