from models.base import BaseModel
import  bcrypt
class Card(BaseModel):
     def __init__(self,card_number,pin,user_id,failed_attempts=0,is_blocked=False):

         super().__init__()
         self.card_number=card_number
         self.__pin=None
         self.user_id=user_id
         self.is_blocked=is_blocked
         self.failed_attempts=failed_attempts

     def set_pin(self,pin):
         self.__pin=bcrypt.hashpw(
             pin.encode('utf-8'),
             bcrypt.gensalt()
         )
     def verify_pin(self,pin):
         return bcrypt.checkpw(
             pin.encode('utf-8'),
             self.__pin

         )

     def to_dict(self):
         data = super().to_dict()
         data.update ({
            "card_number": self.card_number,
            "user_id": self.user_id,
            "is_blocked": self.is_blocked,
            "failed_attempts": self.failed_attempts
         })
         return data
