import requests
from bs4 import BeautifulSoup
import pandas as pd
# CHANGED LINE BELOW
URL = 'https://dailyfantasyrankings.com.au/resources/nba/htm/projections/mballproj.htm'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
# CHANGED LINE BELOW
table = soup.select("#Finish_20945 > table")[0]
columns = ['#', 'PLAYER', 'POS', '@', 'TEAM', 'OPP',
           'M-UP', 'PACE', 'REST', 'PRICE', 'PROJ', 'VALUE', 'AVE']
df = pd.DataFrame(columns=columns)
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    print(row)
    # df = df.append(pd.Series(row, index=columns), ignore_index=True)

df.to_csv('dfr_proj.csv', index=False)
