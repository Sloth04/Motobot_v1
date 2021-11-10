from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    # tg_id = relationship('Users')
    tg_id = Column(Integer)
    data = Column(Integer)
    received = Column(String)

    def __init__(self, tg_id: int, data: int, received: str):
        self.tg_id = tg_id
        self.data = data
        self.received = received
