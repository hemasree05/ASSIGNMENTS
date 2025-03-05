try:
    with open("testfile.txt", "w") as file:
        file.write("Hello")
    with open("testfile.txt", "r") as file:
        file.write("Trying to write in read mode")  # This raises an error
except OSError as e:
    print("IOException occurred:", e)
