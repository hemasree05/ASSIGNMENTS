with open("sample.txt", "r") as file:
    file.seek(5)  
    print(file.read(10)) 
