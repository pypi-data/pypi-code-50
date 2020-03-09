import sys

this = sys.modules[__name__]
this.flaskApp = None

def set_app(app):
    this.flaskApp = app

from flask.views import MethodView


class Watcher(type(MethodView)):
    def __init__(self, *args, **kwargs):
        return_ = super().__init__(*args, **kwargs)
        if hasattr(self, "_add_route_"):
            getattr(self, "_add_route_")(self)
        return return_

class RouteView(MethodView, metaclass=Watcher):
    route = None
    name = None

    def _add_route_(self):
        if self.route is not None:
            if self.name is None:
                self.name = self.__name__
            this.flaskApp.add_url_rule(self.route, self.name, self.as_view(self.name))
