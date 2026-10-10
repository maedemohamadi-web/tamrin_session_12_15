from person import *
from account import *

person1=Person("berke","sanjabi")
print(person1)
print(person1.name)
print(person1.family)
person1.save_it()

account_1=Account("2557",290000,"markazi",person1)
print(account_1)
account_1.bardasht()

account_2=Account("1234",340000,"valiasr",person1)
print(account_2)
account_2.variz()

check1=Check("2556",450000,"markazi",35,52,person1)
print(check1.amount)
print(check1.branch)
print(check1.end_num)
print(check1)

card1=Card("4321",2000000,"park lale",5892,person1)
print(card1)
card1.bardasht()
print(card1.branch)
print(card1.account_id)
print(card1.card_number)

saving1=Saving("5678",455000,"sarsabz",18,person1)
print(saving1)
print(saving1.branch)
saving1.bardasht()