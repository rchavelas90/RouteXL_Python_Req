# -*- coding: utf-8 -*-

# Post requests from python to ROUTEXL API
# By Ricardo Chavelas
# All comments are very very welcome :)
# Purpose: To use ROUTEXL API with python packages requests to automate route optimization
# This documents is a tutorial on how to connect python with the API 

#Other Resources and Guides
# http://isbullsh.it/2012/06/Rest-api-in-python/
#http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# RouteXL API documentation https://www.routexl.nl/blog/api/?lang=en

# Import modules
import requests

############ -- Get status (Hello world) -- ############ 
url = 'https://api.routexl.nl/status' + str('/Hello world')
username = '' # Fill in YOUR username
password = '' # Fill in YOUR password

g = requests.get(url,auth=(username, password))
# Print useful information, just to know what can be retreived
print g
print g.status_code
print g.headers
print g.content
print g.url

############ --  Get distance matrix -- ############ 
# Define location
par1 = {"locations" : '[\
{"address":"The Hague, The Netherlands","lat":"52.05429","lng":"4.248618"},\
{"address":"The Hague, The Netherlands","lat":"52.076892","lng":"4.26975"},\
{"address":"Uden, The Netherlands","lat":"51.669946","lng":"5.61852"},\
{"address":"Sint-Oedenrode, The Netherlands","lat":"51.589548","lng":"5.432482"}]'}
url1 = 'https://api.routexl.nl/distances'

# Send post request
r1 = requests.post(url1, auth=(username, password), data=par1)

# Print useful information
print r1
print r1.content
print r1.url

############ -- Get Optimized Route -- ############ 
# Define location
# First element is used for start location, the last for finish. Note: if you
# need to start and finish from the same location, you’ll need to add it twice 
# in the array.

par2 = {"locations" : '[\
{"address":"The Hague, The Netherlands","lat":"52.05429","lng":"4.248618"},\
{"address":"The Hague, The Netherlands","lat":"52.076892","lng":"4.26975"},\
{"address":"Uden, The Netherlands","lat":"51.669946","lng":"5.61852"},\
{"address":"Sint-Oedenrode, The Netherlands","lat":"51.589548","lng":"5.432482"}]'}
url2 = 'https://api.routexl.nl/tour'
r2 = requests.post(url2, auth=(username, password), data=par2)

# Print useful information
print r2
print r2.content
print r2.url
