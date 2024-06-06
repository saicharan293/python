# web scraping: is a method to get related info of a particular object from net ,
# another definition: automation of data extraction from websites

import requests
from bs4 import BeautifulSoup

req=requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue#')
# print(req)

soup=BeautifulSoup(req.text,"html")

# print(soup)
find=soup.find('table',class_='wikitable sortable')
print(find)
# <table class="wikitable sortable jquery-tablesorter"></table>
# print(res.prettify())
