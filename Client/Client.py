# coding=utf-8
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from dataBase import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    relationship("Transaction", back_populates="client")
    name = Column(String(50))
    surname = Column(String(50))
    document_number = Column(String)
    phone = Column(String(12))
    street = Column(String(70))
    city = Column(String(50))
    post_code = Column (String(6))