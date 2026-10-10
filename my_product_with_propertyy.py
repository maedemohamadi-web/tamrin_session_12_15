class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def add_product(self):
        print("Product added successfully")

    def __repr__(self):
        return f"Product(name={self.name}, price={self.__price})"

    def get_product_price(self):
        print ("GET")
        return self.__price

    def set_new_price(self,new_price):
        print("SET")
        if isinstance(new_price,int)and new_price>0:
           self.__price = new_price
        else:
            print("Invalid price!")

    price=property(get_product_price,set_new_price)

product1=Product("Laptop",100000000)
product1.add_product()
print(product1)
#print(product1.get_product_price())
#product1.set_new_price(100)
#print(product1)
print(product1.price)
product1.price=50000000
print(product1.price)
print (product1)
#print(product1.__dict__)