import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import re

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
    table_head = table.find('thead')
    header = table_head.find('tr').text.strip().split(' ')
    headers = [i.text.replace(u'\xa0', u' ').replace(',', '\n') for i in table_head.findAll('th')]
    new_headers = []
    for i in headers:
        try:
            match = re.search('([a-z])([A-Z])', i)
            new_headers.append(re.sub('[a-z][A-Z]', f'{match.group(1)}\n{match.group(2)}', i))
        except AttributeError:
            new_headers.append(i)
    data = []
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [i.text.strip() for i in cols]
        data.append([i for i in cols])
    df = pd.DataFrame(data, columns = new_headers)
    print(tabulate(df, headers=header, tablefmt='psql', showindex=False))

def get_news():
    inner_content = soup.find('div', {'id': 'innercontent'})
    lists = inner_content.findAll('ul')
    for i in lists:
        x = i.findAll('li')
        bullets = [x[i].text.strip().rstrip(' [source]') for i in range(len(x))]
        for x in bullets:
            print(f"-{x}\n")