from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Given DNA sequences
seq1 = "AATTC"
seq2 = "ATAC"

# Scoring parameters
match = 1
mismatch = -1
gap_open = -2
gap_extend = 0

# Perform global alignment
alignments = pairwise2.align.localms(seq1, seq2, match, mismatch, gap_open, gap_extend)

# Print best alignment and score
print(format_alignment(*alignments[0]))

