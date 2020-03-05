'''_375.py

KlingelnbergHypoidVirtualCylindricalGear
'''


from mastapy.gears.rating.virtual_cylindrical_gears import _377
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'KlingelnbergHypoidVirtualCylindricalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergHypoidVirtualCylindricalGear',)


class KlingelnbergHypoidVirtualCylindricalGear(_377.KlingelnbergVirtualCylindricalGear):
    '''KlingelnbergHypoidVirtualCylindricalGear

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_HYPOID_VIRTUAL_CYLINDRICAL_GEAR
    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergHypoidVirtualCylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
