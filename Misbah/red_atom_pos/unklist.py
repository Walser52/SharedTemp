import re
from ase import Atoms
from ase.cell import Cell

scf_out="pwscf.out"


def extract_ibrav_celldm(scf_out):
    
    """Extracts bravais-lattice index and celldm values from scf.out file"""
    ibrav=None

    with open(scf_out, "r", encoding="utf-8") as f:
        content=f.read()
    match = re.search(r"bravais-lattice index\s*=\s*([\d-]+)",content)
                # if match:
    ibrav=int(match.group(1))
    
    celldm={}
            
    matches = re.findall(r"celldm\((\d+)\)\s*=\s*([\d\.Ee+-]+)", content)
    for index, value in matches:
        celldm[int(index)]=float(value)
            
    return ibrav, celldm
ibrav, celldm = extract_ibrav_celldm(scf_out)
print(f"ibrav={ibrav}")
for i in sorted(celldm.keys()):
    print(f"celldm({i})={celldm[i]:.6f}")
    
    
