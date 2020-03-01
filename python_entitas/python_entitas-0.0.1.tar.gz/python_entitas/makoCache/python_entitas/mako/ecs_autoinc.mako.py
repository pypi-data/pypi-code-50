# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1583057258.6082866
_enable_loop = True
_template_filename = 'E:\\python_entitas\\Parser\\..\\mako\\ecs_autoinc.mako'
_template_uri = '/python_entitas/mako/ecs_autoinc.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        contexts = context.get('contexts', UNDEFINED)
        __M_writer = context.writer()
        for k,con in contexts.items():
            __M_writer('from ..Extension.Context.')
            __M_writer(str(con.Name))
            __M_writer('Context import ')
            __M_writer(str(con.Name))
            __M_writer('Context\r\n')
        __M_writer('\r\n\r\nclass Contexts:\r\n')
        for k,con in contexts.items():

            name = con.Name[0].lower() + con.Name[1:]
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['name'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\r\n    ')
            __M_writer(str(name))
            __M_writer(' = ')
            __M_writer(str(con.Name))
            __M_writer('Context()\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "E:\\python_entitas\\Parser\\..\\mako\\ecs_autoinc.mako", "uri": "/python_entitas/mako/ecs_autoinc.mako", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 2, "24": 2, "25": 2, "26": 2, "27": 2, "28": 4, "29": 7, "30": 8, "36": 10, "37": 11, "38": 11, "39": 11, "40": 11, "46": 40}}
__M_END_METADATA
"""
