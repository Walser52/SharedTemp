
#1. scf (done)
#2. Generate unklist.
    #Input desired path
#3. 


desired_path = [
          ([0,0,0], 30),
          ([0,0.5,0], 30),
]


#input -> scf.out file path. 
# Extract input_unklist parameters from scf.out.
# ase : read_espresso_out. 
inputs = {
 'input_unklist': #Read frpm scf.out
  'TRMAT': [[2,0,0], [0,2,0], [0,0,2]],
  'UNKPTS': desired_path
 
} #save inputs to file: unklist.in


def unfolder(inputs):
  #run_command: unklist.x unlist.in
  #copy K_POINT card/namelist to nscf bands. 
  #run_command: pw.x for nscf bands.
  #run_command: unfold.x on unfold.in
  return
