import time
import json
import requests
import csv
# Grab a list of quotes to get form Yahoo
 
apikey='NPoSyjoUks5WjK0umt8Hca8vuIYbQvLlhm9ZqjKi' #my API Key
 
url = "https://yfapi.net/v6/finance/quote"
 
quest=input("please input stock ticker:")
querystring = {"symbols":quest}
headers = {
  'x-api-key': apikey
   }
 
response = requests.request("GET", url, headers=headers, params=querystring) 
#print(response.text)
 
response.raise_for_status()  # raises exception when not a 2xx response
if response.status_code != 204: 
    stock_json = response.json()
else:
    print('not a known stock ticker')
 
timestamp = stock_json['quoteResponse']['result'][0]['regularMarketTime'] 
#read time in seconds
new_time=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp)) 
#putting time in terms that humans understand
 
 
#Return market price, time and short name
print(str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) + ', ' + converted_time + ', ' + stock_json['quoteResponse']['result'][0]["shortName"])
#store in CSV
with open('newfile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) + ', ' + converted_time + ', ' + stock_json['quoteResponse']['result'][0]["shortName"])
