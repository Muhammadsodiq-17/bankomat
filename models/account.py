from models.base import BaseModel



class  Account(BaseModel):
    def __init__(self, card_id,balance=0,currency="UZS"):
        super().__init__()
        self.card_id=card_id
        self.balance=balance
        self.currency=currency
    def deposit(self,amount):
        if amount<0:
           raise ValueError("Xato!")
        else:
           self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Xato!")
        else:
            self.balance-=amount
    def to_dict(self):
        data=super().to_dict()
        data.update({
        "card_id": self.card_id,
        "balance": self.balance,
        "currency": self.currency
        })
        return  data

