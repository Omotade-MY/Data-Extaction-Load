# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:32:11 2022

@author: Omotade
"""
from sqlalchemy import create_engine
from models import Base

LOCAL_DATABASE_URL = "postgres+psycopg2://postgres:udkhulbisalaam@localhost:5432/Cryptocurrency"

hostname = "borderless-instance.cyjsfpjxjrtj.us-east-1.rds.amazonaws.com"
password = "udkhulbisalaam"

CLOUD_DATABASE_URL = "postgres+psycopg2://postgres:"+password+"@"+hostname+":5432/Cryptocurrency"

engine = create_engine(LOCAL_DATABASE_URL)
cloud_engine = create_engine(CLOUD_DATABASE_URL)

def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
