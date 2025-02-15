from Bio.Seq import Seq

# Define an mRNA sequence
messenger_rna = Seq("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGAUGCCGUGUAGC")

# Perform translation
protein_sequence = messenger_rna.translate()

# Print the sequence
print("Protein sequence:", protein_sequence)