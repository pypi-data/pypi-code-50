'''_1965.py

Bolt
'''


from mastapy.bolts import _1041
from mastapy._internal import constructor
from mastapy.system_model.part_model import _1966, _1967
from mastapy._internal.python_net import python_net_import

_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')


__docformat__ = 'restructuredtext en'
__all__ = ('Bolt',)


class Bolt(_1967.Component):
    '''Bolt

    This is a mastapy class.
    '''

    TYPE = _BOLT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Bolt.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def loaded_bolt(self) -> '_1041.LoadedBolt':
        '''LoadedBolt: 'LoadedBolt' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1041.LoadedBolt)(self.wrapped.LoadedBolt) if self.wrapped.LoadedBolt else None

    @property
    def bolted_joint(self) -> '_1966.BoltedJoint':
        '''BoltedJoint: 'BoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1966.BoltedJoint)(self.wrapped.BoltedJoint) if self.wrapped.BoltedJoint else None
