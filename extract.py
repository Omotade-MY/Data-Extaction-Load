# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:54:44 2022

@author: Omotade
"""
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrape():
    data = requests.get('https://coinmarketcap.com/all/views/all/')
    soup = BeautifulSoup(data.content, 'html.parser')
    
    return soup

def extract_coindata():
    """Extracts the current price, 24thVolume and MarketCap
    returns a list of dictionaries where each dictionary is for each coin"""

    # srape data from website
    cryptosoup = scrape()
    
    # get current time after scraping
    now = datetime.now()
    
    # collecting infomation needed from webpage
    table = cryptosoup.select('table')[2]
    headpane = table.select('thead')[0]
    body = table.select('tbody')[0]
    columns = []
    
    coin_info = []
    heads = headpane.select('th')[1:-1]
    for head in heads:
        if heads.index(head) == 0:
            col = 'CoinName'
        else:
            col = head.text.strip('% ')
        columns.append(col)
    
    # select top 5 rows

    rows = body.select('tr')[:5]
    for r in rows:
        row_vals = []
        
        row =  r.select('td')[1:-1]
        
        for i in range(len(row)):
            val = row[i]
            if i == 0:
                val = val.select('a')[1].text
            elif i == 2:
                val = val.text.split('B')[1]
            else:
                val = val.text
            col = columns[i]
    
            
            row_vals.append(val)
        time = now.strftime('%Y/%m/%d %H:%M')
        
        # save the time and website of scraping
        row_vals.insert(2,time)
        row_vals.append('https://coinmarketcap.com/all/views/all/')
        info = tuple(row_vals)
        coin_info.append(info)
        
    columns.insert(2,'Time')
    columns.append('Website')
    
    return coin_info, columns


def to_csv(coindata, columns):
    
    n = datetime.now()
    n = n.strftime('%H-%M')
    try:
        os.mkdir('{}'.format(n))
    except FileExistsError:
        pass
    
    path = './'+ n + '/cryptocurrency.csv'
    pd.DataFrame(coindata, columns=columns).to_csv(path, index=False)
