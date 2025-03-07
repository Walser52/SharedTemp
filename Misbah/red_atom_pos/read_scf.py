import f90nml

def read_pwscf_input(file_path):
    """
    Reads a Quantum ESPRESSO pwscf.in file and converts it into a dictionary.

    Parameters:
        file_path (str): Path to the pwscf.in file.

    Returns:
        dict: Parsed input file as a dictionary.
    """

    nml = f90nml.read(file_path)
    return nml.todict()  # Convert to dictionary

# Example usage
file_path = "pwscf.in"
qe_input_dict = read_pwscf_input(file_path)

# Print as a dictionary
print(qe_input_dict)
