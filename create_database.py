from models.database import create_db
from models.data import Data  # Do not import if you not use
from models.users import Users


def create_database():
    create_db()
# Why this file exist? It consist from 1 function that call other function.
# May be better call create_db() i target place?
