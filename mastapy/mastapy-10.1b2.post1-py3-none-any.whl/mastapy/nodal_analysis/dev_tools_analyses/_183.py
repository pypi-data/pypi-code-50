'''_183.py

FEModel
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
    _206, _208, _207, _203,
    _209, _205, _204, _202,
    _211, _200
)
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_FE_MODEL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModel',)


class FEModel(_1.APIBase):
    '''FEModel

    This is a mastapy class.
    '''

    TYPE = _FE_MODEL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEModel.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def original_file_path(self) -> 'str':
        '''str: 'OriginalFilePath' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OriginalFilePath

    @property
    def edge_angle_tolerance(self) -> 'float':
        '''float: 'EdgeAngleTolerance' is the original name of this property.'''

        return self.wrapped.EdgeAngleTolerance

    @edge_angle_tolerance.setter
    def edge_angle_tolerance(self, value: 'float'):
        self.wrapped.EdgeAngleTolerance = float(value) if value else 0.0

    @property
    def number_of_nodes(self) -> 'int':
        '''int: 'NumberOfNodes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfNodes

    @property
    def number_of_elements(self) -> 'int':
        '''int: 'NumberOfElements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfElements

    @property
    def model_length_unit(self) -> 'str':
        '''str: 'ModelLengthUnit' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ModelLengthUnit

    @property
    def model_force_unit(self) -> 'str':
        '''str: 'ModelForceUnit' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ModelForceUnit

    @property
    def add_new_material(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddNewMaterial' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddNewMaterial

    @property
    def change_interpolation_constraints_to_distributing(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ChangeInterpolationConstraintsToDistributing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ChangeInterpolationConstraintsToDistributing

    @property
    def rigid_element_properties(self) -> 'List[_206.ElementPropertiesRigid]':
        '''List[ElementPropertiesRigid]: 'RigidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RigidElementProperties, constructor.new(_206.ElementPropertiesRigid))
        return value

    @property
    def solid_element_properties(self) -> 'List[_208.ElementPropertiesSolid]':
        '''List[ElementPropertiesSolid]: 'SolidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SolidElementProperties, constructor.new(_208.ElementPropertiesSolid))
        return value

    @property
    def shell_element_properties(self) -> 'List[_207.ElementPropertiesShell]':
        '''List[ElementPropertiesShell]: 'ShellElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShellElementProperties, constructor.new(_207.ElementPropertiesShell))
        return value

    @property
    def beam_element_properties(self) -> 'List[_203.ElementPropertiesBeam]':
        '''List[ElementPropertiesBeam]: 'BeamElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeamElementProperties, constructor.new(_203.ElementPropertiesBeam))
        return value

    @property
    def spring_dashpot_element_properties(self) -> 'List[_209.ElementPropertiesSpringDashpot]':
        '''List[ElementPropertiesSpringDashpot]: 'SpringDashpotElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDashpotElementProperties, constructor.new(_209.ElementPropertiesSpringDashpot))
        return value

    @property
    def mass_element_properties(self) -> 'List[_205.ElementPropertiesMass]':
        '''List[ElementPropertiesMass]: 'MassElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassElementProperties, constructor.new(_205.ElementPropertiesMass))
        return value

    @property
    def interface_element_properties(self) -> 'List[_204.ElementPropertiesInterface]':
        '''List[ElementPropertiesInterface]: 'InterfaceElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.InterfaceElementProperties, constructor.new(_204.ElementPropertiesInterface))
        return value

    @property
    def other_element_properties(self) -> 'List[_202.ElementPropertiesBase]':
        '''List[ElementPropertiesBase]: 'OtherElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OtherElementProperties, constructor.new(_202.ElementPropertiesBase))
        return value

    @property
    def materials(self) -> 'List[_211.MaterialPropertiesReporting]':
        '''List[MaterialPropertiesReporting]: 'Materials' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Materials, constructor.new(_211.MaterialPropertiesReporting))
        return value

    @property
    def contact_pairs(self) -> 'List[_200.ContactPairReporting]':
        '''List[ContactPairReporting]: 'ContactPairs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ContactPairs, constructor.new(_200.ContactPairReporting))
        return value
