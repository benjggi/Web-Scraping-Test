#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:28:53 2023

@author: benjamin
"""

import requests
from matplotlib import pyplot as plt 
import numpy as np

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
url1 = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
response = requests.get(url)
response1 = requests.get(url1)
data = response.json()
data1 = response1.json()
price_BTC = data['bitcoin']['usd']
price_BTC_ = data1['bitcoin']['eur']

print("The current Bitcoin price is: " + str(price_BTC) +"$")
print("The current Bitcoin price is: " + str(price_BTC_) +"€")

input_BTC = float(input("Enter how much BTC you own: " ))
euro_BTC = input_BTC*price_BTC_
dollar_BTC = input_BTC*price_BTC
print("You own BITCOIN worth " + str(euro_BTC) + "€")
print("You own BITCOIN worth " + str(dollar_BTC) + "$")


url2 = 'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd'
url3 = 'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=eur'
response2 = requests.get(url2)
response3 = requests.get(url3)
data2 = response2.json()
data3 = response3.json()
price_XRP = data2['ripple']['usd']
price_XRP_ = data3['ripple']['eur']

print("The current XRP price is: " + str(price_XRP) +"$")
print("The current XRP price is: " + str(price_XRP_) +"€")

input_XRP = float(input("Enter how much XRP you own: " ))
euro_XRP = input_XRP*price_XRP_
dollar_XRP = input_XRP*price_XRP
print("You own XRP worth " + str(euro_XRP) + "€")
print("You own XRP worth " + str(dollar_XRP) + "$")

url4 = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
url5 = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
response4 = requests.get(url4)
response5 = requests.get(url5)
data4 = response4.json()
data5 = response5.json()
price_ETH = data4['ethereum']['usd']
price_ETH_ = data5['ethereum']['eur']

print("The current ETH price is: " + str(price_ETH) +"$")
print("The current ETH price is: " + str(price_ETH_) +"€")

input_ETH = float(input("Enter how much ETH you own: " ))
euro_ETH = input_ETH*price_ETH_
dollar_ETH = input_ETH*price_ETH
print("You own ETH worth " + str(euro_ETH) + "€")
print("You own ETH worth " + str(dollar_ETH) + "$")

total_inv=euro_BTC+euro_XRP+euro_ETH
pro_BTC=100/total_inv*euro_BTC
pro_XRP=100/total_inv*euro_XRP
pro_ETH=100/total_inv*euro_ETH

print("BTC: " + str(pro_BTC) + "%")
print("XRP: " + str(pro_XRP) + "%")
print("ETH: " + str(pro_ETH) + "%")

cryptos = ['BTC', 'XRP', 'ETH'] 
data = [pro_BTC, pro_XRP, pro_ETH] 
fig = plt.figure(figsize =(10, 7)) 
plt.pie(data, labels = cryptos) 
  
plt.show() 
