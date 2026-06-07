from models.base import BaseModel


class User(BaseModel):
    def __init__(self,first_name,last_name,phone_number,is_active=True):
        super().__init__()
        self.first_name=first_name
        self.last_name=last_name
        self.is_active=is_active
        self.phone_number=phone_number

    def to_dict(self):
        data=super().to_dict()
        data.update({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "is_active": self.is_active

        })
        return data
