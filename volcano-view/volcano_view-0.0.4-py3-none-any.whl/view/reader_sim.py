import random

# locals
from .web_exc import WebException
from .my_tools import to_map, read_json_wx
from .period import ReportPeriod
from .reader_base import BaseReader


_CFG_FILE_NAME = 'sim.json'


class SimulationReader(BaseReader):
    def __init__(self, env, log):
        self.env = env
        self.log = log
        self.hr_ = None
        self.qt_ = None     # ( {id, title, eu, cumulative: bool}, ... )
        
        random.seed ()
        

    def reload_wx(self):
        # log = self.log
        env = self.env
        
        file_name = '{}/{}'.format(env.wd, _CFG_FILE_NAME) if env.wd else _CFG_FILE_NAME
        
        data = read_json_wx(file_name)

        self.hr_ = data.get('hr', None)
        if self.hr_ is None:
            raise Exception('"hr" node not found in {}'.format(file_name))
        
        #self.qt_ = tuple( filter(lambda x: x['cumulative'] == True, sim['qt']) )
        self.qt_ = data.get('qt', None)
        if self.qt_ is None:
            raise Exception('"qt" node not found in {}'.format(file_name))
    

        # rval: ( {id, parent_id, title}, ... )
    def read_hr_wx(self, _filter = None):
        return self.hr_

        # rval: ( {id, title, eu, cumulative: bool}, ... )
    def read_qt_wx(self, cumulative: bool):
        return self.qt_
            
    def read_data_wx (self, hr_ids, qt_id, all_ivl, sub_ivl, finished, setpt):
        # ensure we have hr&qt loaded
        hr_list = self.read_hr_wx ()
        qt_list = self.read_qt_wx (True)

        hr_map = to_map (hr_list, 'id')
        qt_map = to_map (qt_list, 'id')

        hrs = []
        for hr_id in hr_ids:
            hr = hr_map.get ( hr_id, None )
            if hr is None: 
                raise WebException ('Hr "{}" does not exist'.format(hr_id))
            hrs.append ( hr )

        qt = qt_map.get (qt_id, None)
        if not qt: 
            raise WebException ('Qt "{}" does not exist'.format(qt_id))

        crp = ReportPeriod (all_ivl, sub_ivl, finished, setpt)
        
        series = []
        for hr in hrs:
            serie = {
                'hr_id': hr['id'],
                'qt_id': qt['id'],
                'values': tuple ( map (lambda x: random.randint(0, 1000), crp.readouts()) )
            }
            series.append ( serie )
    
        return {
            'cumulative': True,
            'start': crp.begin().isoformat(),
            'readouts': tuple ( map (lambda x: x.isoformat(), crp.readouts()) ),
            'series': series
        }
