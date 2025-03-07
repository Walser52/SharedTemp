from ase.io import read
from ase.spacegroup import Spacegroup
import numpy as np
from ase.data import chemical_symbols

# Read structure from vcrelax.out
atoms = read("vcrelax.out")

# Get atomic positions and numbers
all_sites = atoms.get_scaled_positions()  # Fractional coordinates
all_Z = atoms.get_atomic_numbers()  # Atomic numbers

# Ask user for space group number
spg_number = int(input("Enter space group number: "))
spg = Spacegroup(spg_number)

# Helper function to round fractional coordinates
def round_coords(site, decimals=6):
    return tuple(np.round(site, decimals=decimals))

# Store unique sites
red_sites = []
red_Z = []

for i, site in enumerate(all_sites):
    # Generate symmetry-equivalent positions
    eq_sites = spg.equivalent_sites(site)[0]
    eq_sites_rounded = [round_coords(s) for s in eq_sites]
    
    # Check if any equivalent site is already in reduced list
    if not any(s in red_sites for s in eq_sites_rounded):
        red_sites.append(round_coords(site))
        red_Z.append(all_Z[i])

# Convert atomic numbers to symbols
symbols = [chemical_symbols[num] for num in red_Z]

# Print results
# Print results
print("\nSymmetry-inequivalent sites:")
for site in red_sites:
    print(tuple(float(x) for x in site))  # Convert np.float64 to regular float


print("\nTotal unique sites:", len(red_sites))
print("Elements:", symbols)

# Define output file name
output_filename = "symmetry_inequivalent_atoms.txt"

# Write to file
with open(output_filename, "w") as f:
    f.write("ATOMIC_POSITIONS crystal_sg\n")
    for elem, site in zip(symbols, red_sites):
        f.write(f"{elem:<3}  {site[0]:.10f}  {site[1]:.10f}  {site[2]:.10f}\n")

print(f"Output written to {output_filename}")

