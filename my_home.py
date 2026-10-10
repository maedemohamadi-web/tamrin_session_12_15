class Home:
    def __init__(self,address,owner,number_of_rooms,parking):
        self.address = address
        self.owner = owner
        self.number_of_rooms = number_of_rooms
        self.parking = parking

    def add_home(self):
        print("Home Added")

    def __repr__(self):
        return f"Person({self.__dict__})"

my_home=Home("resalat","bahari",2,"yes")
my_home.add_home()
print(my_home)