from search_google import search_phrase
from search_yandex import yandex_query
def intro():
    key_word = input("Введите текст запроса в поисковик ")
    search_system = input("Пожалуйста, выберите поисковую систему: 1) Google , 2) Yandex\n")


    if search_system == "1":
         search_phrase(str(key_word))
    elif search_system == "2":
         yandex_query(str(key_word))

