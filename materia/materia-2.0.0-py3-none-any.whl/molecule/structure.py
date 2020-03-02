from __future__ import annotations
from typing import Dict, IO, Optional, Tuple, Union

# import collections
import contextlib
import itertools
import numpy as np
import materia
from materia.utils import memoize
import networkx as nx
import openbabel as ob
import pubchempy as pcp
import rdkit, rdkit.Chem, rdkit.Chem.AllChem
import scipy.linalg
import tempfile

__all__ = ["Structure"]


class Structure:
    def __init__(self, atoms: materia.Atom) -> None:
        self.atoms = tuple(atoms)

    @staticmethod
    def read(filepath: str) -> Structure:
        """
        Read structure from a file.

        Args:
            filepath: Path to file from which the structure will be read. Can be an absolute or a relative path.

        Returns:
            materia.Structure: Structure object based on file contents.

        Raises:
            ValueError: If structure file extension is not recognized.
        """
        if filepath.endswith(".xyz"):
            return _read_xyz(filepath=filepath)
        else:
            raise ValueError("Cannot read file with given extension.")

    def __add__(self, other: materia.Structure) -> materia.Structure:
        return materia.Structure((*self.atoms, *other.atoms))

    def perceive_bonds(self) -> Dict[int, int]:
        # FIXME: change this to bonds and add @property decorator
        obmol = ob.OBMol()

        bonds = {k: [] for k in range(self.num_atoms)}

        for a in self.atoms:
            obatom = ob.OBAtom()
            obatom.SetAtomicNum(a.Z)
            obatom.SetVector(*a.position.squeeze())
            obmol.AddAtom(obatom)

        obmol.ConnectTheDots()
        obmol.PerceiveBondOrders()

        # bonds = collections.defaultdict(list)
        for bond in ob.OBMolBondIter(obmol):
            a, b = bond.GetBeginAtomIdx() - 1, bond.GetEndAtomIdx() - 1
            bonds[a].append(b)
            bonds[b].append(a)

        return bonds  # dict(bonds)

    def to_graph(self) -> nx.Graph:
        g = nx.Graph()

        bonds = self.perceive_bonds()

        g.add_edges_from([(i, j) for i, v in bonds.items() for j in v])

        nx.set_node_attributes(
            G=g, values={i: {"Z": Z} for i, Z in enumerate(self.atomic_numbers)}
        )
        # nx.set_edge_attributes(
        #     G=g, values={e: {"dist": v} for e, v in zip(edges, com_distances)}
        # )

        return g

    @staticmethod
    def retrieve(
        name: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        inchikey: Optional[str] = None,
    ) -> materia.Structure:
        kwargs = (
            (name, "name"),
            (smiles, "smiles"),
            (inchi, "inchi"),
            (inchikey, "inchikey"),
        )
        try:
            identifier, identifier_type = next(
                (k, v) for k, v in kwargs if k is not None
            )
        except StopIteration:
            raise ValueError(
                "Identifier (name, SMILES, InChi, or InChiKey) must be provided to retrieve structure."
            )
        try:
            # this just picks the first returned compound; if there are multiple, we are assuming that the first such compound is the "most relevant" in some sense
            cid, *_ = pcp.get_cids(identifier, identifier_type)
            if cid == 0:
                raise ValueError
        except (ValueError, OSError):
            raise ValueError(f"Structure retrieval for {identifier} failed.")

        try:
            return _structure_from_pubchem_compound(
                compound=pcp.Compound.from_cid(cid, record_type="3d")
            )
        except pcp.NotFoundError:
            # no 3d structure from pubchem; there must be a 2d structure since a cid was found
            [property_dict] = pcp.get_properties(
                properties="IsomericSMILES", identifier=cid, namespace="cid"
            )
            return Structure.generate(smiles=property_dict["IsomericSMILES"])

    @staticmethod
    def generate(
        name: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        inchikey: Optional[str] = None,
    ) -> materia.Structure:
        kwargs = (
            (name, "name"),
            (smiles, "smiles"),
            (inchi, "inchi"),
            (inchikey, "inchikey"),
        )
        try:
            identifier, identifier_type = next(
                (k, v) for k, v in kwargs if k is not None
            )
        except StopIteration:
            raise ValueError(
                "Identifier (name, SMILES, InChi, or InChiKey) must be provided to generate structure."
            )

        if identifier_type == "smiles":
            return _structure_from_identifier(smiles=smiles)
        elif identifier_type == "inchi":
            return _structure_from_identifier(inchi=inchi)
        else:
            raise ValueError(f"Structure generation for {identifier} failed.")

    def write(self, file: Union[str, IO], overwrite: Optional[bool] = False) -> None:
        """
        Write structure to a file.

        Args:
            file: Path to file to which the structure will be written. Can be an absolute or a relative path.
            
            overwrite: If False, an error is raised if `filepath` already exists and the structure is not written. Ignored if `file` is a file-like object. Defaults to False.
        """
        open_code = "w" if overwrite else "x"
        with open(materia.expand(file), open_code) if isinstance(
            file, str
        ) else contextlib.nullcontext(file) as f:
            if f.name.endswith(".xyz"):
                s = self.to_xyz()
            else:
                raise ValueError("Cannot write to file with given extension.")

            try:
                f.write(s)
            except TypeError:
                f.write(s.encode())

            f.flush()

    @contextlib.contextmanager
    def tempfile(self, suffix: str, dir: Optional[str] = None):
        with tempfile.NamedTemporaryFile(
            dir=materia.expand(dir) if dir is not None else None, suffix=suffix
        ) as fp:
            try:
                self.write(file=fp)
                yield fp
            finally:
                pass

    def to_xyz(self) -> str:
        return f"{self.num_atoms}\n\n" + "\n".join(
            f"{atom} {x} {y} {z}"
            for atom, (x, y, z) in zip(self.atomic_symbols, self.atomic_positions.T)
        )

    def to_rdkit(self) -> rdkit.Chem.rdchem.Mol:
        # FIXME: segfaults due to xyz2molUSE
        with self.tempfile(suffix=".xyz") as fp:
            rdkit_mol = materia.utils.xyz2molUSE(fp.name)
        return rdkit_mol

    @property
    def num_atoms(self) -> int:
        return len(self.atoms)

    @property
    @memoize
    def atomic_symbols(self) -> Tuple[str]:
        return tuple(atom.atomic_symbol for atom in self.atoms)

    @property
    @memoize
    def atomic_positions(self) -> materia.Qty:
        value = np.hstack([atom.position for atom in self.atoms])
        unit_set = set(atom.position.unit for atom in self.atoms)
        try:
            (unit,) = tuple(unit_set)
        except ValueError:
            raise ValueError("Atomic positions do not have a common unit.")

        return materia.Qty(value=value, unit=unit)

    @property
    @memoize
    def atomic_numbers(self) -> Tuple[int]:
        return tuple(atom.Z for atom in self.atoms)

    @property
    @memoize
    def atomic_masses(self) -> materia.Qty:
        value = tuple(atom.mass.value for atom in self.atoms)
        unit_set = set(atom.mass.unit for atom in self.atoms)
        try:
            (unit,) = tuple(unit_set)
        except ValueError:
            raise ValueError("Atomic masses do not have a common unit.")

        return materia.Qty(value=value, unit=unit)

    @property
    @memoize
    def mass(self) -> materia.Qty:
        value = sum(self.atomic_masses.value)
        unit = self.atomic_masses.unit

        return materia.Qty(value=value, unit=unit)

    @property
    @memoize
    def center_of_mass(self) -> materia.Qty:
        value = (
            sum(
                m * r
                for m, r in zip(self.atomic_masses.value, self.atomic_positions.value.T)
            ).reshape(3, 1)
            / self.mass.value
        )
        unit = self.atomic_positions.unit

        return materia.Qty(value=value, unit=unit)

    @property
    @memoize
    def centered_atomic_positions(self) -> materia.Qty:
        return self.atomic_positions - self.center_of_mass

    @property
    @memoize
    def inertia_tensor(self) -> materia.Qty:
        atomic_masses = self.atomic_masses
        centered_atomic_positions = self.centered_atomic_positions

        xx, xy, xz, yy, yz, zz = (
            np.dot(atomic_masses.value, a * b)
            for a, b in itertools.combinations_with_replacement(
                centered_atomic_positions.value, r=2
            )
        )

        I = np.zeros((3, 3))
        I[np.tril_indices(3, -1)] = -xy, -xz, -yz
        I += I.T
        I += np.diag([yy + zz, xx + zz, xx + yy])

        unit = atomic_masses.unit * centered_atomic_positions.unit ** 2

        return materia.Qty(value=I, unit=unit)

    @property
    @memoize
    def inertia_aligned_atomic_positions(self) -> materia.Qty:
        # FIXME: examine and clean this one up
        principal_moments, principal_directions = scipy.linalg.eigh(
            self.inertia_tensor.value
        )

        if (
            principal_moments == np.array([0, 0, 0])
        ).all():  # i.e. this is an atomic species
            return np.eye(3)

        sorted_moments, sorted_directions = zip(
            *sorted(zip(principal_moments, principal_directions.T), reverse=True)
        )
        u, v, _ = sorted_directions

        u /= scipy.linalg.norm(u)
        v /= scipy.linalg.norm(v)
        z = np.array([[0, 0, 1]]).T
        y = np.array([[0, 1, 0]]).T
        x = np.array([[1, 0, 0]]).T
        axis = np.cross(u.T, z.T).T
        c = np.dot(u.T, z)  # cosine of the angle between u and z
        u1, u2, u3 = np.ravel(axis)
        K = np.array([[0, -u3, u2], [u3, 0, -u1], [-u2, u1, 0]])
        s = np.sqrt(1 - c ** 2)
        Ru = (np.eye(3) + s * K + (1 - c) * (K @ K)).astype("float64")
        axis = np.cross((Ru @ v).T, y.T).T
        axis /= scipy.linalg.norm(axis)
        c = np.dot((Ru @ v).T, y)  # cosine of the angle between Ru@v and y
        u1, u2, u3 = np.ravel(axis)
        K = np.array([[0, -u3, u2], [u3, 0, -u1], [-u2, u1, 0]])
        s = np.sqrt(1 - c ** 2)
        Rv = (np.eye(3) + s * K + (1 - c) * (K @ K)).astype("float64")
        R = Rv @ Ru

        print([[x for x in v] for v in R])

        Rp = np.hstack([y, z, x]) @ np.linalg.inv(
            np.hstack(
                [u.reshape(3, 1), v.reshape(3, 1), np.cross(u.T, v.T).reshape(3, 1)]
            )
        )

        print([[x for x in v] for v in Rp])
        print(R @ u)
        print(R @ v)
        print(Rp @ u)
        print(Rp @ v)
        print(R @ R.T)
        print(Rp @ Rp.T)

        return materia.Qty(
            value=R @ self.centered_atomic_positions.value,
            unit=self.centered_atomic_positions.unit,
        )

    # @property
    # @memoize
    # def atomic_lines(self):
    #     # FIXME: do we need to make sure that only linearly independent lines are returned?
    #     lines = ((a1.position.value - a2.position.value).reshape(3,) for a1,a2 in itertools.combinations(self.atoms,r=2))
    #
    #     return set(tuple(line/np.linalg.norm(line)) for line in lines)
    #
    # @property
    # @memoize
    # def atomic_planes(self):
    #     # FIXME: do we need to make sure that only linearly independent plane normals are returned?
    #     plane_normals = (np.cross((a1.position.value-a2.position.value).reshape(3,),(a2.position.value-a3.position.value).reshape(3,)) for a1,a2,a3 in itertools.combinations(self.atoms,r=3))
    #
    #     return set(tuple(normal/np.linalg.norm(normal)) for normal in plane_normals)

    @property
    @memoize
    def principal_moments(self) -> materia.Qty:
        return materia.Qty(
            scipy.linalg.eigvalsh(self.inertia_tensor), self.inertia_tensor.unit
        )

    @property
    @memoize
    def principal_axes(self) -> Tuple[float]:
        _, axes = scipy.linalg.eigh(self.inertia_tensor)
        return tuple(materia.normalize(ax) for ax in axes.T)

    @property
    @memoize
    def is_linear(self) -> bool:
        (m1, m2, m3) = self.principal_moments.value / sum(self.principal_moments.value)
        return (
            (m1 == 0 and m2 == m3) or (m2 == 0 and m1 == m3) or (m3 == 0 and m1 == m2)
        )

    @property
    @memoize
    def is_planar(self) -> materia.Qty:
        (m1, m2, m3) = self.principal_moments.value / sum(self.principal_moments.value)
        return (m1 + m2 == m3) or (m1 + m2 == m3) or (m1 + m2 == m3)

    @property
    @memoize
    def diameter(self) -> materia.Qty:
        hull = scipy.spatial.ConvexHull(self.atomic_positions.value)
        # only look at atoms on the convex hull
        kdt = scipy.spatial.KDTree(self.atomic_positions.value[hull.vertices, :])
        return materia.Qty(
            max(kdt.sparse_distance_matrix(kdt, np.inf).values()),
            self.atomic_positions.unit,
        )
        # return maximum pairwise distance among all atoms on the convex hull

    # FIXME: fix this, annotation too
    @property
    @memoize
    def pointgroup(self):
        sf = materia.symfinder.SymmetryFinder()
        return sf.molecular_pointgroup(
            atomic_positions=self.atomic_positions.value,
            atomic_numbers=self.atomic_numbers,
        )

    # FIXME: fix this, annotation too
    @property
    @memoize
    def maximally_symmetric_spanning_set(self):
        """
        Finds a set of vectors which span R^3 and which are related to one another
        as much as possible by symmetry operations of the molecule whose
        atomic species and atomic positions are given by xyz.

        Parameters
        ----------
        xyz : XYZ
            XYZ object containing the atomic species and atomic_positions of the molecule
            whose maximally symmetric spanning set is to be computed.

        Returns
        -------
        dict
            Dictionary containing three entries: axes, whose value is a list
            containing the vectors in the maximally symmetric spanning set;
            number_of_equivalent_axes, whose value is the number of axes in the
            spanning set which are related to one another by a symmetry rotation;
            and wprime.
        """
        axgen = materia.symfinder.AxesGenerator()

        return axgen.generate_axes(
            pointgroup_symbol=self.pointgroup, inertia_tensor=self.inertia_tensor
        )


