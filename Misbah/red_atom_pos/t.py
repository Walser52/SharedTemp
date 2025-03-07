def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested_dict = {
    'control': {
        'calculation': 'scf',
        'etot_conv_thr': 7e-05,
        'forc_conv_thr': 0.0001,
        'outdir': '../out/',
        'prefix': 'aiida',
        'pseudo_dir': '../pseudo/',
        'tprnfor': True,
        'tstress': True,
        'verbosity': 'high'
    },
    'system': {
        'degauss': 0.146997236,
        'ecutrho': 320.0,
        'ecutwfc': 40.0,
        'space_group': 221,
        'a': 12.6019078721,
        'nat': 8,
        'nosym': False,
        'ntyp': 4,
        'occupations': 'smearing',
        'smearing': 'cold'
    },
    'electrons': {
        'conv_thr': 1.4e-09,
        'electron_maxstep': 80,
        'mixing_beta': 0.4
    },
    'ions': {
        'ion_dynamics': 'bfgs'
    },
    'cell': {
        'cell_dynamics': 'bfgs',
        'press_conv_thr': 0.05,
        'cell_dofree': 'all'
    }
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)

