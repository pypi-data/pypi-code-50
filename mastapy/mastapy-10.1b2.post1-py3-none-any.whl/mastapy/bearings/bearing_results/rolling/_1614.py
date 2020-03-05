'''_1614.py

LoadedNonBarrelRollerBearingResults
'''


from mastapy.bearings.bearing_results.rolling import _1664, _1619
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNonBarrelRollerBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonBarrelRollerBearingResults',)


class LoadedNonBarrelRollerBearingResults(_1619.LoadedRollerBearingResults):
    '''LoadedNonBarrelRollerBearingResults

    This is a mastapy class.
    '''

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedNonBarrelRollerBearingResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def smt_rib_stress(self) -> '_1664.SMTRibStressResults':
        '''SMTRibStressResults: 'SMTRibStress' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1664.SMTRibStressResults)(self.wrapped.SMTRibStress) if self.wrapped.SMTRibStress else None
