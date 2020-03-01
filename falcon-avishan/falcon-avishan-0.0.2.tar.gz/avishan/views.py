# todo calculate view time
from falcon.request import Request
from falcon.response import Response

from avishan.utils import AvishanRequest, AvishanResponse


class AvishanView:
    url = ''
    request = {}
    response = {}

    def get(self):
        pass

    def post(self):
        pass

    def on_get(self, req: Request, res: Response):
        self.request = AvishanRequest(req=req)
        self.response = AvishanResponse(res=res)
        self.get()
        res.context['response'] = self.response.data

    def on_post(self, req: Request, res: Response):
        self.request = AvishanRequest(req=req)
        self.response = AvishanResponse(res=res)
        self.post()
        res.context['response'] = self.response.data

