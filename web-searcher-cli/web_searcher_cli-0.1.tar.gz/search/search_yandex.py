import yandex_search 
import json
api = json.load(open("../api.txt"))
user = api["api_user"]
key = api["api_key"]
yandex = yandex_search.Yandex(api_user=user, api_key=key)

def yandex_query(key_word):
    text = key_word
    results = yandex.search(text)
    list_results = results.items
    list_len = len(list_results)
    for i in range(list_len-1):
        c = list_results[i]
        print(c['title'],' - ',c['url'],'\n' )


