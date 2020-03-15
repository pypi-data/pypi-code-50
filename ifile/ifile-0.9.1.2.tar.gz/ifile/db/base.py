from ifile.db.sqlalchemy.session import get_session


class DataBase(object):
    def __init__(self, app=None):
        self.app = app
        self.session = None

        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        with app.app_context():
            self.session = get_session()
