import requests
import dbClass

f = open("apikey.txt", "r")
d = open("dbalogin.txt", "r")
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=GE&apikey=' + API_KEY)
result = r.json()
monthly = result['Monthly Time Series']
month = '2018-03-29'
avgMonth = monthly[month]

hostname = d.readline()
username = d.readline()
passw = d.readline(9)
datab = d.read()