# ----- IO helper functions ----- #


def _read_xyz(filepath: str, coordinate_unit: str = "angstrom") -> Structure:
    with open(materia.expand(filepath), "r") as f:
        atom_data = np.atleast_2d(
            np.loadtxt(
                fname=f,
                usecols=(0, 1, 2, 3),
                skiprows=1,
                max_rows=int(next(f)),
                dtype=str,
            )
        )

    atomic_symbols = atom_data[:, 0]
    atomic_positions = (
        materia.Qty(
            value=np.asarray(p, dtype="float64"), unit=getattr(materia, coordinate_unit)
        )
        for p in atom_data[:, 1:]
    )
    atoms = (
        materia.Atom(element=symbol, position=position)
        for symbol, position in zip(atomic_symbols, atomic_positions)
    )

    return Structure(atoms=atoms)


# def _write_sdf(structure, filepath):
# import rdkit


def _structure_from_pubchem_compound(compound: pcp.Compound) -> materia.Structure:
    # FIXME: assumes the pubchem distance unit is angstrom - is this correct??
    atom_generator = (
        (a.element, materia.Qty(value=(a.x, a.y, a.z), unit=materia.angstrom))
        for a in compound.atoms
    )
    atoms = (materia.Atom(element=symb, position=pos) for symb, pos in atom_generator)

    return materia.Structure(atoms=atoms)


