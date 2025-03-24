from ase.io import read, write

atoms = read("vcrelax.out", format="espresso-out")
write("relaxed_structure.cif", atoms)
