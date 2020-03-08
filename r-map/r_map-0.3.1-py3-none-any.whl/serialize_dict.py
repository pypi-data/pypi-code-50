"""Functions for serializing a register map to/from a flat dictionary"""
import r_map
from r_map import Node

"""schema:
{
    root: { #need a starting point
        type: xxx,
        children: [ <uuid>, ]
    },
    <uuid>: {
        name: xxx,
        type: xxx,
        <other metadata>,
        _ref: <uuid>,
        children: [ <uuid>, ]
    }
}
"""

def dump(node, objs:dict=None):
    """Return a dictionary representing this object.
    """
    if node.uuid in objs:
        return
    my_uuid = self.uuid
    objs[my_uuid] = None #placeholder to prevent recursive calls serializing me
    dct = {n:getattr(node,n) for n in node._nb_attrs}
    dct['type'] = type(node).__name__
    ref = dct['_ref']
    if ref is not None:
        dct['_ref'] = ref.uuid
        #only save overridden values
        keys = node._nb_attrs - set(['_ref', '_alias'])
        for k in keys:
            if k in dct and hasattr(ref, k):
                dct_val = dct[k]
                ref_val = getattr(ref, k)
                if dct_val == ref_val:
                    dct.pop(k)
        objs[self.uuid] = dct
        dump(ref, objs)
    elif isinstance(node, r_map.ArrayedNode):
        base_node = dct.pop('base_node')
        if base_node:
            dct['base_node'] = dump(base_node, objs)
    elif len(node):
        dct['children'] = [dump(c, objs) for c in node]

    #no need to add nulls
    objs[my_uuid] = {k:v for k,v in dct.items() if v is not None}
    return my_uuid

def load(to_load:str, dct:dict, already_loaded:dict=None) -> Node:
    if not isinstance(dct, dict):
        raise ValueError(f"Expected dictionary type argument. Got {type(dct)}")
    if already_loaded is None:
        already_loaded = {}
    elif to_load in already_loaded:
        return already_loaded[to_load]

    #decode dict logic here
    entry = dct[to_load]
    type_name = entry.get('type')
    T = getattr(r_map, type_name) if type_name else None
    ref_uuid = entry.get('_ref')
    uuid = entry.get('uuid')
    if uuid in already_loaded:
        obj = already_loaded[uuid]
    elif ref_uuid:
        ref_obj = already_loaded.get(ref_uuid, load(ref_uuid, dct, already_loaded))
        vals = {k:v for k,v in entry.items() if k in ref_obj._nb_attrs
                                             and v is not None}
        obj = ref_obj._copy(alias=vals.pop('_alias', False),
                            **vals)
    elif T:
        vals = {k:v for k,v in entry.items() if k in T._nb_attrs
                                             and v is not None}

        if issubclass(T, r_map.ArrayedNode):
            vals['base_node'] = load(vals['base_node'], dct, already_loaded)
        obj = T(**vals)
        children = entry.get('children')
        if children:
            for child_entry in children:
                child_obj = load(child_entry,
                                 dct,
                                 already_loaded)
                obj._add(child_obj)
    else:
        raise ValueError(f"Could not load data: {entry}")
    already_loaded[obj.uuid] = obj
    return obj