def _structure_from_identifier(
    smiles: Optional[str] = None, inchi: Optional[str] = None, num_conformers: int = 25
) -> materia.Structure:
    # for motivation on generating 25 (as opposed to, say, 10 or 100) conformers, see:
    # https://github.com/rdkit/UGM_2015/blob/master/Presentations/ETKDG.SereinaRiniker.pdf

    if smiles is not None:
        mol = rdkit.Chem.MolFromSmiles(smiles, sanitize=False)
    elif inchi is not None:
        mol = rdkit.Chem.MolFromInchi(inchi, sanitize=False)
    else:
        raise ValueError("Either SMILES or InChi required to generate structure.")

    # sanitize
    try:
        mol.UpdatePropertyCache(False)
        mol = rdkit.Chem.Mol(mol.ToBinary())
        rdkit.Chem.SanitizeMol(mol)
    except ValueError:
        raise ValueError("Cannot sanitize RDKit molecule.")

    # hydrogenate
    mol = rdkit.Chem.AddHs(mol)

    # embed to generate 3D coords
    embedding_parameters = rdkit.Chem.AllChem.ETKDG()
    embed_return_code = rdkit.Chem.AllChem.EmbedMolecule(
        mol=mol, params=embedding_parameters
    )

    if embed_return_code == -1:
        embedding_parameters.useRandomCoords = True
        rdkit.Chem.AllChem.EmbedMolecule(mol=mol, params=embedding_parameters)

    # embed multiple conformers and find one with lowest energy
    rdkit.Chem.AllChem.EmbedMultipleConfs(
        mol, numConfs=num_conformers, params=embedding_parameters
    )

    # MMFF seems to give slightly better geometries, so it is preferred if possible
    if rdkit.Chem.AllChem.MMFFHasAllMoleculeParams(mol=mol):
        mmff_props = rdkit.Chem.AllChem.MMFFGetMoleculeProperties(mol=mol)
        rdkit.Chem.AllChem.MMFFSanitizeMolecule(mol=mol)
        energy = lambda conformer: rdkit.Chem.AllChem.MMFFGetMoleculeForceField(
            mol=conformer.GetOwningMol(),
            pyMMFFMolProperties=mmff_props,
            confId=conformer.GetId(),
        ).CalcEnergy()
    else:
        energy = lambda conformer: rdkit.Chem.AllChem.UFFGetMoleculeForceField(
            mol=conformer.GetOwningMol(), confId=conformer.GetId()
        ).CalcEnergy()

    energies = {conformer: energy(conformer) for conformer in mol.GetConformers()}

    conformer = min(energies, key=energies.get)

    # convert to materia.Structure
    symbols = (a.GetSymbol() for a in conformer.GetOwningMol().GetAtoms())

    # FIXME: assumes the RDKIT distance unit is angstrom - is this correct??
    # NOTE: using conformer.GetPositions sometimes causes a seg fault (RDKit) - use GetAtomPosition instead
    atoms = (
        materia.Atom(
            element=symbol,
            position=materia.Qty(
                value=conformer.GetAtomPosition(i), unit=materia.angstrom
            ),
        )
        for i, symbol in enumerate(symbols)
    )

    return materia.Structure(atoms=atoms)


