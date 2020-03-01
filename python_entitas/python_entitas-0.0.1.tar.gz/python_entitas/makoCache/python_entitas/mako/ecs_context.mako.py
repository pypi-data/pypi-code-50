# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1583056422.6279085
_enable_loop = True
_template_filename = 'E:\\python_entitas\\Parser\\..\\mako\\ecs_context.mako'
_template_uri = '/python_entitas/mako/ecs_context.mako'
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
        import json
        def params_str(a, sep = ', ' , b = []):
            b = []
            for item in a:
                b.append('"' + item[0] + '"')
            return sep.join(b)
        def params(a, sep = ', ' , b = []):
            b = []
            for item in a:
                b.append(item[0])
            return sep.join(b)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['params_str','components','Context_name','json','params'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\nfrom .Source import Context, Entity, PrimaryEntityIndex, EntityIndex, Matcher\r\nfrom ..Extension.Entity.')
        __M_writer(str(Context_name))
        __M_writer('Entity import ')
        __M_writer(str(Context_name))
        __M_writer('Entity\r\nfrom .')
        __M_writer(str(Context_name))
        __M_writer('Components import ')
        __M_writer(str(Context_name))
        __M_writer('Components as Attr_comps\r\n\r\n\r\n\r\nclass ')
        __M_writer(str(Context_name))
        __M_writer('Context(Context):\r\n    def __init__(self):\r\n')
        for comp in components:

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','name','Context_name','properties'] if __M_key in __M_locals_builtin_stored]))
            if comp.single:
                if not comp.simple and comp.single:
                    __M_writer('        self.')
                    __M_writer(str(name))
                    __M_writer(' = None\r\n        self.')
                    __M_writer(str(name))
                    __M_writer('Entity = None\r\n')
        __M_writer('        super().__init__()\r\n        return\r\n\r\n')
        for comp in components:
            __M_writer('    ')

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','name','Context_name','properties'] if __M_key in __M_locals_builtin_stored]))
            if comp.single:
                if not comp.simple:
                    __M_writer('    def set')
                    __M_writer(str(Name))
                    __M_writer('(self,')
                    __M_writer(str(params(properties)))
                    __M_writer('):\r\n        if self.has_unique_component(')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(") then\r\n            error('")
                    __M_writer(str(Name))
                    __M_writer("Component already have')\r\n        end\r\n        return self.set_unique_component('")
                    __M_writer(str(name))
                    __M_writer("', ")
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(', ')
                    __M_writer(str(params(properties)))
                    __M_writer(')\r\n\r\n    def replace')
                    __M_writer(str(Name))
                    __M_writer('(self,')
                    __M_writer(str(params(properties)))
                    __M_writer('):\r\n        local entity = self.')
                    __M_writer(str(name))
                    __M_writer('Entity\r\n        if entity == nil then\r\n            self.set')
                    __M_writer(str(Name))
                    __M_writer('(')
                    __M_writer(str(params(properties)))
                    __M_writer(')\r\n        else\r\n            self.')
                    __M_writer(str(name))
                    __M_writer(' = entity.replace(')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(', ')
                    __M_writer(str(params(properties)))
                    __M_writer(')\r\n        end\r\n        return entity\r\n\r\n\r\n')
                else:
                    __M_writer('    def set')
                    __M_writer(str(Name))
                    __M_writer('(self, value):\r\n        if (value ~= self.has')
                    __M_writer(str(Name))
                    __M_writer("()) then\r\n            if (value) then\r\n                self.set_unique_component('")
                    __M_writer(str(name))
                    __M_writer("',")
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(", true)\r\n            else\r\n                self.remove_unique_component('")
                    __M_writer(str(name))
                    __M_writer("')\r\n            end\r\n        end\r\n        return self\r\n\r\n")
                __M_writer('\r\n    def has')
                __M_writer(str(Name))
                __M_writer('(self):\r\n        return self.has_unique_component(')
                __M_writer(str(Context_name))
                __M_writer('_comps.')
                __M_writer(str(Name))
                __M_writer(')\r\n\r\n    def remove')
                __M_writer(str(Name))
                __M_writer("(self):\r\n        self.remove_unique_component('")
                __M_writer(str(name))
                __M_writer("')\r\n")
        __M_writer('\r\n    def _create_entity(self):\r\n        return ')
        __M_writer(str(context_name))
        __M_writer('Entity()\r\n\r\n    def initGenerateEntityIndexes(self):\r\n')
        for comp in components:
            __M_writer('    ')

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','name','Context_name','properties'] if __M_key in __M_locals_builtin_stored]))
            for attr in  comp.attr:
                if attr.class_name == "primaryindex":
                    __M_writer('        local group = self:get_group(Matcher({')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer('}))\r\n        self._')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('PrimaryIndex = PrimaryEntityIndex:new(')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(", group, '")
                    __M_writer(str(attr.p_name))
                    __M_writer("')\r\n        self.add_entity_index(self._")
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('PrimaryIndex)\r\n')
                elif attr.class_name == "index":
                    __M_writer('        local group = self:get_group(Matcher({')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer('}))\r\n        self._')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('Index = EntityIndex:new(')
                    __M_writer(str(Context_name))
                    __M_writer('_comps.')
                    __M_writer(str(Name))
                    __M_writer(", group, '")
                    __M_writer(str(attr.p_name))
                    __M_writer("')\r\n        self.add_entity_index(self._")
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('Index)\r\n')
        __M_writer('\r\n    ')

        i = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        for index in contexts.muIndex:
            __M_writer('    ')

            matcher_parm = []
            call_parm = []
            i += 1
            for index_data in index.index_data:
                Name = index_data.k
                Name = Name[0].upper() + Name[1:]
                matcher_parm.append(Context_name + "_comps." + Name)
                value = index_data.v
                call_parm.append('{' + 'comp_type={0},  key =  "{1}"'.format(Context_name + "_comps." + Name, value) + '}')
            print(','.join(matcher_parm))
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['matcher_parm','Name','index_data','value','i','call_parm'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('        local group = self.get_group(Matcher({')
            __M_writer(str(','.join(matcher_parm)))
            __M_writer('}))\r\n        self._ContextIndex')
            __M_writer(str(i))
            __M_writer(' = classMap.EntityMuIndex:new(group, {\r\n            ')
            __M_writer(str(','.join(call_parm)))
            __M_writer('\r\n        })\r\n')
        __M_writer('        return\r\n\r\n\r\n')
        for comp in components:
            __M_writer('    ')

            Name = comp.Name
            name =  comp.name
            Context_name = context_name[0].upper() + context_name[1:]
            properties = comp.data
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['Name','name','Context_name','properties'] if __M_key in __M_locals_builtin_stored]))
            for attr in  comp.attr:
                if attr.class_name == "primaryindex":
                    __M_writer('    def GetEntityBy')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('(self,')
                    __M_writer(str(attr.p_name))
                    __M_writer('):\r\n        return self._')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('PrimaryIndex.get_entity(self,')
                    __M_writer(str(attr.p_name))
                    __M_writer(')\r\n')
                elif attr.class_name == "index":
                    __M_writer('    def GetEntitiesBy')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('(self,')
                    __M_writer(str(attr.p_name))
                    __M_writer('):\r\n        return self._')
                    __M_writer(str(Name))
                    __M_writer(str(attr.p_name))
                    __M_writer('Index.get_entities(')
                    __M_writer(str(attr.p_name))
                    __M_writer(')\r\n\r\n')
        __M_writer('\r\n\r\n    ')

        i = 0
            
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        for index in contexts.muIndex:
            __M_writer('    ')

            call_parm = []
            i += 1
            name_parm = []
            for index_data in index.index_data:
                Name = index_data.k
                Name = Name[0].upper() + Name[1:]
                name_parm.append(Name)
                name_parm.append(index_data.v)
                call_parm.append(Name+'_'+value)
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['name_parm','Name','index_data','i','call_parm'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\r\n    def ')
            __M_writer(str(index.funcName))
            __M_writer('(self,')
            __M_writer(str(','.join(call_parm)))
            __M_writer('):\r\n        return self._ContextIndex')
            __M_writer(str(i))
            __M_writer('.get_entities(')
            __M_writer(str(','.join(call_parm)))
            __M_writer(')\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "E:\\python_entitas\\Parser\\..\\mako\\ecs_context.mako", "uri": "/python_entitas/mako/ecs_context.mako", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "41": 16, "42": 18, "43": 18, "44": 18, "45": 18, "46": 19, "47": 19, "48": 19, "49": 19, "50": 23, "51": 23, "52": 25, "53": 26, "62": 32, "63": 33, "64": 34, "65": 34, "66": 34, "67": 35, "68": 35, "69": 39, "70": 42, "71": 43, "72": 43, "81": 49, "82": 50, "83": 51, "84": 51, "85": 51, "86": 51, "87": 51, "88": 52, "89": 52, "90": 52, "91": 52, "92": 53, "93": 53, "94": 55, "95": 55, "96": 55, "97": 55, "98": 55, "99": 55, "100": 55, "101": 55, "102": 57, "103": 57, "104": 57, "105": 57, "106": 58, "107": 58, "108": 60, "109": 60, "110": 60, "111": 60, "112": 62, "113": 62, "114": 62, "115": 62, "116": 62, "117": 62, "118": 62, "119": 62, "120": 67, "121": 68, "122": 68, "123": 68, "124": 69, "125": 69, "126": 71, "127": 71, "128": 71, "129": 71, "130": 71, "131": 71, "132": 73, "133": 73, "134": 79, "135": 80, "136": 80, "137": 81, "138": 81, "139": 81, "140": 81, "141": 83, "142": 83, "143": 84, "144": 84, "145": 87, "146": 89, "147": 89, "148": 92, "149": 93, "150": 93, "159": 99, "160": 100, "161": 101, "162": 101, "163": 101, "164": 101, "165": 101, "166": 102, "167": 102, "168": 102, "169": 102, "170": 102, "171": 102, "172": 102, "173": 102, "174": 102, "175": 103, "176": 103, "177": 103, "178": 104, "179": 105, "180": 105, "181": 105, "182": 105, "183": 105, "184": 106, "185": 106, "186": 106, "187": 106, "188": 106, "189": 106, "190": 106, "191": 106, "192": 106, "193": 107, "194": 107, "195": 107, "196": 111, "197": 112, "203": 114, "204": 115, "205": 116, "206": 116, "221": 128, "222": 128, "223": 128, "224": 129, "225": 129, "226": 130, "227": 130, "228": 133, "229": 136, "230": 137, "231": 137, "240": 143, "241": 144, "242": 145, "243": 145, "244": 145, "245": 145, "246": 145, "247": 145, "248": 146, "249": 146, "250": 146, "251": 146, "252": 146, "253": 147, "254": 148, "255": 148, "256": 148, "257": 148, "258": 148, "259": 148, "260": 149, "261": 149, "262": 149, "263": 149, "264": 149, "265": 154, "266": 156, "272": 158, "273": 159, "274": 160, "275": 160, "289": 171, "290": 172, "291": 172, "292": 172, "293": 172, "294": 173, "295": 173, "296": 173, "297": 173, "303": 297}}
__M_END_METADATA
"""
