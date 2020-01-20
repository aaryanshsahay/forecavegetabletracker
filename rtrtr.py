from bs4 import BeautifulSoup
import time
from smtplib import SMTP
import pandas as pd
import numpy as np
import requests
import re


def compare(rates, mrp):
    result="equal"
    if rates<mrp:
        result="Foreca is charging less "
    elif rates>mrp:
        result="Foreca is charging more"
    return result

table = pd.read_csv(r'C:\Users\sahay\Downloads\priceforeca1.csv')
df = pd.DataFrame(table, columns = ['vegetable','rates','URL'])
urls= df["URL"]
price=[]
for URL in urls:
    # Do the beautiful soup code to extract price here and append to price
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'}

    #def check_price
    page= requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.text,'html.parser')

    mrp_string = soup.select_one('#price tr').text
    actual_price_string = soup.select_one('td[data-qa="productPrice"]').text

    # converting the value of MRP to a float
    mrp = float(mrp_string.replace("MRP: Rs ",""))

    # converting string to float , same as above
    actual_price = float(actual_price_string.replace("Rs ",""))
    price.append(mrp)
    

df['mrp'] = price
df['index'] = df.apply(lambda x: compare(x['rates'], x['mrp']), axis=1)
df=df.drop(columns='mrp')  #You can delete the column later
print(df)