# def sanitize(self):
# 	"""
# 	   This code belongs to James Davidson and is discussed here:
#
# 	   http://www.mail-archive.com/rdkit-discuss@lists.sourceforge.net/msg01185.html
# 	   http://www.mail-archive.com/rdkit-discuss@lists.sourceforge.net/msg01162.html
# 	   http://www.mail-archive.com/rdkit-discuss@lists.sourceforge.net/msg01900.html
# 	"""
# 	try:
# 		self.mol.UpdatePropertyCache(False)
# 		from_binary = rdkit.Chem.Mol(self.mol.ToBinary())
# 		rdkit.Chem.SanitizeMol(from_binary)
# 		self.mol = from_binary
# 	except ValueError:
# 		try:
# 			self._AdjustAromaticNs()
# 			rdkit.Chem.SanitizeMol(nm)
# 			self.mol = nm
# 		except ValueError:
# 			raise ValueError('Cannot sanitize RDKit molecule.')
#
#
#
# def _AdjustAromaticNs(self, nitrogenPattern='[n&D2&H0;r5,r6]'):
# 	"""
#        default nitrogen pattern matches Ns in 5 rings and 6 rings in order to be able
#        to fix: O=c1ccncc1
# 	"""
# 	rdkit.Chem.GetSymmSSSR(self.mol)
# 	self.mol.UpdatePropertyCache(False)
#
#     # break non-ring bonds linking rings:
# 	em = rdkit.Chem.EditableMol(self.mol)
# 	linkers = self.mol.GetSubstructMatches(rdkit.Chem.MolFromSmarts('[r]!@[r]'))
# 	plsFix = set()
# 	for a,b in linkers:
# 		em.RemoveBond(a,b)
# 		plsFix.add(a)
# 		plsFix.add(b)
# 	nm = em.GetMol()
# 	for at in plsFix:
# 		at = nm.GetAtomWithIdx(at)
# 		if at.GetIsAromatic() and at.GetAtomicNum() == 7:
# 			at.SetNumExplicitHs(1)
# 			at.SetNoImplicit(True)
#
#     # build molecules from the fragments:
# 	frags = (self._FragIndicesToMol(oMol=nm,indices=x) for x in rdkit.Chem.GetMolFrags(nm))
#
#     # loop through the fragments in turn and try to aromatize them:
# 	for i,frag in enumerate(frags):
# 		frag_mol = rdkit.Chem.Mol(frag)
# 		try:
# 			rdkit.Chem.SanitizeMol(frag_mol)
# 		except ValueError:
# 			matches = tuple(x[0] for x in frag.GetSubstructMatches(rdkit.Chem.MolFromSmarts(nitrogenPattern)))
# 			lres,indices = self._recursivelyModifyNs(mol=frag,matches=matches)
# 			if not lres:
# 				raise ValueError('Could not aromatize fragments.')
# 			else:
# 				revMap = {v: k for k,v in frag._idxMap.items()}
# 				for idx in indices:
# 					oatom = self.mol.GetAtomWithIdx(revMap[idx])
# 					oatom.SetNoImplicit(True)
# 					oatom.SetNumExplicitHs(1)
#
# def _FragIndicesToMol(self, oMol, indices):
#     em = rdkit.Chem.EditableMol(rdkit.Chem.Mol())
#
#     newIndices = {}
#     for i,idx in enumerate(indices):
#         em.AddAtom(oMol.GetAtomWithIdx(idx))
#         newIndices[idx] = i
#
#     for i,idx in enumerate(indices):
#         at = oMol.GetAtomWithIdx(idx)
#         for bond in at.GetBonds():
#             if bond.GetBeginAtomIdx() == idx:
#                 oidx = bond.GetEndAtomIdx()
#             else:
#                 oidx = bond.GetBeginAtomIdx()
#             # make sure every bond only gets added once:
#             if oidx < idx:
#                 continue
#             em.AddBond(newIndices[idx],newIndices[oidx],bond.GetBondType())
#     res = em.GetMol()
#     res.ClearComputedProps()
#     rdkit.Chem.GetSymmSSSR(res)
#     res.UpdatePropertyCache(False)
#     res._idxMap = newIndices
#
#     return res
#
# def _recursivelyModifyNs(self, mol, matches, indices=None):
#     if indices is None:
#         indices = []
#     res = None
#     while len(matches) and res is None:
#         tIndices = indices[:]
#         nextIdx = matches.pop(0)
#         tIndices.append(nextIdx)
#         nm = rdkit.Chem.Mol(mol)
#         nm.GetAtomWithIdx(nextIdx).SetNoImplicit(True)
#         nm.GetAtomWithIdx(nextIdx).SetNumExplicitHs(1)
#         cp = rdkit.Chem.Mol(nm)
#         try:
#             rdkit.Chem.SanitizeMol(cp)
#         except ValueError:
#             res,indices = self._recursivelyModifyNs(mol=nm,matches=matches,indices=tIndices)
#         else:
#             indices = tIndices
#             res = cp
#     return res, indices
