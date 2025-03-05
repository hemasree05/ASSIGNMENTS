class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self.model = model 
        self.year = year    

    def display(self):
        print(f"Car Details: {self.brand} {self.model}, Year: {self.year}")
my_car = Car("Toyota", "Corolla", 2022)
my_car.display()
