import multiprocessing
import requests

from n3th0us3.colorizers import (
    ok,
    notice,
)

TLD = [
    # Российские
    'ru',
    'su',
    'spb.ru',
    'msk.ru',
    'com.ru',
    'org.ru',
    'pp.ru',
    'net.ru',
    'msk.su',
    'nov.ru',
    'nov.su',
    'ru.net',
    'spb.su',
    'moscow',
    'ru.com',
    # Кириллические
    'рф',
    'рус',
    'сайт',
    'онлайн',
    'москва',
    'дети',
    # Международные
    'com',
    'org',
    'info',
    'me',
    'cc',
    'eu',
    'fm',
    'tv',
    'ws',
    'io',
    'us',
    'name',
    # Тематические
    'online',
    'club',
    'tech',
    'site',
    'fun',
    'website',
    'space',
    'nu',
    'land',
    'camera',
    'bike',
    'computer',
    'house',
    'zone',
    'holiday',
    'wiki',
    'academy',
    'education',
    'university',
    'events',
    'bar',
    'coffee',
    'cooking',
    'menu',
    'pub',
    'best',
    'cool',
    'photo',
    'dance',
    'florist',
    'moda',
    'sexy',
    'click',
    'city',
    'report',
    'help',
    'software',
    'community',
    'digital',
    'direct',
    'domains',
    'social',
    'rest',
    'global',
    'how',
    'science',
    'party',
    'win',
    'download',
    'review',
    'news',
    'men',
    'one',
    'study',
    'xyz',
    'li',
    'moe',
    'live',
    'studio',
    'video',
    'style',
    'team',
    'show',
    'life',
    'world',
    'co',
    'cloud',
    'pw',
    'blog',
    'art',
    'stream',
    'cam',
    'be',
    'realty',
    'im',
    'auction',
    'band',
    'beer',
    'bet',
    'date',
    'fish',
    'fit',
    'futbol',
    'love',
    'ooo',
    'run',
    'tel',
    'uno',
    'vet',
    # Бизнес
    'store',
    'shop',
    'biz',
    'mobi',
    'guru',
    'today',
    'pro',
    'estate',
    'company',
    'email',
    'center',
    'trade',
    'expert',
    'media',
    'build',
    'capital',
    'country',
    'services',
    'support',
    'technology',
    'business',
    'finance',
    'money',
    'coach',
    'work',
    'mba',
    'top',
    'sale',
    'promo',
    'ltd',
    'group',
    'market',
    # Геодомены
    'abkhazia.su',
    'adygeya.ru',
    'adygeya.su',
    'aktyubinsk.su',
    'arkhangelsk.su',
    'armenia.su',
    'ashgabad.su',
    'azerbaijan.su',
    'balashov.su',
    'bashkiria.ru',
    'bashkiria.su',
    'bir.ru',
    'bryansk.su',
    'bukhara.su',
    'cbg.ru',
    'chimkent.su',
    'dagestan.ru',
    'dagestan.su',
    'east-kazakhstan.su',
    'georgia.su',
    'grozny.ru',
    'grozny.su',
    'ivanovo.su',
    'kalmykia.ru',
    'jambyl.su',
    'kalmykia.su',
    'kaluga.su',
    'karacol.su',
    'karaganda.su',
    'karelia.su',
    'khakassia.su',
    'krasnodar.su',
    'kurgan.su',
    'kustanai.ru',
    'kustanai.su',
    'lenug.su',
    'mangyshlak.su',
    'marine.ru',
    'mordovia.ru',
    'mordovia.su',
    'murmansk.su',
    'mytis.ru',
    'nalchik.ru',
    'nalchik.su',
    'navoi.su',
    'north-kazakhstan.su',
    'obninsk.su',
    'penza.su',
    'pokrovsk.su',
    'pyatigorsk.ru',
    'sochi.su',
    'tashkent.su',
    'termez.su',
    'togliatti.su',
    'troitsk.su',
    'tselinograd.su',
    'tula.su',
    'tuva.su',
    'vladikavkaz.ru',
    'vladikavkaz.su',
    'vladimir.ru',
    'vladimir.su',
    'vologda.su',
    'exnet.su',
]


def get_domain_info(domain_name, domain_tld):
    headers = dict()
    headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    headers['Accept-Encoding'] = 'gzip, deflate, br'
    headers['Accept-Language'] = 'ru,en;q=0.9'
    headers['Cache-Control'] = 'no-cache'
    headers['Connection'] = 'keep-alive'
    headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    headers['Host'] = 'domains.nethouse.ru'
    headers['Origin'] = 'https://domains.nethouse.ru'
    headers['Pragma'] = 'no-cache'
    headers['Referer'] = 'https://domains.nethouse.ru/domains'
    headers['Sec-Fetch-Site'] = 'same-origin'
    headers['Sec-Fetch-Mode'] = 'cors'
    headers['X-Requested-With'] = 'XMLHttpRequest'
    headers['User-Agent'] = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/78.0.3904.108 YaBrowser/19.12.3.332 (beta) Yowser/2.5 Safari/537.36')

    response = requests.post(
        'https://domains.nethouse.ru/domains/check',
        dict(
            name=domain_name,
            domain_tld=domain_tld
        ),
        headers=headers
    )
    return response.json()


def pooled_domains_info(domains_names, callback_method=None, processes_count: int = None):
    if processes_count is None:
        processes_count = 2
    if callback_method is None:
        callback_method = formatted_print
    _pool = multiprocessing.Pool(processes=processes_count)

    for domain_name in domains_names:
        for _tld in TLD:
            print(notice('Add pool check for: %s.%s' % (domain_name, _tld)))
            _pool.apply_async(get_domain_info, args=(domain_name, _tld), callback=callback_method)

    _pool.close()
    print(ok('Start...'))
    _pool.join()
    print(ok('End.'))


def special_formatted_print(data):
    print(
        data.get('result').get('domain'),
        ' / %s' % data.get('result').get('type_error') if data.get('result').get('type_error') else '',
        ' / %s' % data.get('result').get('error_message') if data.get('result').get('error_message') else '',
        ' / %s₽' % data.get('result').get('premium_price') if data.get('result').get('premium_price') else '',
        ' / %s' % data.get('result'),
        sep=''
    )


def formatted_print(data):
    print(
        data.get('result').get('domain'),
        data,
        sep=' '
    )


def do_nothing(data):
    return data
