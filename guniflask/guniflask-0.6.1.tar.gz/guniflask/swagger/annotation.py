# coding=utf-8

from guniflask.annotation.core import Annotation


class Api(Annotation):
    pass


class ApiMethod(Annotation):
    pass


class ApiParam(Annotation):
    QUERY_PARAM = 'query'
    PATH_PARAM = 'path'
    BODY_PARAM = 'body'

    def __init__(self, name: str = None, description: str = None, default=None, required: bool = False,
                 example=None, type: str = None):
        if type is None:
            type = self.QUERY_PARAM
        super().__init__(name=name, description=description, default=default, required=required,
                         exmaple=example, type=type)


def api_param(name: str = None, description: str = None, default=None, required: bool = False,
              example=None, type: str = None):
    pass


class ApiResponse(Annotation):
    def __init__(self, code: int = None, message: str = None, response: type = None):
        super().__init__(code=code, message=message, response=response)
