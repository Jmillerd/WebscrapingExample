import requests, json
from bs4 import BeautifulSoup
import pandas as pd

webpage_response = requests.get('https://cdn5.editmysite.com/app/store/api/v28/editor/users/143337397/sites/895400403664825007/products?page=1&per_page=60&sort_by=popularity_score&sort_order=desc&include=images,media_files,discounts&excluded_fulfillment=dine_in')
x = webpage_response.json()['data']

# Define product dictionary
product_data = {}

product_ids = []
site_product_ids = []
product_prices = []
product_names = []
product_badges = []
product_stock = []
price_formatted = []

for id in x:
  id = id['id']
  product_id = list(id.split(" "))
  product_ids.append(product_id)

for site_id in x:
  site_product_id = site_id['site_product_id']
  s_ids = list(site_product_id.split(" "))
  site_product_ids.append(s_ids)

for name in x:
  names = list(name['name'].split("\n"))
  product_names.append(names)


for badge in x:
 product_badge = badge['badges']  
 product_stock = str(product_badge['out_of_stock'])
 badges = list(product_stock.split(" "))
 product_badges.append(badges)


for price in x:
 product_price = price['price']  
 price_formatted = product_price['high_formatted']
 prices = list(price_formatted.split(" "))
 product_prices.append(prices)


new_data_list = list(zip(product_ids, site_product_ids, product_names, product_prices, product_badges))

df = pd.DataFrame(new_data_list, columns =['Id', 'Site Id', 'Name','Produce','Out of Stock'])
 
print(df)