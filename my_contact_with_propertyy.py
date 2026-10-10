from persian_tools import phone_number

class Contact:
    def __init__(self,name,last_name,phone_number,title):
        self.name=name
        self.last_name=last_name
        self.__phone_number=phone_number
        self.title=title

    def add_contact(self):
        print("Contact Added!")

    def get_phone_number(self):
        print(" Getter!")
        return self.__phone_number

    def set_new_phone_number(self,new_phone_number):
        print(" Setter!")
        if isinstance(new_phone_number,str) and phone_number.validate(new_phone_number):
            self.__phone_number=new_phone_number
        else:
            print("Invalid phone number!")

    phone_number=property(get_phone_number,set_new_phone_number)

    def __repr__(self):
        return f"Contact({self.__dict__})"

my_contact=Contact("berke","mirzai","09912305265","mobile_number")
my_contact.add_contact()
print(my_contact)
#print(my_contact.get_phone_number())
#my_contact.set_new_phone_number("09191023192")
#print(my_contact)
print(my_contact.phone_number)
my_contact.phone_number="09128045794"
print(my_contact)