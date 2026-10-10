class Lesson:
    def __init__(self, title, teacher, code, unit):
        self.title = title
        self.teacher = teacher
        self.code = code
        self.unit = unit

    def add_lesson(self):
        print("Lesson added successfully")

    def __repr__(self):
        return f"Person({self.__dict__})"

lesson1=Lesson("python","mesbah","381841",3)
lesson1.add_lesson()
print(lesson1)