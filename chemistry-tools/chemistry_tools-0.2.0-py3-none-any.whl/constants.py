#!/usr/bin/env python
#
#  constants.py
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import logging

API_BASE = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug'

log = logging.getLogger('pubchempy')
log.addHandler(logging.NullHandler())

text_types = str, bytes

ELEMENTS = {
		1: 'H',
		2: 'He',
		3: 'Li',
		4: 'Be',
		5: 'B',
		6: 'C',
		7: 'N',
		8: 'O',
		9: 'F',
		10: 'Ne',
		11: 'Na',
		12: 'Mg',
		13: 'Al',
		14: 'Si',
		15: 'P',
		16: 'S',
		17: 'Cl',
		18: 'Ar',
		19: 'K',
		20: 'Ca',
		21: 'Sc',
		22: 'Ti',
		23: 'V',
		24: 'Cr',
		25: 'Mn',
		26: 'Fe',
		27: 'Co',
		28: 'Ni',
		29: 'Cu',
		30: 'Zn',
		31: 'Ga',
		32: 'Ge',
		33: 'As',
		34: 'Se',
		35: 'Br',
		36: 'Kr',
		37: 'Rb',
		38: 'Sr',
		39: 'Y',
		40: 'Zr',
		41: 'Nb',
		42: 'Mo',
		43: 'Tc',
		44: 'Ru',
		45: 'Rh',
		46: 'Pd',
		47: 'Ag',
		48: 'Cd',
		49: 'In',
		50: 'Sn',
		51: 'Sb',
		52: 'Te',
		53: 'I',
		54: 'Xe',
		55: 'Cs',
		56: 'Ba',
		57: 'La',
		58: 'Ce',
		59: 'Pr',
		60: 'Nd',
		61: 'Pm',
		62: 'Sm',
		63: 'Eu',
		64: 'Gd',
		65: 'Tb',
		66: 'Dy',
		67: 'Ho',
		68: 'Er',
		69: 'Tm',
		70: 'Yb',
		71: 'Lu',
		72: 'Hf',
		73: 'Ta',
		74: 'W',
		75: 'Re',
		76: 'Os',
		77: 'Ir',
		78: 'Pt',
		79: 'Au',
		80: 'Hg',
		81: 'Tl',
		82: 'Pb',
		83: 'Bi',
		84: 'Po',
		85: 'At',
		86: 'Rn',
		87: 'Fr',
		88: 'Ra',
		89: 'Ac',
		90: 'Th',
		91: 'Pa',
		92: 'U',
		93: 'Np',
		94: 'Pu',
		95: 'Am',
		96: 'Cm',
		97: 'Bk',
		98: 'Cf',
		99: 'Es',
		100: 'Fm',
		101: 'Md',
		102: 'No',
		103: 'Lr',
		104: 'Rf',
		105: 'Db',
		106: 'Sg',
		107: 'Bh',
		108: 'Hs',
		109: 'Mt',
		110: 'Ds',
		111: 'Rg',
		112: 'Cp',
		113: 'ut',
		114: 'uq',
		115: 'up',
		116: 'uh',
		117: 'us',
		118: 'uo',
		}

# Allows properties to optionally be specified as underscore_separated, consistent with Compound attributes
PROPERTY_MAP = {
		'molecular_formula': 'MolecularFormula',
		'molecular_weight': 'MolecularWeight',
		'canonical_smiles': 'CanonicalSMILES',
		'isomeric_smiles': 'IsomericSMILES',
		'inchi': 'InChI',
		'inchikey': 'InChIKey',
		'iupac_name': 'IUPACName',
		'xlogp': 'XLogP',
		'exact_mass': 'ExactMass',
		'monoisotopic_mass': 'MonoisotopicMass',
		'tpsa': 'TPSA',
		'complexity': 'Complexity',
		'charge': 'Charge',
		'h_bond_donor_count': 'HBondDonorCount',
		'h_bond_acceptor_count': 'HBondAcceptorCount',
		'rotatable_bond_count': 'RotatableBondCount',
		'heavy_atom_count': 'HeavyAtomCount',
		'isotope_atom_count': 'IsotopeAtomCount',
		'atom_stereo_count': 'AtomStereoCount',
		'defined_atom_stereo_count': 'DefinedAtomStereoCount',
		'undefined_atom_stereo_count': 'UndefinedAtomStereoCount',
		'bond_stereo_count': 'BondStereoCount',
		'defined_bond_stereo_count': 'DefinedBondStereoCount',
		'undefined_bond_stereo_count': 'UndefinedBondStereoCount',
		'covalent_unit_count': 'CovalentUnitCount',
		'volume_3d': 'Volume3D',
		'conformer_rmsd_3d': 'ConformerModelRMSD3D',
		'conformer_model_rmsd_3d': 'ConformerModelRMSD3D',
		'x_steric_quadrupole_3d': 'XStericQuadrupole3D',
		'y_steric_quadrupole_3d': 'YStericQuadrupole3D',
		'z_steric_quadrupole_3d': 'ZStericQuadrupole3D',
		'feature_count_3d': 'FeatureCount3D',
		'feature_acceptor_count_3d': 'FeatureAcceptorCount3D',
		'feature_donor_count_3d': 'FeatureDonorCount3D',
		'feature_anion_count_3d': 'FeatureAnionCount3D',
		'feature_cation_count_3d': 'FeatureCationCount3D',
		'feature_ring_count_3d': 'FeatureRingCount3D',
		'feature_hydrophobe_count_3d': 'FeatureHydrophobeCount3D',
		'effective_rotor_count_3d': 'EffectiveRotorCount3D',
		'conformer_count_3d': 'ConformerCount3D',
		}


class CoordinateType:
	TWO_D = 1
	THREE_D = 2
	SUBMITTED = 3
	EXPERIMENTAL = 4
	COMPUTED = 5
	STANDARDIZED = 6
	AUGMENTED = 7
	ALIGNED = 8
	COMPACT = 9
	UNITS_ANGSTROMS = 10
	UNITS_NANOMETERS = 11
	UNITS_PIXEL = 12
	UNITS_POINTS = 13
	UNITS_STDBONDS = 14
	UNITS_UNKNOWN = 255


class ProjectCategory:
	MLSCN = 1
	MPLCN = 2
	MLSCN_AP = 3
	MPLCN_AP = 4
	JOURNAL_ARTICLE = 5
	ASSAY_VENDOR = 6
	LITERATURE_EXTRACTED = 7
	LITERATURE_AUTHOR = 8
	LITERATURE_PUBLISHER = 9
	RNAIGI = 10
	OTHER = 255


# The following from periodictable
# public domain data
# Author: Paul Kienzle

avogadro_number = 6.02214179e23  # (30) mol-1
plancks_constant = 4.13566733e-15  # (10) eV s
electron_volt = 1.602176487e-19  # (40) J / eV
speed_of_light = 299792458  # m/s (exact)
electron_radius = 2.8179402894e-15  # (58) m

# From NIST Reference on Constants, Units, and Uncertainty
#   http://physics.nist.gov/cuu/index.html
# neutron mass = 1.008 664 915 97(43) u
# atomic mass constant m_u = 1.660 538 782(83) x 10-27 kg
neutron_mass = 1.00866491597  # u
atomic_mass_constant = 1.660538782e-27  # (83) kg / u
