import itertools

massTable = {
    'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147,
    'G': 57, 'H': 137, 'I': 113, 'K': 128, 'L': 113,
    'M': 131, 'N': 114, 'P': 97, 'Q': 128, 'R': 156,
    'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163
}

def getMass(peptide):
    return sum(massTable[aa] for aa in peptide)

def bruteForce(massTable, min_length=1, max_length=5):
   
    amino_acids = {aa for aa, mass in massTable.items()}
    matching = []

    for length in range(min_length, max_length + 1):
        for peptide in itertools.product(amino_acids, repeat=length):
            peptide_str = ''.join(peptide) 
            matching.append(peptide_str)
    
    return matching

matching = bruteForce(massTable, min_length=1, max_length=5)

print("Matching cyclopeptides:")
print("\n".join(matching))