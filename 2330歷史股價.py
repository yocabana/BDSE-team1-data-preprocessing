# -*- coding: utf-8 -*-
"""[爬蟲]2330歷史股價.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qES00tnKdH4ubffHNyI40t2gtKFtNWCm
"""

!pip install yfinance
!pip install h5py
import yfinance as yf
import h5py
import pandas as pd

stock_id = '2317.TW'
data = yf.Ticker(stock_id)
df = data.history(start="2018-01-01", end="2021-09-30")

df=df.drop(columns=['Dividends','Stock Splits'])

df=df.rename(columns={'Open':'開盤價','High':'最高價','Low':'最低價','Close':'收盤價'})

from google.colab import drive
drive.mount('/content/drive')

df.to_csv('/content/drive/MyDrive/chinese_sent_data/2317_price.csv')

