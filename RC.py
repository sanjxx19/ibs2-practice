def reverse_complement(dna_sequence):
    reverse_complement = ""
    for base in dna_sequence:
        if base == "A":
            reverse_complement += "T"
        elif base == "T":
            reverse_complement += "A"
        elif base == "C":
            reverse_complement += "G"
        elif base == "G":
            reverse_complement += "C"
    return reverse_complement

dna_sequence = "ACGTACGTACGT"
print(reverse_complement(dna_sequence))