def transcription(dna_sequence):
    transcription = ""
    for base in dna_sequence:
        if base == "T":
            transcription += "U"
        else:
            transcription += base
    return transcription

dna_sequence = "ACGTACGTACGT"
print(transcription(dna_sequence))