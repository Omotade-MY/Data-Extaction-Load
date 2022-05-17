# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:32:11 2022

@author: Omotade
"""
from sqlalchemy import create_engine
from models import Base

DATABASE_URI = "postgres+psycopg2://postgres:udkhul bisalaam@localhost:5432/Cryptocurrency"

engine = create_engine(DATABASE_URI)

def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
