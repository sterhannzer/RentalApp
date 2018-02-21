# coding=utf-8
from sqlalchemy import Column, String, Integer
import sys
sys.path.insert(0, '/Users/lukasz/Documents/RentalApp/RentalApp/dataBase.py')

import dataBase


class Store(dataBase.Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name


