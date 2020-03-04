import helper

helper.shape = {
        # Components
        'Cloud':'cloud',
        'Database':'database',
        'Folder':'folder',
        'Frame':'tab',
        'Node':'box3d',
        'Package':'package',
        'Rectangle':'rect',    
        'Component':'component',
        'Interface':'circle',
        'Diamond':'diamond',

        # Views
        'Table'         :   'rect',
        'View'          :   'parallelogram',
        'Package'       :   'invhouse',
        'File'          :   'folder',
        'Integration'   :   'invtrapezium',
        'System'        :   'ellipse',
        'Task'          :   'cds'
    }

helper.comment_format = "# {text}\n"

class Helper(helper.helper):

    extension   = 'gv'    
    name = 'Graphviz'

    @staticmethod
    def render_attrs(label, attrs, enclosed=True):
        attrs.update({'label':label or ""})
        return \
            ('[' if enclosed else '') \
            + '; '.join(['{}="{}"'.format(k,v) for (k,v) in attrs.items()]) \
            + (']' if enclosed else '') \
            + ';' 

    @staticmethod
    def node(id, label, **kwargs):
        if kwargs.has_key('shape'):
            kwargs['shape'] = Helper.shape(kwargs['shape'])

        return id + ' ' + Helper.render_attrs(label, kwargs)

    @staticmethod    
    def edge(fromId, toId, label=None, **kwargs):
        return '{} -> {}'.format(fromId, toId) + ' ' + Helper.render_attrs(label, kwargs)

    note_node_attrs = {
            'shape':'note',
            'fillcolor':'lightyellow',
            'color':'darkred',
            'fontname':'Cambria',
            'fontcolor':'darkred' 
            }

    note_edge_attrs = {
            'color':'darkred',
            'style':'dashed',
            'constraint':'false',
            'arrowhead':'open'
    }

    comment_format = "' {text}\n"

    @staticmethod
    def startDiagram(*args, **attrs):
        return """
digraph g {{
#######################################
# base formatting

fontname="{fontname}";
compound=true; #enables edges between clusters

graph [
    fontname="{fontname}";
    fontsize=20;
    labelloc="t";
];

node [
    style=filled; 
    colorscheme=paired12; 
    fontname="{fontname}";
    fontsize=14;
];

edge [
    fontname="{fontname}"
    fontsize=14;
];
#######################################
{attrs}
        """.format(fontname='Calibri', attrs=Helper.render_attrs(args[1], attrs, False))

    @staticmethod
    def endDiagram(*args):
        return '}'

    @staticmethod
    def startSubdiagram(id, label, **kwargs):
        if kwargs.has_key('fillcolor'):
            kwargs.setdefault('style','filled')

        kwargs.setdefault('label',label)
        attrs = "; ".join(['{}="{}"'.format(k,v) for (k,v) in kwargs.items()]) +";"
        return """
subgraph cluster_{id} {{
    fontsize=18;
{attrs}""".format(id=id, attrs=attrs)


    @staticmethod
    def endSubdiagram(id, label, **kwargs):
        return "\n}} \n".format(id=id)