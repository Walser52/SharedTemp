from ase.io.espresso import Namelist
from ase.io.espresso import write_fortran_namelist

# input_data for pp.x, built automatically
#input_data = {'outdir': '/path/to/output', 'prefix': 'prefix', 'verbosity': 'high'}
#
#input_data = Namelist(input_data)
#input_data.to_nested(binary='pp')

#write_fortran_namelist('input_pp.in', input_data)


input_data = {'environ': {'environ_type': 'water'}, 'kpts': {'abc': [1,2,3]}} 

additional_cards = [
      'EXTERNAL_CHARGES (bohr)',
      '-0.5 0. 0. 25.697 1.0 2 3',
      '-0.5 0. 0. 20.697 1.0 2 3'
] # This will be added at the end of the file


with open('environ.in', "w") as f:
  write_fortran_namelist(f, input_data, additional_cards=additional_cards)
