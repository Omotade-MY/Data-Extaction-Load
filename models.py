# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:29:48 2022

@author: Omotade
"""


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Crypto(Base):
    __tablename__ = 'CryptoPrice'
    id = Column(Integer, primary_key=True)
    CoinName = Column(String)
    Coin = Column(String)
    Time = Column(DateTime)
    Price = Column(String)
    Website = Column(String)
    
    def __repr__(self):
        return "Crypto(CoinName: {}, Coin: {}, Time: {}, Price: {}, Website: {})"\
        .format(self.CoinName, self.Coin, self.Time, self.Price, self.Website)
    
