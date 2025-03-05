data = b"Hello, this is binary data!"
with open("binary_file.bin", "wb") as file:
    file.write(data)
