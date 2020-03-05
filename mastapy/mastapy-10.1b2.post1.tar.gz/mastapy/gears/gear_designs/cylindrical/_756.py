'''_756.py

BaffleLoss
'''


from mastapy._internal import constructor
from mastapy.utility import _1122
from mastapy.gears.gear_designs.cylindrical import _820
from mastapy._internal.python_net import python_net_import

_BAFFLE_LOSS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'BaffleLoss')


__docformat__ = 'restructuredtext en'
__all__ = ('BaffleLoss',)


class BaffleLoss(_1122.IndependentReportablePropertiesBase['_820.TiffAnalysisSettings']):
    '''BaffleLoss

    This is a mastapy class.
    '''

    TYPE = _BAFFLE_LOSS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BaffleLoss.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def baffle_loss_factor(self) -> 'float':
        '''float: 'BaffleLossFactor' is the original name of this property.'''

        return self.wrapped.BaffleLossFactor

    @baffle_loss_factor.setter
    def baffle_loss_factor(self, value: 'float'):
        self.wrapped.BaffleLossFactor = float(value) if value else 0.0

    @property
    def baffle_type(self) -> 'str':
        '''str: 'BaffleType' is the original name of this property.'''

        return self.wrapped.BaffleType

    @baffle_type.setter
    def baffle_type(self, value: 'str'):
        self.wrapped.BaffleType = str(value) if value else None
