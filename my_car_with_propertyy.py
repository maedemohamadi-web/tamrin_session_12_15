class Car:
    def __init__(self,name,color,plate):
        self.name=name
        self.color=color
        self.__plate = plate

    def add_car(self):
        print("Car Added!!!")

    def get_plate(self):
        print("GET")
        return self.__plate

    def set_plate(self,plate):
        print("SET")
        if isinstance(plate,str):
            self.__plate=plate
        else:
            print("Invalid PLATE")
        #میخواستم از persian_toolsاستفاده کنم تا شماره پلاک معتبر باشه اما توی تست گرفتن چون شماره پلاک ها فارسیه و بهم میریزه به مشکل می خوردم

    plate=property(get_plate,set_plate)

    def __repr__(self):
        return f"Car(name={self.name}, color={self.color}, plate={self.__plate})"

car1=Car("volks wagen","red","6768")
print(car1.plate)
car1.plate="3489"
print(car1.plate)
print(car1)