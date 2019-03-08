# Requirements
#
#
# Imports and so requires BeautifulSoup, Requests. Install those with:
#`pip install beautifulsoup4`
#`pip install requests`
#
#
# How it works
#"input.csv" should start with a column of atom_ids
# To use, run `appcostlookup.py` and the price will be appended as a column
"""
# Import necessary modules
import requests
import io
from bs4 import BeautifulSoup
import csv
import random
import time
from datetime import datetime

# Import APP ID's
IMPORT_FILE_NAME = 'input.csv'
ids = []
    
with open(IMPORT_FILE_NAME, 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        ids.append(row[0])
print('Total id imported: ' + str(len(ids)))

# Custom Header
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'}

# Base URL

base_url = 'https://itunes.apple.com/us/app/id'

# Here data points will be store
price_list = []
id_track = []

# Entering loop
for i, id_ in enumerate(ids):
    
    try:
        # Making URL
        url = base_url + str(id_).replace('\n','').replace(' ','')
        # Doing GET requests with header
        r = requests.get(url, headers=headers)
        # Making soup object
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Extracting price
        price = soup.find(attrs={"class": "inline-list__item inline-list__item--bulleted app-header__list__item--price"}).text
        
        # Appending price and id
        price_list.append(price)
        id_track.append(id_)
        
        print('Left: ' + str(len(ids)-i))
        # Random sleep for not putting pressure on server
        time.sleep(random.random())
    
    except Exception as e: 
        print('Error: ' + str(e))
        print('id :' + str(id_))
        pass

# Zip data  
data = [[a,b] for a,b in zip(id_track, price_list)]
 
# Export to CSV     
EXPORT_FILE_NAME = 'output-' + "{:%Y_%m_%d_%M_%S}".format(datetime.now())  + '.csv'   
with open(EXPORT_FILE_NAME, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(data)

print(EXPORT_FILE_NAME + ' saved successfully.')
