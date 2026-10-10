from person import *

class Account:
    def __init__(self,account_id:str,amount:int,branch:str,owner:Person):
        self.account_id=account_id
        self.amount=amount
        self.branch=branch
        self.owner=owner

    def bardasht(self):
        print("Mablagh bardasht shod!")

    def variz(self):
        print("Mablagh variz shod!")

    def __repr__(self):
        return f"Account({self.__dict__})"

class Check(Account):
    def __init__(self, account_id: str, amount: int, branch: str,start_num:int,end_num:int,owner:Person):
        self.account_id=account_id
        self.amount=amount
        self.branch=branch
        self.start_num=start_num
        self.end_num=end_num
        self.owner=owner
    
class Card(Account):
    def __init__(self, account_id: str, amount: int, branch: str,card_number:str,owner:Person):
        self.account_id=account_id
        self.amount=amount
        self.branch=branch
        self.card_number=card_number
        self.owner=owner

class Saving(Account):
    def __init__(self, account_id: str, amount: int, branch: str,benefit_percentage:int,owner:Person):
        self.account_id=account_id
        self.amount=amount
        self.branch=branch
        self.benefit_pct=benefit_percentage
        self.owner=owner
    