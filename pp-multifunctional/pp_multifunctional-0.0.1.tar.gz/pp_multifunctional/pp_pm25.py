def pm25(city_number):
    import requests
    try:
        number = int(city_number)
    except ValueError:
        return '请输入城市编号（数字）！'
    else:
        a = requests.post('http://api.k780.com/?app=weather.pm25&appkey=49037&sign=745a62fb8cf430aae10da5bbd4c776d9&format=json', data={'weaid': number})
        if int(a.status_code) == 200:
            c = a.json()
            d = c['result']
            return d
