class Lesson:
    def __init__(self,code,name, unit):
        self.__code = code
        self.name = name
        self.unit = unit

    def add_lesson(self):
        print("Lesson added successfully")

    def get_code(self):
        print("code getter")
        return self.__code

    code = property(get_code)

    def get_unit(self):
        print("unit getter")
        return self.__unit

    def set_unit(self,new_unit):
        print("unit setter")
        if isinstance(new_unit,int) and new_unit in[1,2,3,5]:
            self.__unit = new_unit
        else:
            print("Invalid unit")

    unit=property(get_unit,set_unit)

    def __repr__(self):
        return f"Person({self.__dict__})"

lesson1=Lesson(381841,"python",3)
#lesson1.add_lesson()
print(lesson1.unit)
lesson1.unit=2
print(lesson1)
print(lesson1.code)