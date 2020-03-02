from nwbn_conversion_tools.gui.classes.forms_basic import BasicFormFixed, BasicFormCollapsible
from ndx_fret import FRET, FRETSeries


class GroupFRET(BasicFormCollapsible):
    def __init__(self, parent, metadata=None):
        """Groupbox for abc.FRET fields filling form."""
        super().__init__(parent=parent, pynwb_class=FRET, metadata=metadata)

    def fields_info_update(self):
        """Updates fields info with specific fields from the inheriting class."""
        specific_fields = [
            {'name': 'donor',
             'type': 'group',
             'class': 'FRETSeries',
             'required': True,
             'doc': 'Group storing donor data'},
            {'name': 'acceptor',
             'type': 'group',
             'class': 'FRETSeries',
             'required': True,
             'doc': 'Group storing acceptor data'}
        ]
        self.fields_info.extend(specific_fields)


class GroupFRETSeries(BasicFormFixed):
    def __init__(self, parent, metadata=None):
        """Groupbox for abc.FRETSeries fields filling form."""
        super().__init__(parent=parent, pynwb_class=FRETSeries, metadata=metadata)

    def fields_info_update(self):
        """Updates fields info with specific fields from the inheriting class."""
        specific_fields = [
            {'name': 'device',
             'type': 'link',
             'class': 'Device',
             'required': True,
             'doc': 'The device that was used to record'},
            {'name': 'optical_channel',
             'type': 'group',
             'class': 'OpticalChannel',
             'required': True,
             'doc': 'One of possibly many groups storing channels pecific data'}
        ]
        self.fields_info.extend(specific_fields)
