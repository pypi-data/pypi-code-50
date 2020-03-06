import codecs
import json
import http.server

from .web_exc import WebException


_MIME = {
    'txt': 'text/plain; charset=utf-8',
    'html': 'text/html; charset=utf-8',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpg',
    'json': 'application/json',
    'xml': 'application/xml; charset=utf-8',
}


class WebArgs:
    def __init__(self, args_str):
        self.args = {}
        for a in args_str.split('&'):
            eq = a.find('=')
            if eq==-1:
                self.args[a] = True
            else:
                self.args[a[:eq]] = a[eq+1:]

    def get_str(self, name, default = None):
        val = self._get( name )
        if val is None:
            if default is None:
                raise WebException ('Missing "{}" argument'.format(name), 400)
            return default
        else:
            return val

    def get_bool(self, name, default = None):
        val = self._get( name )
        if val is None:
            if default is None:
                raise WebException ('Missing "{}" argument'.format(name), 400)
            return default
        
        if val=='1':    return True
        elif val=='0':  return False

        raise WebException ('Argument "{}={}" is not a valid boolean (use 0 and 1)'.format(name, val), 400)

    def _get(self, name):
        return  self.args.get(name, None)


class BaseWebHandler(http.server.SimpleHTTPRequestHandler):
    
    WebPackage = None
    StaticPath = 'www'
    
    error_content_type = _MIME['txt']
    error_message_format = '%(message)s'

    '''
    def do_POST(self):
    '''
    
    # can throw WebException
    def on_get(self, path: str, args: WebArgs) -> None:                 # pylint:disable=no-self-use
        raise WebException('Path not found: {}'.format(path), 404)
    
    def do_GET(self):
        question_mark = self.path.find('?')
        
        if question_mark==-1:
            path = self.path
            args = ''
        else:
            path = self.path[:question_mark]
            args = self.path[question_mark+1:]

        # print('{} -- {} -- {}'.format(self.path, path, args))

        if path in ('/', '/index.html'):
            self.send_response(301)
            self.send_header('Location', '/www/index.html')
            self.end_headers()
            return
            
        if path.startswith('/www/'):
            self._serve_static(path[5:])
            return
            
        try:
            self.on_get(path, WebArgs(args))
        except WebException as ex:
            self.send_error(ex.http_code, '{}: {}'.format(path, ex))

    def _serve_static(self, file_path):
        dot = file_path.rfind('.')
        if dot!=-1:
            ext = file_path[dot+1:]
            if ext in _MIME:
                self.send_file(BaseWebHandler.StaticPath + '/' + file_path, _MIME[ext])
            else:
                self.send_file(BaseWebHandler.StaticPath + '/' + file_path, _MIME['txt'])
        else:
            self.send_error(404, 'File Not Found: {}'.format(file_path))

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', _MIME['json'])
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def send_file(self, path, mime):
        try:
            self.send_response(200)
            self.send_header('Content-type', mime)
            self.end_headers()
            
            if BaseWebHandler.WebPackage is None:
                with codecs.open(path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                with BaseWebHandler.WebPackage.open(path) as f:
                    self.wfile.write(f.read())
        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(path))
        
        
