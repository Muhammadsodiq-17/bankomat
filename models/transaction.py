from  models.base import BaseModel
from enum import Enum
class TransactionType (Enum):
   WITHDRAW = "withdraw"
   DEPOSIT  = "deposit"
   TRANSFER = "transfer"
   BALANCE  = "balance_check"





class Transaction(BaseModel):
    def __init__(self,account_id, amount,status="success",description="default",type=TransactionType.WITHDRAW):
        super().__init__()
        self.account_id=account_id
        self.type=type
        self.amount=amount
        self.status=status
        self.description=description

    def to_dict(self):
       data= super().to_dict()
       data.update({
           "account_id":self.account_id,
           "type":self.type.value,
           "amount":self.amount,
           "status":self.status,
           "description": self.description


       })
       return data