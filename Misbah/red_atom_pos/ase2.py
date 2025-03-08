from jhr.io.base import FileHandler


def QE_additional_cards_splitter(additional_cards):
  keywords = ["ATOMIC_SPECIES", "ATOMIC_POSITIONS", "K_POINTS"]
  cards_dict = FileHandler.fortran_card_splitter(additional_cards, keywords)

  for k in cards_dict.keys():
    #parse each key.
    if 'K_POINTS' in k.upper():
#     print(cards_dict[k][0].split())
      pass
  return cards_dict


def flatten_dict(d):
    """
    Flattens a nested dict by removing parents. 
    """
    items = []
    for k, v in d.items():
        new_key = f"{k}" if parent_key else k

        try:
          v = v.data
        except:
          pass

        if isinstance(v, dict):
            items.extend(flatten_dict(v).items())
        else:
            items.append((new_key, v))

    return dict(items)


input_data, additional_cards = FileHandler.read_fortran_namelists('pwscf.in')

cards_dict = QE_additional_cards_splitter(additional_cards)
flattened_dict = flatten_dict(input_data)

#import json
#with open('result.json', 'w') as fp:
#    json.dump(flattened_dict, fp)


#==============
from jhr.codes.espresso.study import BaseQENormalCalculation as QECalc
mat_file = "result.json"
code = "qe/pw.x"
update = {}


scf = QECalc(
    template=mat_file, code=code, files="scf", update=update, run=False
)


