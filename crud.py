# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:36:44 2022

@author: Omotade
"""


from sqlalchemy.orm import sessionmaker
from tqdm.std import tqdm
from extract import extract_coindata
from models import Crypto
from config import engine, cloud_engine

coindata = extract_coindata()
Session = sessionmaker(bind=cloud_engine)

def load_data(data = coindata):
    s = Session()
    for coin in tqdm(data, desc="Inserting data into {} table".format(Crypto.__tablename__)):
        s.rollback()
        row = Crypto(**coin)
        s.add(row)
        s.commit()
    s.close()
    print('Batch Load Executed!!!')
        