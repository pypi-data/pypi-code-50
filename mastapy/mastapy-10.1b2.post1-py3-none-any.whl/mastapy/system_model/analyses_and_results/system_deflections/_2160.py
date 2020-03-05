'''_2160.py

ConicalGearMeshSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.conical import _996, _1001, _1006
from mastapy.system_model.connections_and_sockets.gears import (
    _1797, _1789, _1791, _1793,
    _1805, _1808, _1809, _1810,
    _1813, _1815, _1817, _1821
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.conical import _449
from mastapy.gears.rating.zerol_bevel import _298
from mastapy.gears.rating.straight_bevel_diff import _324
from mastapy.gears.rating.straight_bevel import _328
from mastapy.gears.rating.spiral_bevel import _331
from mastapy.gears.rating.klingelnberg_spiral_bevel import _334
from mastapy.gears.rating.klingelnberg_hypoid import _337
from mastapy.gears.rating.klingelnberg_conical import _340
from mastapy.gears.rating.hypoid import _367
from mastapy.gears.rating.bevel import _464
from mastapy.gears.rating.agma_gleason_conical import _475
from mastapy.gears.gear_designs.zerol_bevel import _831
from mastapy.gears.gear_designs.straight_bevel_diff import _840
from mastapy.gears.gear_designs.straight_bevel import _844
from mastapy.gears.gear_designs.spiral_bevel import _848
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _852
from mastapy.gears.gear_designs.klingelnberg_hypoid import _856
from mastapy.gears.gear_designs.klingelnberg_conical import _860
from mastapy.gears.gear_designs.hypoid import _864
from mastapy.gears.gear_designs.bevel import _1027
from mastapy.gears.gear_designs.agma_gleason_conical import _1040
from mastapy.gears.ltca.conical import _763
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2162, _2132, _2139, _2140,
    _2141, _2144, _2194, _2199,
    _2202, _2205, _2231, _2237,
    _2240, _2241, _2242, _2263,
    _2188
)
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConicalGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshSystemDeflection',)


class ConicalGearMeshSystemDeflection(_2188.GearMeshSystemDeflection):
    '''ConicalGearMeshSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def delta_xp(self) -> 'float':
        '''float: 'DeltaXP' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeltaXP

    @property
    def delta_xw(self) -> 'float':
        '''float: 'DeltaXW' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeltaXW

    @property
    def delta_e(self) -> 'float':
        '''float: 'DeltaE' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeltaE

    @property
    def delta_sigma(self) -> 'float':
        '''float: 'DeltaSigma' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeltaSigma

    @property
    def loaded_flank(self) -> '_996.ActiveConicalFlank':
        '''ActiveConicalFlank: 'LoadedFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.LoadedFlank)
        return constructor.new(_996.ActiveConicalFlank)(value) if value else None

    @property
    def pinion_torque_for_ltca(self) -> 'float':
        '''float: 'PinionTorqueForLTCA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinionTorqueForLTCA

    @property
    def load_in_line_of_action_from_ltca(self) -> 'float':
        '''float: 'LoadInLineOfActionFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LoadInLineOfActionFromLTCA

    @property
    def torque_on_gear_a_due_to_force_in_line_of_action_at_mesh_node(self) -> 'float':
        '''float: 'TorqueOnGearADueToForceInLineOfActionAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueOnGearADueToForceInLineOfActionAtMeshNode

    @property
    def torque_on_gear_b_due_to_force_in_line_of_action_at_mesh_node(self) -> 'float':
        '''float: 'TorqueOnGearBDueToForceInLineOfActionAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueOnGearBDueToForceInLineOfActionAtMeshNode

    @property
    def torque_on_gear_a_due_to_moment_at_mesh_node(self) -> 'float':
        '''float: 'TorqueOnGearADueToMomentAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueOnGearADueToMomentAtMeshNode

    @property
    def torque_on_gear_b_due_to_moment_at_mesh_node(self) -> 'float':
        '''float: 'TorqueOnGearBDueToMomentAtMeshNode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueOnGearBDueToMomentAtMeshNode

    @property
    def linear_misalignment_in_surface_of_action(self) -> 'float':
        '''float: 'LinearMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LinearMisalignmentInSurfaceOfAction

    @property
    def angular_misalignment_in_surface_of_action(self) -> 'float':
        '''float: 'AngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AngularMisalignmentInSurfaceOfAction

    @property
    def pinion_angular_misalignment_in_surface_of_action(self) -> 'float':
        '''float: 'PinionAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinionAngularMisalignmentInSurfaceOfAction

    @property
    def wheel_angular_misalignment_in_surface_of_action(self) -> 'float':
        '''float: 'WheelAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WheelAngularMisalignmentInSurfaceOfAction

    @property
    def connection_design(self) -> '_1797.ConicalGearMesh':
        '''ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1797.ConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_1789.AGMAGleasonConicalGearMesh':
        '''AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1789.AGMAGleasonConicalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1789.AGMAGleasonConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_bevel_differential_gear_mesh(self) -> '_1791.BevelDifferentialGearMesh':
        '''BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1791.BevelDifferentialGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelDifferentialGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1791.BevelDifferentialGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_bevel_gear_mesh(self) -> '_1793.BevelGearMesh':
        '''BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1793.BevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1793.BevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_hypoid_gear_mesh(self) -> '_1805.HypoidGearMesh':
        '''HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1805.HypoidGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to HypoidGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1805.HypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_1808.KlingelnbergCycloPalloidConicalGearMesh':
        '''KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1808.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1808.KlingelnbergCycloPalloidConicalGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_1809.KlingelnbergCycloPalloidHypoidGearMesh':
        '''KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1809.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1809.KlingelnbergCycloPalloidHypoidGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        '''KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1810.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_spiral_bevel_gear_mesh(self) -> '_1813.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1813.SpiralBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpiralBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1813.SpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_1815.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1815.StraightBevelDiffGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelDiffGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1815.StraightBevelDiffGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_straight_bevel_gear_mesh(self) -> '_1817.StraightBevelGearMesh':
        '''StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1817.StraightBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1817.StraightBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_design_of_type_zerol_bevel_gear_mesh(self) -> '_1821.ZerolBevelGearMesh':
        '''ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1821.ZerolBevelGearMesh.TYPE not in self.wrapped.ConnectionDesign.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ZerolBevelGearMesh. Expected: {}.'.format(self.wrapped.ConnectionDesign.__class__.__qualname__))

        return constructor.new(_1821.ZerolBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def rating(self) -> '_449.ConicalGearMeshRating':
        '''ConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_449.ConicalGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_zerol_bevel_gear_mesh_rating(self) -> '_298.ZerolBevelGearMeshRating':
        '''ZerolBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _298.ZerolBevelGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_298.ZerolBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_straight_bevel_diff_gear_mesh_rating(self) -> '_324.StraightBevelDiffGearMeshRating':
        '''StraightBevelDiffGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _324.StraightBevelDiffGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelDiffGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_324.StraightBevelDiffGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_straight_bevel_gear_mesh_rating(self) -> '_328.StraightBevelGearMeshRating':
        '''StraightBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _328.StraightBevelGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_328.StraightBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_spiral_bevel_gear_mesh_rating(self) -> '_331.SpiralBevelGearMeshRating':
        '''SpiralBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _331.SpiralBevelGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_331.SpiralBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self) -> '_334.KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _334.KlingelnbergCycloPalloidSpiralBevelGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidSpiralBevelGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_334.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self) -> '_337.KlingelnbergCycloPalloidHypoidGearMeshRating':
        '''KlingelnbergCycloPalloidHypoidGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _337.KlingelnbergCycloPalloidHypoidGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidHypoidGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_337.KlingelnbergCycloPalloidHypoidGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self) -> '_340.KlingelnbergCycloPalloidConicalGearMeshRating':
        '''KlingelnbergCycloPalloidConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _340.KlingelnbergCycloPalloidConicalGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidConicalGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_340.KlingelnbergCycloPalloidConicalGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_hypoid_gear_mesh_rating(self) -> '_367.HypoidGearMeshRating':
        '''HypoidGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _367.HypoidGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to HypoidGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_367.HypoidGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_bevel_gear_mesh_rating(self) -> '_464.BevelGearMeshRating':
        '''BevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _464.BevelGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_464.BevelGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def rating_of_type_agma_gleason_conical_gear_mesh_rating(self) -> '_475.AGMAGleasonConicalGearMeshRating':
        '''AGMAGleasonConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _475.AGMAGleasonConicalGearMeshRating.TYPE not in self.wrapped.Rating.__class__.__mro__:
            raise CastException('Failed to cast rating to AGMAGleasonConicalGearMeshRating. Expected: {}.'.format(self.wrapped.Rating.__class__.__qualname__))

        return constructor.new(_475.AGMAGleasonConicalGearMeshRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def mesh_design(self) -> '_1001.ConicalGearMeshDesign':
        '''ConicalGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1001.ConicalGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_zerol_bevel_gear_mesh_design(self) -> '_831.ZerolBevelGearMeshDesign':
        '''ZerolBevelGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _831.ZerolBevelGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to ZerolBevelGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_831.ZerolBevelGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_straight_bevel_diff_gear_mesh_design(self) -> '_840.StraightBevelDiffGearMeshDesign':
        '''StraightBevelDiffGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _840.StraightBevelDiffGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to StraightBevelDiffGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_840.StraightBevelDiffGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_straight_bevel_gear_mesh_design(self) -> '_844.StraightBevelGearMeshDesign':
        '''StraightBevelGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _844.StraightBevelGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to StraightBevelGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_844.StraightBevelGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_spiral_bevel_gear_mesh_design(self) -> '_848.SpiralBevelGearMeshDesign':
        '''SpiralBevelGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _848.SpiralBevelGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to SpiralBevelGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_848.SpiralBevelGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self) -> '_852.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _852.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to KlingelnbergCycloPalloidSpiralBevelGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_852.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> '_856.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        '''KlingelnbergCycloPalloidHypoidGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _856.KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to KlingelnbergCycloPalloidHypoidGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_856.KlingelnbergCycloPalloidHypoidGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_klingelnberg_conical_gear_mesh_design(self) -> '_860.KlingelnbergConicalGearMeshDesign':
        '''KlingelnbergConicalGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _860.KlingelnbergConicalGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to KlingelnbergConicalGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_860.KlingelnbergConicalGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_hypoid_gear_mesh_design(self) -> '_864.HypoidGearMeshDesign':
        '''HypoidGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _864.HypoidGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to HypoidGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_864.HypoidGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_bevel_gear_mesh_design(self) -> '_1027.BevelGearMeshDesign':
        '''BevelGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1027.BevelGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to BevelGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_1027.BevelGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def mesh_design_of_type_agma_gleason_conical_gear_mesh_design(self) -> '_1040.AGMAGleasonConicalGearMeshDesign':
        '''AGMAGleasonConicalGearMeshDesign: 'MeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1040.AGMAGleasonConicalGearMeshDesign.TYPE not in self.wrapped.MeshDesign.__class__.__mro__:
            raise CastException('Failed to cast mesh_design to AGMAGleasonConicalGearMeshDesign. Expected: {}.'.format(self.wrapped.MeshDesign.__class__.__qualname__))

        return constructor.new(_1040.AGMAGleasonConicalGearMeshDesign)(self.wrapped.MeshDesign) if self.wrapped.MeshDesign else None

    @property
    def misalignments_pinion(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsPinion) if self.wrapped.MisalignmentsPinion else None

    @property
    def misalignments_wheel(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsWheel) if self.wrapped.MisalignmentsWheel else None

    @property
    def misalignments_total(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsTotal) if self.wrapped.MisalignmentsTotal else None

    @property
    def mesh_node_misalignments_pinion(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MeshNodeMisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MeshNodeMisalignmentsPinion) if self.wrapped.MeshNodeMisalignmentsPinion else None

    @property
    def mesh_node_misalignments_wheel(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MeshNodeMisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MeshNodeMisalignmentsWheel) if self.wrapped.MeshNodeMisalignmentsWheel else None

    @property
    def mesh_node_misalignments_total(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MeshNodeMisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MeshNodeMisalignmentsTotal) if self.wrapped.MeshNodeMisalignmentsTotal else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_imported_fe_node_total(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeTotal' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeTotal) if self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeTotal else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_imported_fe_node_pinion(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodePinion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodePinion) if self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodePinion else None

    @property
    def misalignments_with_respect_to_cross_point_using_reference_imported_fe_node_wheel(self) -> '_1006.ConicalMeshMisalignments':
        '''ConicalMeshMisalignments: 'MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeWheel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1006.ConicalMeshMisalignments)(self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeWheel) if self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceImportedFENodeWheel else None

    @property
    def ltca_results(self) -> '_763.ConicalMeshLoadDistributionAnalysis':
        '''ConicalMeshLoadDistributionAnalysis: 'LTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_763.ConicalMeshLoadDistributionAnalysis)(self.wrapped.LTCAResults) if self.wrapped.LTCAResults else None

    @property
    def gear_a(self) -> '_2162.ConicalGearSystemDeflection':
        '''ConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2162.ConicalGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2132.AGMAGleasonConicalGearSystemDeflection':
        '''AGMAGleasonConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2132.AGMAGleasonConicalGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2132.AGMAGleasonConicalGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_bevel_differential_gear_system_deflection(self) -> '_2139.BevelDifferentialGearSystemDeflection':
        '''BevelDifferentialGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2139.BevelDifferentialGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2139.BevelDifferentialGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2140.BevelDifferentialPlanetGearSystemDeflection':
        '''BevelDifferentialPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.BevelDifferentialPlanetGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2140.BevelDifferentialPlanetGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2141.BevelDifferentialSunGearSystemDeflection':
        '''BevelDifferentialSunGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.BevelDifferentialSunGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2141.BevelDifferentialSunGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_bevel_gear_system_deflection(self) -> '_2144.BevelGearSystemDeflection':
        '''BevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.BevelGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2144.BevelGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_hypoid_gear_system_deflection(self) -> '_2194.HypoidGearSystemDeflection':
        '''HypoidGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.HypoidGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to HypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2194.HypoidGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2199.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2199.KlingelnbergCycloPalloidConicalGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_spiral_bevel_gear_system_deflection(self) -> '_2231.SpiralBevelGearSystemDeflection':
        '''SpiralBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2231.SpiralBevelGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to SpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2231.SpiralBevelGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2237.StraightBevelDiffGearSystemDeflection':
        '''StraightBevelDiffGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2237.StraightBevelDiffGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2237.StraightBevelDiffGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_gear_system_deflection(self) -> '_2240.StraightBevelGearSystemDeflection':
        '''StraightBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2240.StraightBevelGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2240.StraightBevelGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2241.StraightBevelPlanetGearSystemDeflection':
        '''StraightBevelPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2241.StraightBevelPlanetGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2241.StraightBevelPlanetGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2242.StraightBevelSunGearSystemDeflection':
        '''StraightBevelSunGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2242.StraightBevelSunGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2242.StraightBevelSunGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_zerol_bevel_gear_system_deflection(self) -> '_2263.ZerolBevelGearSystemDeflection':
        '''ZerolBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2263.ZerolBevelGearSystemDeflection.TYPE not in self.wrapped.GearA.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ZerolBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_2263.ZerolBevelGearSystemDeflection)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_b(self) -> '_2162.ConicalGearSystemDeflection':
        '''ConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2162.ConicalGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2132.AGMAGleasonConicalGearSystemDeflection':
        '''AGMAGleasonConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2132.AGMAGleasonConicalGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2132.AGMAGleasonConicalGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_bevel_differential_gear_system_deflection(self) -> '_2139.BevelDifferentialGearSystemDeflection':
        '''BevelDifferentialGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2139.BevelDifferentialGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2139.BevelDifferentialGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2140.BevelDifferentialPlanetGearSystemDeflection':
        '''BevelDifferentialPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2140.BevelDifferentialPlanetGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2140.BevelDifferentialPlanetGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2141.BevelDifferentialSunGearSystemDeflection':
        '''BevelDifferentialSunGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2141.BevelDifferentialSunGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2141.BevelDifferentialSunGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_bevel_gear_system_deflection(self) -> '_2144.BevelGearSystemDeflection':
        '''BevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2144.BevelGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2144.BevelGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_hypoid_gear_system_deflection(self) -> '_2194.HypoidGearSystemDeflection':
        '''HypoidGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.HypoidGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to HypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2194.HypoidGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2199.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        '''KlingelnbergCycloPalloidConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2199.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2199.KlingelnbergCycloPalloidConicalGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2202.KlingelnbergCycloPalloidHypoidGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2205.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_spiral_bevel_gear_system_deflection(self) -> '_2231.SpiralBevelGearSystemDeflection':
        '''SpiralBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2231.SpiralBevelGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to SpiralBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2231.SpiralBevelGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2237.StraightBevelDiffGearSystemDeflection':
        '''StraightBevelDiffGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2237.StraightBevelDiffGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2237.StraightBevelDiffGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_gear_system_deflection(self) -> '_2240.StraightBevelGearSystemDeflection':
        '''StraightBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2240.StraightBevelGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2240.StraightBevelGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2241.StraightBevelPlanetGearSystemDeflection':
        '''StraightBevelPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2241.StraightBevelPlanetGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2241.StraightBevelPlanetGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2242.StraightBevelSunGearSystemDeflection':
        '''StraightBevelSunGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2242.StraightBevelSunGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2242.StraightBevelSunGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_zerol_bevel_gear_system_deflection(self) -> '_2263.ZerolBevelGearSystemDeflection':
        '''ZerolBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2263.ZerolBevelGearSystemDeflection.TYPE not in self.wrapped.GearB.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ZerolBevelGearSystemDeflection. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_2263.ZerolBevelGearSystemDeflection)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def planetaries(self) -> 'List[ConicalGearMeshSystemDeflection]':
        '''List[ConicalGearMeshSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ConicalGearMeshSystemDeflection))
        return value
