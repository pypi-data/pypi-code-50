class BaseEventHandlers(object):
    def handle_response(self, response):
        print(response.text)

    def handle_error(self, exception):
        print(repr(exception))


class FileEventHandlers(BaseEventHandlers):
    _cursor_position = None

    def get_cursor_position(self):
        return self._cursor_position

    def record_cursor_position(self, cursor):
        self._cursor_position = cursor
