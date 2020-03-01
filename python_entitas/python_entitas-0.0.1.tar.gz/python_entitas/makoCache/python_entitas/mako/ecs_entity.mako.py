# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1583056174.2661617
_enable_loop = True
_template_filename = 'E:\\python_entitas\\Parser\\..\\mako\\ecs_entity.mako'
_template_uri = '/python_entitas/mako/ecs_entity.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        context_name = context.get('context_name', UNDEFINED)
        contexts = context.get('contexts', UNDEFINED)
        __M_writer = context.writer()

        Context_name = context_name[0].upper() + context_name[1:]
        components = contexts.components
        event_comps = contexts.event_comps
        import json
        def params(a, sep = ', ' , b = []):
            b = []
            for item in a:
                b.append(item[0])
            return sep.join(b)
        
        def params_str(a, sep = ', ' , b = []):
            b = []
            for item in a:
                b.append('"' + item[0] + '"')
            return sep.join(b)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['json','params','params_str','event_comps','Context_name','components'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\nfrom .Source import Context, Entity, PrimaryEntityIndex, EntityIndex, Matcher\r\nfrom .')
        __M_writer(str(Context_name))
        __M_writer('Components import ')
        __M_writer(str(Context_name))
        __M_writer('Components as ')
        __M_writer(str(Context_name))
        __M_writer('_comps\r\n\r\n\r\nclass ')
        __M_writer(str(Context_name))
        __M_writer('Entity(Entity):\r\n    def __init__(self):\r\n        super().__init__()\r\n')
        for comp in components:

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','Context_name','name','properties'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('        self.')
            __M_writer(str(name))
            __M_writer(' = None\r\n')
        __M_writer('        return\r\n\r\n\r\n')
        for comp in components:

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','Context_name','name','properties'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\r\n')
            if not comp.simple:
                __M_writer('    def has')
                __M_writer(str(Name))
                __M_writer('(self):\r\n        return self.has(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n\r\n    def add')
                __M_writer(str(Name))
                __M_writer(' (self, ')
                __M_writer(str(params(properties)))
                __M_writer('):\r\n        self.add(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(', ')
                __M_writer(str(params(properties)))
                __M_writer(')\r\n        return self\r\n\r\n    def replace')
                __M_writer(str(Name))
                __M_writer(' (self,')
                __M_writer(str(params(properties)))
                __M_writer('):\r\n        self.replace(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(', ')
                __M_writer(str(params(properties)))
                __M_writer(')\r\n        return self\r\n\r\n    def remove')
                __M_writer(str(Name))
                __M_writer(' (self):\r\n        self.remove(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n        return self\r\n')
            else:
                __M_writer('    def has')
                __M_writer(str(Name))
                __M_writer('(self):\r\n        return self.has(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n\r\n    def set')
                __M_writer(str(Name))
                __M_writer('(self, v):\r\n        if (v != self.has')
                __M_writer(str(Name))
                __M_writer('()):\r\n            if (v):\r\n                self.add(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n            else:\r\n                self.remove(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n        return self\r\n')
        if event_comps:
            for comp in event_comps:
                __M_writer('    def Add')
                __M_writer(str(comp.Name))
                __M_writer('CallBack(self, callback, target):\r\n        local list\r\n        if not self.has')
                __M_writer(str(comp.Name))
                __M_writer('() then\r\n            list = set.new(false)\r\n        else\r\n            list = self.')
                __M_writer(str(comp.name))
                __M_writer('.value\r\n        end\r\n        list:insertkv(callback, target)\r\n        self.replace')
                __M_writer(str(comp.Name))
                __M_writer('(list)\r\n\r\n    def Remove')
                __M_writer(str(comp.Name))
                __M_writer('CallBack(self, callback, removeComponentWhenEmpty):\r\n        if removeComponentWhenEmpty == nil then\r\n            removeComponentWhenEmpty = true\r\n        end\r\n        local listeners = self.')
                __M_writer(str(comp.name))
                __M_writer('.value\r\n        listeners:remove(callback)\r\n        if removeComponentWhenEmpty and listeners:size() == 0 then\r\n            self.remove')
                __M_writer(str(comp.Name))
                __M_writer('()\r\n        else\r\n            self.replace')
                __M_writer(str(comp.Name))
                __M_writer('(listeners)\r\n        end\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "E:\\python_entitas\\Parser\\..\\mako\\ecs_entity.mako", "uri": "/python_entitas/mako/ecs_entity.mako", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "43": 18, "44": 20, "45": 20, "46": 20, "47": 20, "48": 20, "49": 20, "50": 23, "51": 23, "52": 26, "53": 27, "62": 33, "63": 33, "64": 33, "65": 35, "66": 38, "67": 39, "76": 44, "77": 45, "78": 46, "79": 46, "80": 46, "81": 47, "82": 47, "83": 47, "84": 47, "85": 49, "86": 49, "87": 49, "88": 49, "89": 50, "90": 50, "91": 50, "92": 50, "93": 50, "94": 50, "95": 53, "96": 53, "97": 53, "98": 53, "99": 54, "100": 54, "101": 54, "102": 54, "103": 54, "104": 54, "105": 57, "106": 57, "107": 58, "108": 58, "109": 58, "110": 58, "111": 60, "112": 61, "113": 61, "114": 61, "115": 62, "116": 62, "117": 62, "118": 62, "119": 64, "120": 64, "121": 65, "122": 65, "123": 67, "124": 67, "125": 67, "126": 67, "127": 69, "128": 69, "129": 69, "130": 69, "131": 73, "132": 74, "133": 75, "134": 75, "135": 75, "136": 77, "137": 77, "138": 80, "139": 80, "140": 83, "141": 83, "142": 85, "143": 85, "144": 89, "145": 89, "146": 92, "147": 92, "148": 94, "149": 94, "150": 98, "156": 150}}
__M_END_METADATA
"""
