cal_molecule = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRn" \
           "FArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMg" \
           "ArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArP" \
           "TiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnF" \
           "ArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

with open("inputs/day19.txt", 'r') as fh:
    lines = fh.readlines()

transformations = {}
for line in lines:
    parts = line.rstrip().split()
    if parts[0] in transformations:
        transformations[parts[0]].append(parts[2])
    else:
        transformations[parts[0]] = [parts[2], ]


def get_new_molecules(molecule):
    new_molecules = set()
    for element in transformations:
        molecule_parts = molecule.split(element)
        for new_element in transformations[element]:
            replacements = [[element, ] * x + [new_element, ] + [element, ] * (len(molecule_parts) - 2 - x)
                            for x in range(len(molecule_parts) - 1)]
            for replacement in replacements:
                replacement.append('')
                new_molecules.add(''.join([''.join(x) for x in zip(molecule_parts, replacement)]))
    return new_molecules


available_molecules = ['e', ]
iteration = 0
while cal_molecule not in available_molecules:
    print(available_molecules)
    newly_available_molecules = []
    for available_molecule in available_molecules:
        newly_available_molecules += get_new_molecules(available_molecule)
    available_molecules = set(newly_available_molecules)
    iteration += 1
    if iteration == 5:
        break

print(iteration)



