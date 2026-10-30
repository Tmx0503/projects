class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model}")

    def stop(self):
        print(f"stop the {self.model}")

car1 = Car("C8", 2008, "black", False)
# ha megpróbáljuk printelni akkor a memory adresset kapjuk meg ahol a car object located
car2 = Car("corvette,", 2008, "black", False )
print(car1.model) # pont kell és aztán mit akarsz

car1.drive()


#object oriented programming








