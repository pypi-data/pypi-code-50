import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

url = 'https://www.worldometers.info/coronavirus/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
important_info = soup.findAll('div', {'class': 'maincounter-number'})

def get_stats():
    for i, v in enumerate(('Cases', 'Deaths', 'Recovered')):
        print(f'{v}: {important_info[i].get_text().strip()}')

def get_table():
    table = soup.find('table', {'id': 'main_table_countries'})
    table_body = table.find('tbody')
    header = 'Country,Total\nCases,New\nCases,Total\nDeaths,New\nDeaths,Active\nCases,Total\nRecovered,Serious'.split(',')
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [i.text.strip() for i in cols]
        data.append([i for i in cols])
    df = pd.DataFrame(data, columns = header)
    print(tabulate(df, headers=header, tablefmt='psql', showindex=False))


def get_news():
    inner_content = soup.find('div', {'id': 'innercontent'})
    lists = inner_content.findAll('ul')
    for i in lists:
        x = i.findAll('li')
        bullets = [x[i].text.strip().rstrip(' [source]') for i in range(len(x))]
        for x in bullets:
            print(f"-{x}\n")

if __name__ == "__main__":
    print('Quick Stats:')
    get_stats()
    print()
    get_table()
    print()
    print('News:')
    get_news()