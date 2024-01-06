class Product:
    def __init__(self, car: str) -> None:
        self.car = car

    def manufacturer(self, name: str):
        self.car = self.car + " " + name
        return self

    def model(self, choice: str):
        self.car = self.car + " " + choice
        return self

    def climate(self, choice: int):
        if choice == 1:
            self.car = self.car + " " + "Climate"
        return self

    def radio(self, choice: int):
        if choice == 1:
            self.car = self.car + " " + "Radio"
        return self

    def color(self, choice: str):
        self.car = self.car + " " + choice
        return self


print(Product("Car 1").manufacturer("BMW").model("118i").color("Red").climate(1).car)
print(Product("Car 2").manufacturer("VW").model("Golf").color("White").climate(0).car)
