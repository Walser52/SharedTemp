
def extract_tot_energy(files):
    with open(files, 'r') as file:
        for line in file:
            if '!' in line and 'total energy' in line:
                parts = line.split("=")
                if len(parts) > 1:
                    energy = float(parts[1]. split()[0])
                    return energy
                
                
def energy_dict(files):
    energy= {}
    for label, file in files.items():
        energy[label] = extract_tot_energy(file)
    return energy



# sum of (mui) * (ni)
def extract_mu(files):
    mu = {}
    for file in files.keys():
        if '_mu' in file:
            energy = extract_tot_energy(files[file])
            element = file.split('_')[0]
            mu[element] = energy
            
    return mu


#calculate sum of (mui)*(ni)
def chem_pot(mu:dict, n:dict) -> float:
    tot_chem_pot = 0
    for element in mu:
        tot_chem_pot += mu[element] * n.get(element,0)
    return tot_chem_pot