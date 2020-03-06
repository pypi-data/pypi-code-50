from .web_exc import WebException
from .the_time import IvlDef
from .base_web_handler import BaseWebHandler, WebArgs
from .my_tools import deserialize_tstamp


class WebHandler(BaseWebHandler):
    
    Reader = None
    
    def on_get(self, path: str, args: WebArgs) -> None:
        if path == '/info.json':
            self._parse_info()
        elif path == '/enum_hr.json':
            self._parse_enum_hr()
        elif path == '/enum_qt.json':
            self._parse_enum_qt()
        elif path == '/read.json':
            self._parse_read(args)
        else:
            raise WebException('Path not found: {}'.format(path), 404)

    def _parse_info(self):
        self.send_json({
            "version":{
                "major": 1,
                "minor": 1,
                "patch": 1,
            }
        })
        
    def _parse_enum_hr(self):
        # filter = args.get_str('filter', '')
        self.send_json(WebHandler.Reader.read_hr_wx(''))
        
    def _parse_enum_qt(self):
        self.send_json(WebHandler.Reader.read_qt_wx(True))
    
    def _parse_read(self, args):
        hr_ids_str = args.get_str ('hr')
        qt_id = args.get_str ('qt')
        all_ivl_s = args.get_str ('all_ivl')
        sub_ivl_s = args.get_str ('sub_ivl')
        finished = args.get_bool ('finished', False)
        setpt_str = args.get_str ('setpt', '')

        hr_ids = hr_ids_str.split(',')

        try: 
            all_ivl = IvlDef.parse ( all_ivl_s )
            sub_ivl = IvlDef.parse ( sub_ivl_s )
            
            setpt = None
            if setpt_str and setpt_str != 'null':
                setpt = deserialize_tstamp(setpt_str)   # *ValueError
                
        except ValueError as ex: 
            raise WebException(ex, 400)

        j = WebHandler.Reader.read_data_wx (hr_ids, qt_id, all_ivl, sub_ivl, finished, setpt)
        self.send_json(j)
