import requests
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
htmlvalue = response.content

soup = BeautifulSoup(htmlvalue,'html.parser')

title = soup.find_all('td',{'class':'titleColumn'})
reating = soup.find_all('td',{'class':'ratingColumn imdbRating'})

for baslig,izlenme in zip(title,reating):
    baslig = baslig.text
    izlenme = izlenme.text
    
    
    baslig = baslig.strip()
    baslig = baslig.replace('\n','')
    
    izlenme = izlenme.strip()
    izlenme = izlenme.replace('\n','')
    
    print(baslig)
    
    