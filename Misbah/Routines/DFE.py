# read scf.out, extract energy and store it in a var
# write program for mu 
# sxdefectalign and epsilon.x calcs

from DFE_module import extract_tot_energy, extract_mu, chem_pot, energy_dict

# files= ['pwscf.out', 'pwscf copy.out']
files = {
    'pristine': 'pwscf.out',
    'defected': 'pwscf copy.out',
    'Pb_mu' : 'pwscf copy.out',
    'Zn_mu' : 'pwscf.out'
}

n = {
    'Pb' : -1,
    'Zn':   5  
}


tot_energy = energy_dict(files)
print(tot_energy)
# extract mu
mu_elements = extract_mu(files)
print(mu_elements)

#calculate sum of (mui)*(ni)

tot_chem_pot = chem_pot(mu_elements, n)
print(tot_chem_pot)



