import numpy as np

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    m, n = len(seq1), len(seq2)
    
    score_matrix = np.zeros((m+1, n+1))
    
    for i in range(m+1):
        score_matrix[i][0] = i * gap
    for j in range(n+1):
        score_matrix[0][j] = j * gap
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch
            
            score_matrix[i][j] = max(
                score_matrix[i-1][j-1] + score,
                score_matrix[i-1][j] + gap,
                score_matrix[i][j-1] + gap
            )
    
    print(score_matrix)
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = m, n
    
    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and (score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)) == current_score:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            i -= 1
            j -= 1
        elif i > 0 and (score_matrix[i-1][j] + gap) == current_score:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1
    
    return aligned_seq1, aligned_seq2, score_matrix[m][n]

seq1 = "ATGCT"
seq2 = "AGCT"
alignment1, alignment2, score = needleman_wunsch(seq1, seq2)

print(alignment1)
print(alignment2)
print("Score:", score)