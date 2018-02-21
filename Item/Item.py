# coding=utf-8
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean

from dataBase import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    id_transaction = Column(Integer, ForeignKey('transaction.id'))
    name = Column(String)
    barcode = Column(String)
    is_lent = Column(Boolean)
    store = Column(Integer, ForeignKey('store.id'))

    def __init__(self, id_transaction, name, barcode, store):
        self.id_transaction = id_transaction
        self.name = name
        self.barcode = barcode
        self.store = store
        self.is_lent = False
