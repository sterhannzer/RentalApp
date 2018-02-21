# coding=utf-8
from sqlalchemy import Column, Integer, Date, Float, ForeignKey

from dataBase import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    data_begin = Column(Date)
    date_end = Column(Date)
    price = Column(Float)
    client_id = Column(Integer, ForeignKey('client.id'))
    employee = Column(Integer, ForeignKey('user.id'))

    def __init__(self, date_begin, date_end, price, client_id, employee):
        self.date_begin = date_begin
        self.date_end = date_end
        self.price = price
        self.client_id = client_id
        self.employee = employee