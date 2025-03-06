from ase.io import read
from ase.spacegroup import Spacegroup
import numpy as np
from ase.data import chemical_symbols

# Read the CIF file into an Atoms object
atoms = read("CsPbI3_3x3x3.cif")

# Get all scaled positions and atomic numbers
all_sites = atoms.get_scaled_positions()  # (N, 3) array
all_Z = atoms.get_atomic_numbers()          # length N

red_sites = []  # will store rounded fractional coordinates as tuples
red_Z = []

# Initialize the spacegroup (here, space group number 221)
spg = Spacegroup(221)

# Helper function to round coordinates
def round_coords(site, decimals=6):
    return tuple(np.round(site, decimals=decimals))


#eq_sites = spg.equivalent_sites(all_sites[0])  # returns a list of arrays
#print(eq_sites[0])
#exit()
# Loop over each site using its index so we can also add the atomic number
for i, site in enumerate(all_sites):
    eq_sites = spg.equivalent_sites(site)[0]  # returns a list of arrays
    eq_sites_rounded = [round_coords(s, decimals=6) for s in eq_sites]
    
    # If any equivalent site is already in our reduced list, skip this site
    flag = False
    for s in eq_sites_rounded:
      #print(s)
      if s in red_sites:
        flag = True

    if flag:
      continue
    else:
      print(s)
      red_sites.append(round_coords(site, decimals=6))
      red_Z.append(all_Z[i])

symbols = [chemical_symbols[num] for num in red_Z]
print(len(red_sites))
print(symbols)
