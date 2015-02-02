# -*- coding: utf-8 -*-

# Post requests from python to ROUTEXL API
# By Ricardo Chavelas
# All comments are very very welcome :)
# Purpose: To use ROUTEXL API with python packages requests & pandas to automate route optimization
# This documents is kind of a tutorial on how to connect python with the API 

# Import modules (All are included in CANOPY so no need to source code!)

import requests # To work with the API
import pandas as pd # to read CSV file
import os # to define working directory
import json # to convert json object

############ -- Get status (Hello world) -- ############ 

url = 'https://api.routexl.nl/status' + str('/Hello world')
username = '' # Fill in YOUR username
password = '' # Fill in YOUR password

g = requests.get(url,auth=(username, password))

# Print useful information, just to know what can be retreived
print ''
print g # If you get <Response [401]> then the API does not recognize your user/password
print g.status_code
print g.headers
print g.content 
print g.url


############ --  Define locations  -- ############ 

# A) Define locations by hand (Not very nice to do this by hand :/ )

par = {"locations" : '[\
{"address":"The Hague, The Netherlands","lat":"52.05429","lng":"4.248618"},\
{"address":"The Hague, The Netherlands","lat":"52.076892","lng":"4.26975"},\
{"address":"Uden, The Netherlands","lat":"51.669946","lng":"5.61852"},\
{"address":"Sint-Oedenrode, The Netherlands","lat":"51.589548","lng":"5.432482"}]'}

# B) Define locations by reading them from CSV flie with pandas DataFrame object
## Now this is nice, readable and easy

## Get working directory and change it to where the file is
print ''
os.getcwd() # Do we have the current WD defined?
path = '/Users/Ricardo/Dropbox/Proyectos/RouteXL_Python_Req' # Your path!
os.chdir(path)
os.listdir(path) # Verify that file 'locations.csv' file is on current directory

## Read CSV file with the locations
locations = pd.read_csv('locations.csv')
print ''
print locations 
print ''

## Now change the pandas DataFrame to JSON format and asign it to par variable
## Requests needs this info as a dict {parameter_name : information}
par = {'locations': locations.to_json(orient = 'records')} 

############ --  Get distance matrix -- ############ 

# Send post request
url1 = 'https://api.routexl.nl/distances'
r1 = requests.post(url1, auth=(username, password), data=par)

# Print useful information
print ''
print r1
print r1.content
print ''

# Get distance matrix in DataFrame object
dist_matrix_DF = pd.read_json(json.dumps(r1.json()[u'distances'], sort_keys=True), orient = 'index')
## Rearange columns (somehow I can't manage to get them ordered from the beggining)
dist_matrix_DF = dist_matrix_DF[['from', 'to', 'distance', 'duration', 'router']]
print dist_matrix_DF


############ -- Get Optimized Route -- ############ 
# Send post request
url2 = 'https://api.routexl.nl/tour'
r2 = requests.post(url2, auth=(username, password), data=par)

# Print useful information
print ''
print r2
print r2.content
print ''

# Get route in DataFrame object
route_matrix_DF = pd.read_json(json.dumps(r2.json()[u'route'],sort_keys = True), orient = 'index')
## Rearange columns (somehow I can't manage to get them ordered from the beggining)
route_matrix_DF = route_matrix_DF[['name', 'arrival', 'distance']]
print route_matrix_DF

############ --  Other Resources and Guides -- ############

# request package usage http://isbullsh.it/2012/06/Rest-api-in-python/
# request package how-to http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# RouteXL API documentation https://www.routexl.nl/blog/api/?lang=en
# DataFrame to JSON http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.to_json.html
# Get precise coordinates http://universimmedia.pagesperso-orange.fr/geo/loc.htm
# Reading JSON with pandas http://pandas.pydata.org/pandas-docs/stable/io.html#reading-json