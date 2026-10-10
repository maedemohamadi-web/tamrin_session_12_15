class Person:
    def __init__(self,name,family):
        self.name=name
        self.family=family

    def save_it(self):
        print("SAVED!")

    def __repr__(self):
        return f"Person({self.__dict__})"