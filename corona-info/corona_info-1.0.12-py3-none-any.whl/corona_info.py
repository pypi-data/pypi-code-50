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
    print(tabulate(df, headers=new_headers, tablefmt='psql', showindex=False))

def get_news(limit=15):
    c = 0
    flag = False
    inner_content = soup.find('div', {'id': 'innercontent'})
    lists = inner_content.findAll('ul')
    for i in lists:
        x = i.findAll('li')
        bullets = [x[i].text.strip().rstrip(' [source]') for i in range(len(x))]
        for x in bullets:
            if limit == c:
                flag = True
                break
            print(f"-{x}\n")
            c += 1
        if flag:
            break

def get_advice():
    print("Basic protective measures against the new coronavirus\n- Stay aware of the latest information on the COVID-19 outbreak, available on the WHO website and through your national and local public health authority.\n - COVID-19 is still affecting mostly people in China with some outbreaks in other countries. Most people who become infected experience mild illness and recover, but it can be more severe for others.\n\n1. WASH YOUR HANDS FREQUENTLY\n- Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.\n- Why? Washing your hands with soap and water or using alcohol-based hand rub kills viruses that may be on your hands.\n\n2. MAINTAIN SOCIAL DISTANCING\n- Maintain at least 1 meter (3 feet) distance between yourself and anyone who is coughing or sneezing.\n- Why? When someone coughs or sneezes they spray small liquid droplets from their nose or mouth which may contain virus.\n- If you are too close, you can breathe in the droplets, including the COVID-19 virus if the person coughing has the disease.\n\n3. AVOID TOUCHING EYES, NOSE, AND MOUTH\n- Why? Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth.\n- From there, the virus can enter your body and can make you sick.\n\n4. PRACTICE RESPIRATORY HYGIENE\n- Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately.\n- Why? Droplets spread virus. By following good respiratory hygiene you protect the people around you from viruses such as cold, flu and COVID-19.\n\n5. IF YOU HAVE FEVER, COUGH, AND DIFFICULTY BREATHING, SEEK MEDICAL CARE EARLY\n- Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority.\n- Why? National and local authorities will have the most up to date information on the situation in your area.\n- Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.\n\n6. STAY INFORMED AND FOLLOW ADVICE GIVEN BY YOUR HEALTHCARE PROVIDER\n- Stay informed on the latest developments about COVID-19. Follow advice given by your healthcare provider, your national and local public health authority or your employer on how to protect yourself and others from COVID-19.\n- Why? National and local authorities will have the most up to date information on whether COVID-19 is spreading in your area. They are best placed to advise on what people in your area should be doing to protect themselves.\n\n7. FOLLOW PROTECTION MEASURES FOR PERSONS WHO ARE IN OR HAVE RECENTLY VISITED (PAST 14 DAYS) AREAS WHERE COVID-19 IS SPREADING\n- Follow the guidance outlined above.\n- Stay at home if you begin to feel unwell, even with mild symptoms such as headache and slight runny nose, until you recover.\n- Why? Avoiding contact with others and visits to medical facilities will allow these facilities to operate more effectively and help protect you and others from possible COVID-19 and other viruses.\n\n8. IF YOU DEVELOP FEVER, COUGH AND DIFFICULTY BREATHING, SEEK MEDICAL ADVICE PROMPTLY AS THIS MAY BE DUE TO A RESPIRATORY INFECTION OR OTHER SERIOUS CONDITION\n- Call in advance and tell your provider of any recent travel or contact with travelers.\n- Why? Calling in advance will allow your health care provider to quickly direct you to the right health facility. This will also help to prevent possible spread of COVID-19 and other viruses.\n")

def get_help():
    print("-stats provides quick facts on the impact of coronavirus")
    print("-table provides a table of the number of people by country affected by the coronavirus")
    print("-news provides news updates regarding the spread of coronavirus")
    print("-advice provides tips on how to protect yourself from coronavirus")