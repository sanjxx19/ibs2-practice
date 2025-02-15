massTable = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
        'C': 103, 'L': 113, 'N': 114, 'D': 115, 'Q': 128, 'E': 129, 
        'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

def getMass(combination):
    return sum([massTable[amino] for amino in combination])

def getSpectrum(peptide):
    sub_strings = sorted([peptide[i:j] for i in range(len(peptide)) for j in range(i+1, len(peptide)+1)], key=lambda x: getMass(x))
    
    theoretical_spectra = [0]
    for i in sub_strings:
        theoretical_spectra.append(getMass(i))
    theoretical_spectra.sort()
    
    return theoretical_spectra

spectrum = [0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]
k_mers = {}
k_mers[1] = list(filter(lambda x: getMass(x) in spectrum, massTable.keys()))

while True:
    temp = []
    max_mer = max(k_mers.keys())
    for mer in k_mers[max_mer]:
        amm = k_mers[1]
        for a in amm:
            if mer[-1] == a:
                continue
            com = mer + a
            if set(getSpectrum(com)).issubset(set(spectrum)):
                temp.append(com)
    temp.sort()
    k_mers[max_mer+1] = temp    

    if k_mers[max(k_mers.keys())] == []:
        break

for i in range(1,len(k_mers)):
    print(f"Consistent {i}-mers:")
    print(k_mers[i])
    print(f"Number of {i}-mers: {len(k_mers[i])}")
    print()