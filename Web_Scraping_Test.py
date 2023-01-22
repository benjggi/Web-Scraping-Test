#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:28:53 2023

@author: benjamin
"""

import requests

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

