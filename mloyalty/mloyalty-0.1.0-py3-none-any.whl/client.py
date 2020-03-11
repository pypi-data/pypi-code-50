from mloyalty.base import Mloyalty


class Client(Mloyalty):
    def __init__(self, username=None, password=None, base_url=None):
        super().__init__(username, password, base_url)

    def get_client_info(self, phone=None, card=None):
        """
        Получение данных Участника по заданному номеру телефона или номеру карты.
        :param phone: номер телефона (должен начинаться с 9)
        :param card: номер карты
        :return: словарь данных
        """
        method_url = 'api/client/ClientInfo'
        params = self.get_request_params()
        payload = {
            'operator': params['operator_id'],
        }
        if phone:
            payload['phone'] = phone
        if card:
            payload['card'] = card

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def client_create(self, phone, card=None, first_name=None, last_name=None, middle_name=None, email=None,
                      birth_date=None, allow_sms=1, allow_email=1, allow_push=0, gender=0, agree=1, friend_phone=None,
                      promo_code=None):
        """
        Создание профиля Участника программы лояльности.
        :param phone: номер телефона (должен начинаться с 9)
        :param card: номер карты
        :param first_name: имя
        :param last_name: фамилия
        :param middle_name: отчетво
        :param email: адрес электронной почты
        :param birth_date: дата рождения
        :param allow_sms: получать уведомления по SMS
        :param allow_email: получать уведомления по E-mail
        :param allow_push: получать уведомления через Push
        :param gender: пол (1 - муж., -1 - жен., 0 - не опеределен)
        :param agree: согласие на обработку персональных данных
        :param friend_phone: телефон друга/подруги для механики "Приведи друга"
        :param promo_code: промокод
        :return: словарь данных
        """
        method_url = 'api/values/ClientCreate'
        params = self.get_request_params()
        payload = {
            'Operator': params['operator_id'],
            'Partner': params['partner_id'],
            'PosCode': params['pos_code'],
            'Phone': phone,
            'AllowSms': allow_sms,
            'AllowEmail': allow_email,
            'AllowPush': allow_push,
            'Gender': gender,
            'AgreePersonalData': agree,
        }
        if card:
            payload['Card'] = card
        if first_name:
            payload['Name'] = first_name
        if last_name:
            payload['Surname'] = last_name
        if middle_name:
            payload['Patronymic'] = middle_name
        if email:
            payload['Email'] = email
        if birth_date:
            payload['Birthdate'] = birth_date
        if friend_phone:
            payload['FriendPhone'] = friend_phone
        if promo_code:
            payload['Promocode'] = promo_code

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def send_verification_code(self, phone):
        """
        Отправка проверочного код в SMS сообщении на указанный номер телефона.
        :param phone: номер телефона (должен начинаться с 9)
        :return: словарь данных
        """
        method_url = 'api/client/GetSendVerificationCode'
        params = self.get_request_params()
        payload = {
            'operator': params['operator_id'],
            'poscode': params['pos_code'],
            'phone': phone,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)

    def confirm_code(self, phone, code):
        """
        Проверка кода и валидация номера телефона.
        :param phone: номер телефона
        :param code: код подтверждения
        :return: словарь данных
        """
        method_url = 'api/client/GetConfirmCode'
        params = self.get_request_params()
        payload = {
            'phone': phone,
            'code': code,
        }

        return self._make_request(params['token'], method_url, method='post', params=payload)
