n= input("Enter a number or string: ")

if n==n[::-1]: #slicing
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
