import requests
import json, csv

url = 'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=usd&sort=exchangedate&order=asc&json'

# Download JSON data
data = json.loads(requests.get(url).text)

# Write .json data to CSV file
with open('history.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['exchangedate', 'rate_per_unit'])
    for d in data:
        writer.writerow([d['exchangedate'], d['rate_per_unit']])

