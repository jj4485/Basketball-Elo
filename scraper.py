from bs4 import BeautifulSoup
import http.client
import requests

url = 'https://www.interbasket.net/news/rank-75-100-on-espns-list-of-best-nba-players-of-all-time-nbarank/30927/'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
players = []
tables = soup.find_all('table')
fourth_table = tables[3]

for row in fourth_table.find_all('tr')[1:]:
    cols = row.find_all('td')
    players.append(cols[1].text.strip())

print(players)

base_url = 'https://nba-players.herokuapp.com/players'
params = {"first_name": "Lebron"}
response = requests.get(base_url, params = params)
print(response.status_code) 