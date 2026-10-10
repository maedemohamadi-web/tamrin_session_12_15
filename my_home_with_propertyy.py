class Home:
    def __init__(self,address,owner,number_of_rooms,parking):
        self.__address = address
        self.owner = owner
        self.number_of_rooms = number_of_rooms
        self.parking = parking

    def add_home(self):
        print("Home Added")

    def get_address(self):
        print("GET")
        return self.__address

    def set_address(self, address):
        print("SET")
        if isinstance(address,str)and len(address)>0:
            self.__address = address
        else:
            print("Invalid address")

    address=property(get_address,set_address)

    def __repr__(self):
        return f"Person({self.__dict__})"

my_home=Home("resalat","bahari",2,"yes")
my_home.add_home()
print(my_home)
print(my_home.address)
my_home.address="vanak"
print(my_home)