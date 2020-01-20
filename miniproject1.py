from bs4 import BeautifulSoup
import time
from smtplib import SMTP
import pandas as pd
import numpy as np
import requests
import re


#links = {'Item':['Tomato','Potato','Onion'],'URL':['https://www.bigbasket.com/pd/10000200/fresho-tomato-hybrid-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop','https://www.bigbasket.com/pd/40023476/fresho-potato-organically-grown-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop','https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop']}
URL='https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/?nc=cl-prod-list&t_pg=&t_p=&t_s=cl-prod-list&t_pos=1&t_ch=desktop'

#df = pd.DataFrame(links,columns = ['Item','URL'])
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

#print("MRP: Rs", mrp)
print("Price: Rs", actual_price)
print("Price: Rs",mrp)


    


