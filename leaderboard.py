def LeaderboardCyclopeptideSequencing(spectrum, N):
    def calculate_mass(peptide):
        mass_table = {
            'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57,
            'H': 137, 'I': 113, 'K': 128, 'L': 113, 'M': 131, 'N': 114,
            'P': 97, 'Q': 128, 'R': 156, 'S': 87, 'T': 101, 'V': 99,
            'W': 186, 'Y': 163
        }
        return sum(mass_table[aa] for aa in peptide)

    def score(peptide, spectrum):
        theoretical_masses = []
        for i in range(len(peptide)):
            for j in range(i + 1, len(peptide) + 1):
                theoretical_masses.append(calculate_mass(peptide[i:j]))
        score = sum(1 for mass in theoretical_masses if mass in spectrum)
        return score

    def expand(leaderboard):
        expanded = []
        for peptide in leaderboard:
            for amino_acid in 'ACDEFGHIKLMNPQRSTVWY': 
                expanded.append(peptide + amino_acid)
        return expanded

    def trim(leaderboard, spectrum, N):
        scored_peptides = [(peptide, score(peptide, spectrum)) for peptide in leaderboard]
        scored_peptides.sort(key=lambda x: x[1], reverse=True)
        return [peptide for peptide, _ in scored_peptides[:N]]

    leaderboard = ['']
    leader_peptide = ''

    parent_mass = max(spectrum)
    
    while leaderboard:
        leaderboard = expand(leaderboard)
        leaderboard = [peptide for peptide in leaderboard if calculate_mass(peptide) <= parent_mass]

        for peptide in leaderboard:
            peptide_mass = calculate_mass(peptide)
            if peptide_mass == parent_mass:
                if score(peptide, spectrum) > score(leader_peptide, spectrum):
                    leader_peptide = peptide

        leaderboard = trim(leaderboard, spectrum, N)
        
    return leader_peptide

spectrum = [0, 113, 128, 185, 226, 256, 285, 342, 370, 471]  
N = len(spectrum)
result = LeaderboardCyclopeptideSequencing(spectrum, N)
print("Leader Peptide:", result)