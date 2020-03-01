# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1583056174.2339158
_enable_loop = True
_template_filename = 'E:\\python_entitas\\Parser\\..\\mako\\ecs_make_component.mako'
_template_uri = '/python_entitas/mako/ecs_make_component.mako'
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
        def params_str(a, sep = ', ' , b = []):
            b = []
            for item in a:
                b.append('' + item[0] + '')
            return sep.join(b)
        components = contexts.components
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['components','Context_name','params_str'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('class ')
        __M_writer(str(Context_name))
        __M_writer('Components:\r\n')
        for comp in components:

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','Context_name','name','properties'] if __M_key in __M_locals_builtin_stored]))
            if not comp.simple:
                __M_writer('\r\n    class ')
                __M_writer(str(Name))
                __M_writer(":\r\n        _name = '")
                __M_writer(str(name))
                __M_writer("'\r\n        _Name = '")
                __M_writer(str(Name))
                __M_writer("'\r\n\r\n        def __init__(self, ")
                __M_writer(str(params_str(properties)))
                __M_writer('):\r\n')
                for p in properties:
                    __M_writer('            self.')
                    __M_writer(str(p[0]))
                    __M_writer(' = ')
                    __M_writer(str(p[0]))
                    __M_writer('\r\n')
            else:
                __M_writer('\r\n    class ')
                __M_writer(str(Name))
                __M_writer(":\r\n        _name = '")
                __M_writer(str(name))
                __M_writer("'\r\n        _Name = '")
                __M_writer(str(Name))
                __M_writer("'\r\n")
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "E:\\python_entitas\\Parser\\..\\mako\\ecs_make_component.mako", "uri": "/python_entitas/mako/ecs_make_component.mako", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "35": 10, "36": 10, "37": 10, "38": 11, "39": 12, "48": 18, "49": 19, "50": 20, "51": 20, "52": 21, "53": 21, "54": 22, "55": 22, "56": 24, "57": 24, "58": 25, "59": 26, "60": 26, "61": 26, "62": 26, "63": 26, "64": 28, "65": 29, "66": 30, "67": 30, "68": 31, "69": 31, "70": 32, "71": 32, "72": 35, "78": 72}}
__M_END_METADATA
"""
