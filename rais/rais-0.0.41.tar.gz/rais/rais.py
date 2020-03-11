__author__ = 'v.denisov'

from rais.parameter_initialization import ParameterInitialization as pi
from rais.session import SessionHelper as session
from rais.create_interested_parties import CreateInterestedParties as create_ip

class Rais:
    def __init__(self):
        pass

    @classmethod
    def initialization(self, url_host, prefix, x_project_name):
        """
        Инициализация параметров. обязателен перед логином

        :param url_host:
        :type url_host: Строка
        :param prefix: Префикс при создании наименования
        :type prefix: Строка
        :param x_project_name: Обязательный параметр для headers
        :type x_project_name: Строка
        """
        pi.set_url_host(url_host=url_host)
        pi.set_prefix(prefix=prefix)
        pi.set_headers(headers={'X-Project-Name': x_project_name})

    @classmethod
    def get_parameters(self):
        parameters = {
            "url_host": pi.get_url_host(),
            "prefix": pi.get_prefix(),
            "headers": pi.get_headers(),
            "cookies": pi.get_cookies()
        }
        return parameters

    @classmethod
    def login(self, username, password, profiles_cookie, language):
        response_login = session.login(username=username, password=password,
                                       profiles_cookie=profiles_cookie, language=language)
        return response_login

    @classmethod
    def create_IP_person(self, type_person, prefix='_'):
        """
        Создание Заинтересованной стороны.
        Физическое лицо.

        :param type_person: Тип физического лица.
                            Могут быть следующие значения:
                            composer: Композитор
                            corpse: Мертвец
                            scriptwriter: Автор текста
                            atk: АТК
                            foreigner: Иностранец
                            removed_rights: Изъявший -Есть уведомление об изъятии прав
                            not_transferring_rights: Не передавший права РАО
        :type type_person: Строка
        :param prefix: Префикс
        :return: Возврощает данные о созданной заинтересованной стороне
        :rtype:
        """
        person = create_ip.person(type_person=type_person, prefix=prefix)
        return person
