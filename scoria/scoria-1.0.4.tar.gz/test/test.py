import scoria

filename = "1pzo_ligand.pdbqt"
filename = "1pzo.pdbqt"

mol = scoria.Molecule()
mol.load_pdbqt_into(filename, False)
mol.assign_elements_from_atom_names()

# mol.assign_masses()
mol.create_bonds_by_distance(True, True)

print(mol.get_bonds())

# print()

# print(mol.get_atom_information()[0]["resname"])
# print(mol.belongs_to_protein(0))
# print(mol.belongs_to_dna(1))
# print(mol.belongs_to_rna(3))

# import pdb; pdb.set_trace()
