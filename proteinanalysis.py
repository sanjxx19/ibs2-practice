from Bio.SeqUtils.ProtParam import ProteinAnalysis

analysis = ProteinAnalysis("VKLFPWFNQY")
mw = analysis.molecular_weight()
c = analysis.get_amino_acids_percent()
ip = analysis.isoelectric_point()

print(f"Mol wt.: {mw}")
print(f"AAC: {c}")
print(f"Isoelectric point: {ip}")
print(analysis.aromaticity())
print(analysis.count_amino_acids())