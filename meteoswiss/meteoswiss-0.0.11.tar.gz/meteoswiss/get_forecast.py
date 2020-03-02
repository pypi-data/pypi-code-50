from bs4 import BeautifulSoup
import json
import requests
def get_forecast(postCode):
    baseUrl = 'https://www.meteosuisse.admin.ch'

    s = requests.Session()
    #Forcing headers to avoid 500 error when downloading file
    s.headers.update({"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, sdch",'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1337 Safari/537.36'})

    tmp = s.get("https://www.meteosuisse.admin.ch/home/actualite/infos.html?ort=%s"%postCode)

    soup = BeautifulSoup(tmp.text,features="html.parser")
    widgetHtml = soup.find_all("section",{"id": "weather-widget"})
    jsonUrl = widgetHtml[0].get("data-json-url")
    jsonDataFile = str.split(jsonUrl,'/')[-1]
    newJsonDataFile = str(postCode)+"00.json"
    jsonUrl = str(jsonUrl).replace(jsonDataFile,newJsonDataFile)
    jsonData = s.get(baseUrl + jsonUrl)
    jsonData.encoding = "utf8"
    jsonDataTxt = jsonData.text

    jsonObj = json.loads(jsonDataTxt)

    return jsonObj