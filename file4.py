with open("sample.txt", "rb") as file:
    file.seek(10)  # Move to the 10th byte
    print(file.read(5))
