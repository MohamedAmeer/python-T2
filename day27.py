# scrap a web and store data in excel.
import requests
import bs4
import pandas as pd


url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)


soup = bs4.BeautifulSoup(result.text, 'lxml')


cases = soup.find_all('div', class_='encounter-number')


data = []

for q in cases:
    span = q.find('span')
    data.append(span.string)

print(data)

df = pd.DataFrame({"CoronaData": data})

df.index = ['TotalCases', ' Deaths', 'Recovered']

df.to_csv('Covid_Data.csv')
cases = soup.find_all('div', class_='encounter-number')

data = []

for i in cases:
    span = i.find('span')
    data.append(span.string)

print(data)

df = pd.DataFrame({"CovidData": data})


df.index = ['TotalCases', ' Deaths', 'Recovered']


df.to_csv('Corona_Data.csv')