from Bio.Seq import Seq

# Define the DNA sequence
my_dna = Seq("AGTACACTGGT")

# Find the complement of the sequence
complement = my_dna.complement()

# Print both the original sequence and its compliment
print("Original DNA Sequence:", my_dna)
print("Complement Sequence:", complement)