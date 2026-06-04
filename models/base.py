from  datetime  import  datetime
import  uuid

class BaseModel:
    def __init__(self):
        self.id=str(uuid.uuid4())
        self.created_at=datetime.now()
        self.update_at=datetime.now()
    def update(self):
        self.update_at=datetime.now()
    def to_dict(self):
        return {
            "id": self.id,
            "created_at": str(self.created_at),
            "update": str(self.update_at)
        }
