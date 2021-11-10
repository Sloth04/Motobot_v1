from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_user_id = Column(Integer)
    # tg_user_id = Column(Integer, ForeignKey('data.tg_id'))
    user_nickname = Column(String)
    user_lastname = Column(String)

    def __init__(self, tg_user_id: int, user_nickname: str, user_lastname: str):
        self.tg_user_id = tg_user_id
        self.user_nickname = user_nickname
        self.user_lastname = user_lastname

    def __repr__(self):
        info: str = f'Пользователь [Идентификатор Tg: {self.tg_user_id},' \
                    f'Имя: {self.user_nickname}, Фамилия: {self.user_lastname}]'
        return info
