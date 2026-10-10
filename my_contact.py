class Contact:
    def __init__(self,name,last_name,phone_number,title):
        self.name=name
        self.last_name=last_name
        self.phone_number=phone_number
        self.title=title

    def add_contact(self):
        print("Contact Added!")

    def __repr__(self):
        return f"Contact({self.__dict__})"

my_contact=Contact("berke","mirzai","09912305265","mobile_number")
my_contact.add_contact()
print(my_contact)