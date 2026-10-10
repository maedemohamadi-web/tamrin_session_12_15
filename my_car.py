class Car:
    def __init__(self,name,color,plate):
        self.name=name
        self.color=color
        self.plate=plate

    def add_car(self):
        print("Car Added!!!")

    def __repr__(self):
        return f"Car(name={self.name}, color={self.color}, plate={self.plate})"

car1=Car("volks wagen","red",6768)
car1.add_car()
print(car1)