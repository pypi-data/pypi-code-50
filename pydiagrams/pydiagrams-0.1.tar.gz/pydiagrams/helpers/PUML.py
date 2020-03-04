from pydiagrams.helpers.constants import *
from pydiagrams.helpers import helper 


# Map of shapes
helper.shape = {
        'Cloud':'cloud',
        'Database':'database',
        'Folder':'folder',
        'Frame':'frame',
        'Node':'node',
        'Package':'package',
        'Rectangle':'rectangle',    
        'Component':'component',
        'Interface':'interface',
        'Diamond':'interface',

        # Views
        'Table'         :   'rectangle',
        'View'          :   'rectangle',
        'Package'       :   'package',
        'File'          :   'folder',
        'Integration'   :   'interface',
        'System'        :   'cloud',
        'Task'          :   'component'
    }

helper.comment_format = "' {text}\n"

class Helper(helper.helper):
    """ 
    The Helper class stores the methods specific to a diagram language.
    It's passed to the FlowchartBase object to be used when rendering code
    """

    extension   = "puml"
    name = "PUML"

    arrows = {
         'vertical'   : '-->',
         'horizontal' : '->',
         'right'    : '-right->',
         'left'     : '-left->',
         'up'       : '-up->',
         'down'     : '-down->',
         'hline'    : '-',
         'vline'    : '--',
         'vdotted'  : '..>'
        }


    @staticmethod
    def node(id, label, **kwargs):
        #eg: interface "[DR3] Customer Review Authorisation" as rms_cra
        n = Helper.shape(kwargs.get('shape', 'rectangle'))
        if label or label != '':            
            n += ' "{}"'.format(label)
        n += ' as {} '.format(id)

        if kwargs.has_key(fillcolor):
            FILLCOLOR=kwargs[fillcolor]
            if not FILLCOLOR.startswith('#'):
                n += '#'
            n += FILLCOLOR

        if kwargs.has_key('note'):
            n += '\nnote right of {id}\n{note}\nend note'.format(id=id, note=kwargs['note'])
        return n

    @staticmethod
    def edge(fromId, toId, label=None, **kwargs):
        #TODO: Support directional arrows

        dir = kwargs.get('dir', None)

        if not dir:
            dir = 'vertical'

        edge = '{} {} {}'.format(fromId, Helper.arrows[dir], toId)

        if label:
            edge += ' : ' + label

        return edge

    @staticmethod
    def startDiagram(*args):
        """ Called first during the render to initialise a diagram """
        return """@startuml {filename}
!include w:\\plantuml\\theme-blue.iuml
        """.format(filename=args[0])

    @staticmethod
    def endDiagram(*args):
        """ Called last uring the render to finalise a diagram """
        return "@enduml"


    @staticmethod
    def startSubdiagram(id, label, **kwargs):
        shape=Helper.shape(kwargs.get('shape', 'rectangle'))
        #label=kwargs.get('label')
        
        
        t = shape
        if label and label != '':
            t += ' "{}" '.format(label)

        color=str(kwargs.get('fillcolor', ""))
        if color:
            if not color.startswith('#'):
                t += '#' 
            t += str(color)

        #return '{shape} "{label}" {color} {{\n'.format(shape=shape, label=label, color=color)
        return t + ' {\n'

    @staticmethod
    def endSubdiagram(id, label, **kwargs):
        return "\n}} \n".format(id=id)