# -*- coding: utf-8 -*-

# Druwez - A GUI printing tool
# https://www.florian-diesch.de/software/druwez/
#
# Copyright (C) 2019 Florian Diesch devel@florian-diesch.de
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import json
from gi.repository import GObject

class JSONObjError(RuntimeError):
    pass

_registry = {}

def register_classes(*classes):
    for c in classes:
        _registry[c.__name__] = c

def to_str(objs):
    return json.dumps(objs, cls=GObjectJSONEncoder, indent=1)
            
def write_to_file(objs, path):
    with open(path, 'w') as outpt:
        outpt.write(to_str(objs))
        
def read_from_file(path):
    with open(path) as inpt:
        data = inpt.read()
    if data:
        return GObjectJSONDecoder().decode(data)

    
class GObjectJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, GObject.GObject):
            d = {'__gobject__': o.__class__.__name__}

            for spec in o.list_properties():
                if spec.flags & GObject.ParamFlags.READABLE:
                    d[spec.name] = o.get_property(spec.name)
            return d
        else:
            return super().default(o)

        
class GObjectJSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        kwargs['object_hook'] = self.object_hook
        super().__init__(*args, **kwargs)
        
    def object_hook(self, d):
        if d.get('__gobject__', None) is not None:
            cname = d['__gobject__']
            klass = _registry.get(cname, None)
            if klass is not None:
                del d['__gobject__']
                try:
                    return klass(**d)
                except Exception as e:
                    raise JSONObjError(str(e))



