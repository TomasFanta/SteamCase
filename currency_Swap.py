import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
today = date.today()
currency = yf.download('USDEUR=X',start=today)
excel1 = pd.read_excel("data/data.xlsx",index_col=0)
excel2 = pd.read_excel("data/data2.xlsx",index_col=0)
excel = pd.concat([excel1,excel2])

currency = currency.reset_index()
excel["Price_$"] = excel["Price_$"].str[1:5]
temp =[]

for i,n in excel.iterrows():
    temp.append((float(n["Price_$"])*currency["Adj Close"].values).round(2).item())

excel["Price_€"]= temp

excel.to_excel("excel.xlsx", engine='xlsxwriter')
