from . import helper

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
        'Task'          :   'cds',

        #Architecture
        'Entity'        :   'ellipse',
        'Module'        :   'component',
        'SystemIntegration' : 'rect'
    }

helper.comment_format = "# {text}\n"

class Helper(helper.helper):

    extension   = 'graphml'    
    name = 'GraphML'

    @staticmethod
    def render_attrs(label, attrs, enclosed=True):
        attrs.update({'label':label or ""})
        return \
            ('[' if enclosed else '') \
            + '; '.join(['{}="{}"'.format(k,v) for (k,v) in list(attrs.items())]) \
            + (']' if enclosed else '') \
            + ';' 

    @staticmethod
    def node(id, label, **kwargs):
        attrs = kwargs
        print('{}: fillcolor={}'.format(id, attrs.get('fillcolor')))
        for (k,v) in [('id', id), ('label', label),
                      ('shape', 'rectangle'), 
                      ('fillcolor', '#FFFFFF'),
                      ('height', 30), 
                      ('width', 120),
                      ('x', 0),
                      ('y', 0),
                      ('rotationAngle', 0.0),
                      ('fontSize', 12)]:
            attrs.setdefault(k, v)

        return """
	<node id="{id}">
		<data key="d0">
			<y:ShapeNode>
				<y:Geometry height="{height}" width="{width}" x="{x}" y="{y}"/>
				<y:Fill color="{fillcolor}" transparent="false"/>
				<y:BorderStyle color="#000000" type="line" width="1.0"/>
				<y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="{fontSize}" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" modelPosition="c" rotationAngle="{rotationAngle}" textColor="#000000" visible="true" >{label}</y:NodeLabel>
				<y:Shape type="{shape}"/>
            </y:ShapeNode>
		</data>		
		<data key="d1">{label}</data>
		<data key="d6">{id}</data>
	</node>
""".format(**kwargs)

    @staticmethod    
    def edge(fromId, toId, label=None, **kwargs):
        kwargs['label']=label
        kwargs['EDGE_ID']= fromId + "-" + toId
        kwargs['source'] = fromId
        kwargs['target'] = toId

        kwargs.setdefault('edge_color', '#000000')

        SOURCE="none"
        TARGET="none"
        edge_dir = kwargs.get('direction', 'right') or 'right'

        standard = 'standard'

        if edge_dir == 'left':
            SOURCE = standard
        elif edge_dir == 'right':
            TARGET = standard
        elif edge_dir == 'both':
            (SOURCE, TARGET) = (standard, standard)

        kwargs.setdefault('SOURCE', SOURCE)
        kwargs.setdefault('TARGET', TARGET)

        e = """
        <edge id="{EDGE_ID}" source="{source}" target="{target}">
            <data key="d2">
                <y:PolyLineEdge>
                    <y:LineStyle color="{edge_color}" type="line" width="1.0"/>
                    <y:Arrows source="{SOURCE}" target="{TARGET}"/>
        """.format(**kwargs)

        if label:
            e += """
                        <y:EdgeLabel alignment="center" distance="2.0" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="six_pos" modelPosition="tail" preferredPlacement="anywhere" ratio="0.5" textColor="#000000" visible="true">{label}</y:EdgeLabel>
            """.format(**kwargs)

        e += """
                    <y:BendStyle smoothed="false"/>
                </y:PolyLineEdge>
            </data>
        """.format(**kwargs)

        if label:
            e += '<data key="d3">{label}</data>'.format(label=label)
        if 'url' in kwargs:
            e += '<data key="d5"><![CDATA[{url}]]></data>'.format(**kwargs)        

        e += '</edge>'

        return e

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
        return """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
	<key for="node" id="d0" yfiles.type="nodegraphics"/>
	<key attr.name="description" attr.type="string" for="node" id="d1"/>
	<key for="edge" id="d2" yfiles.type="edgegraphics"/>
	<key attr.name="description" attr.type="string" for="edge" id="d3"/>
	<key for="graphml" id="d4" yfiles.type="resources"/>  
	<key attr.name="url" attr.type="string" for="edge" id="d5"/>
	<key attr.name="archid" attr.type="string" for="node" id="d6"/>
	<graph id="G" edgedefault="directed">
        """.format(fontname='Calibri', attrs=Helper.render_attrs(args[1], attrs, False))

    @staticmethod
    def endDiagram(*args):
        return """
	</graph>
</graphml>
"""

    @staticmethod
    def startSubdiagram(id, label, **kwargs):
        attrs = kwargs
        attrs['id'] = id
        #TODO: support fillcolor and other attributes
        return """
	<node id="sub_{id}">
		<graph id="{id}"  edgedefault="directed" >
""".format(**attrs)


    @staticmethod
    def endSubdiagram(id, label, **kwargs):
        return """
		</graph>
	</node>
"""
