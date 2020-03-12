# -*- coding: utf-8 -*-

"""
    Регистратор методов для JSON-RPC.

    Используется для централизованного управления всеми методами приложения.

"""
# встроенные модули
from functools import partial
from inspect import signature
from types import FunctionType
from typing import Optional, List, Callable, Dict, Sequence, Union, Coroutine

# модули проекта
from trivial_tools.json_rpc.errors import (
    invalid_format, empty_request, invalid_version, no_method,
    unknown_method, no_arguments, wrong_arguments_type, no_secret_key,
    internal_error, not_found)
from trivial_tools.formatters.base import s_type
from trivial_tools.json_rpc.basic_tools import (
    Request, Error, form_error, Result, decide, authorize, result
)


class JSONRPCMethodMaster:
    """
    Регистратор методов для JSON-RPC.

    Используется для централизованного управления всеми методами приложения.
    """

    def __init__(
            self,
            config,
            auth_callback: Optional[Callable] = None,
            post_mortem_callback: Optional[Callable] = None,
            ignores: Sequence[str] = ('secret_key',),
    ):
        """
        Инициация.
        """
        self.config = config
        self.auth_callback = auth_callback
        self.post_mortem_callback = post_mortem_callback
        self._ignores = ['return'] + list(ignores)
        self._methods: Dict[str, Callable] = {}

    def __contains__(self, method_name: str):
        """
        Проверить, имеется ли этот метод в записях.
        """
        return method_name in self._methods

    def register_method(self, func: Union[FunctionType, Coroutine]) -> FunctionType:
        """
        Зарегистрировать метод.
        """
        self._methods[func.__name__] = func
        return func

    def unknown_method(self, method_name: str) -> bool:
        """
        Этот метод нам неизвестен?
        """
        return method_name not in self._methods

    def get_method(self, method_name: str) -> Optional[Callable]:
        """
        Получить метод.
        """
        return self._methods.get(method_name)

    def get_method_names(self) -> List[str]:
        """
        Получить имена доступных методов.
        """
        return sorted(self._methods.keys())

    @staticmethod
    def base_conveyor(requests: List[Request], errors: List[Error], func: Callable) -> None:
        """
        Базовая функция сортировки запросов.
        """
        filtered = []
        while requests:
            new_request = requests.pop()
            output = func(new_request)
            decide(output, filtered, errors)

        requests.extend(reversed(filtered))

    def check_request_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверить на предмет соответствия JSON RPC 2.0.
        """
        self.base_conveyor(requests, errors, func=self.check_dict)

    def check_signature_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        self.base_conveyor(requests, errors, func=self._check_signature)

    def check_auth_conveyor(self, requests: List[Request], errors: List[Error]) -> None:
        """
        Проверить авторизацию внешней функцией (если есть).
        """
        if self.auth_callback is None:
            self.base_conveyor(requests, errors,
                               func=lambda x: x)
        else:
            self.base_conveyor(requests, errors,
                               func=partial(authorize, check_func=self.auth_callback))

    def _check_signature(self, request: Request) -> Union[Request, Error]:
        """
        Проверка полученных параметров на соответствие сигнатуре метода.
        """
        method_name = request.get('method')
        params = request.get('params')
        msg_id = request.get('id')
        need_id = 'id' in request

        if isinstance(params, list):
            # мы не можем проверить аргументы, если они переданы по порядку
            return request

        params = params.keys()

        method: FunctionType = self._methods[method_name]
        sig = signature(method)

        if 'kwargs' in sig.parameters:
            # мы не можем проверить аргументы, если функция принимает их в запакованном виде
            return request

        valid_keys = {x for x in sig.parameters if x not in self._ignores}
        other_keys = {x for x in params if x not in self._ignores}

        message = 'Расхождение в аргументах метода: '

        if valid_keys != other_keys:
            insufficient = ', '.join(sorted(valid_keys - other_keys))
            excess = ', '.join(sorted(other_keys - valid_keys))

            if insufficient:
                message += 'не хватает аргументов ' + insufficient

                if excess:
                    message += ', '

            if excess:
                message += 'лишние аргументы ' + excess

            return form_error(-32602, message, need_id, msg_id)
        return request

    def check_dict(self, request: Request) -> Union[Request, Error]:
        """
        Проверить словарь запроса.
        """
        if not isinstance(request, dict):
            return form_error(*invalid_format(s_type(request)))

        method = request.get('method')
        params = request.get('params')
        msg_id = request.get('id')
        need_id = 'id' in request

        if not request:
            response = form_error(*empty_request())

        elif request.get('jsonrpc') != '2.0':
            response = form_error(*invalid_version(), need_id, msg_id)

        elif method is None:
            response = form_error(*no_method(), need_id, msg_id)

        elif method not in self._methods:
            response = form_error(*unknown_method(str(method)), need_id, msg_id)

        elif params is None:
            response = form_error(*no_arguments(), need_id, msg_id)

        elif not isinstance(params, (dict, list)):
            response = form_error(*wrong_arguments_type(), need_id, msg_id)

        elif isinstance(params, dict) and params.get('secret_key') is None:
            response = form_error(*no_secret_key(), need_id, msg_id)

        else:
            response = request

        return response

    def execute(self, request: Request) -> Result:
        """
        Исполнить запрос.
        """
        method_name = request.get('method', 'unknown method')
        params = request.get('params', {})
        method = self.get_method(method_name)

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if isinstance(params, dict):
            # убираем игнорируемые параметры
            for argument in self._ignores:
                params.pop(argument, None)
            response = method(**params)
        else:
            response = method(*params)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        return response

    async def async_execute(self, request: Request) -> Result:
        """
        Исполнить запрос.
        """
        method_name = request.get('method', 'unknown method')
        params = request.get('params', {})
        method = self.get_method(method_name)

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if isinstance(params, dict):
            # убираем игнорируемые параметры
            for argument in self._ignores:
                params.pop(argument, None)
            response = await method(**params)
        else:
            response = await method(*params)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        return response

    async def render_get(self):
        """
        Приветствие для пользователя
        """
        methods = ''.join([f'<li>{x}</li>' for x in sorted(self.get_method_names())])

        html = (
            f"<html><head><title>{self.config.SERVICE_NAME}</title></head>"
            f"<body><strong>{self.config.SERVICE_NAME}</strong><br>POST methods:<ul>"
            f"{methods}"
            "</ul></body></html>"
        )

        return html

    async def render_post(self, request: Union[list, dict]) -> Union[Result, Error]:
        """
        Обработка запроса
        """
        if isinstance(request, dict):
            requests = [request]

        elif isinstance(request, list):
            requests = request

        else:
            response = form_error(*invalid_format(f'{s_type(request)}'))
            return response

        errors = []
        results = []

        try:
            self.check_request_conveyor(requests, errors)
            self.check_signature_conveyor(requests, errors)
            self.check_auth_conveyor(requests, errors)

        except Exception as err:
            self.post_mortem_callback(err)
            errors.append(form_error(*internal_error()))

        else:
            for job in requests:
                need_id = 'id' in job
                msg_id = job.get('id')

                # noinspection PyBroadException
                try:
                    method_result = await self.async_execute(job)

                    if need_id:
                        results.append(result(method_result, msg_id=msg_id))
                    else:
                        # мы не отвечаем на нотификации без id
                        pass

                except FileNotFoundError:
                    errors.append(form_error(*not_found(), need_id=need_id, msg_id=msg_id))

                except Exception as err:
                    self.post_mortem_callback(err)
                    errors.append(form_error(*internal_error(), need_id=need_id, msg_id=msg_id))

        output = results + errors
        if len(output) == 1:
            output = output[0]

        return output
