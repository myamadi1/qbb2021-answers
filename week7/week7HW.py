import numpy as np
import pandas as pd
import sys

#FASTA reader
def FASTAReader(file):
    # Get the first line, which should contain the sequence name
    line = file.readline()

    # Let's make sure the file looks like a FASTA file
    assert line.startswith('>'), "Not a FASTA file"
    
    # Get the sequence name
    seq_id = line[1:].rstrip('\r\n')

    # create a list to contain the 
    sequence = []

    # Get the next line
    line = file.readline()

    # Add a list to hold all of the sequences in
    sequences = []

    # Keep reading lines until we run out
    while line:
        # Check if we've reached a new sequence (in a multi-sequence file)
        if line.startswith('>'):
            # Add previous sequence to list
            sequences.append((seq_id, ''.join(sequence)))
            
            # Record new sequence name and reset sequence
            seq_id = line[1:].rstrip('\r\n')
            sequence = []
        else:
            # Add next chunk of sequence
            sequence.append(line.strip())
        
        # Get the next line
        line = file.readline()
    # Add the last sequence to sequences
    sequences.append((seq_id, ''.join(sequence)))

    return sequences

#FASTA
arg1 = sys.argv[1]

#Matrix
arg2 = sys.argv[2]

#Gap penalty for gaps in the alignment
gap_penalty = float(sys.argv[3])

#Filepath for the alignment
path = sys.argv[4]

#call FASTA reader
sequence = FASTAReader(open(arg1))

#pull out two sequences in the alignment
seq1 = sequence[0][1]
seq2 = sequence[1][1]
seq1_len = len(seq1)
seq2_len = len(seq2)

# print(seq1)
# print(seq2)

#read matrix file in to pd Dataframe
matrix = pd.read_csv(sys.argv[2], delim_whitespace = True, index_col=0)

#print(matrix)

#F-matrix
F_matrix = np.zeros((len(seq1)+1, len(seq2)+1))

#print(F_matrix)

#Traceback matrix
TB_matrix = np.empty((len(seq1)+1, len(seq2)+1), dtype = str)

#print(TB_matrix)

#first column
for i in range(seq1_len+1):
    F_matrix[i,0] = i*gap_penalty

#first row
for j in range(seq2_len+1):
    F_matrix[0,j] = j*gap_penalty

#print(F_matrix)

#Populating the matrices

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        d = F_matrix[i-1, j-1] + matrix.loc[seq1[i-1], seq2[j-1]]
        h = F_matrix[i, j-1] + gap_penalty
        v = F_matrix[i-1, j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)

        #diagonal
        if max(d,h,v) == d:
            TB_matrix[i, j] = 'd'
        #left
        elif max(d,h,v) == h:
            TB_matrix[i, j] = 'h'
        #up
        elif max(d,h,v) == v:
            TB_matrix[i, j] = 'v'

#print(F_matrix)
#print(TB_matrix)

#Generate Alignment
i, j = (len(seq1), len(seq2))

align1 = ''
align2 = ''

gap1_count = 0
gap2_count = 0

while i >= 1 and j >= 1: 
    if TB_matrix[i,j] == 'd':
        align1 += seq1[i-1] 
        align2 += seq2[j-1]
        i = i - 1
        j = j - 1
    elif TB_matrix[i,j] == 'h':
        align1 += seq1[i-1]
        align2 += '-'
        j = j - 1
        gap2_count += 1
    elif TB_matrix[i,j] == 'v':
        align1 += '-'
        align2 += seq2[j-1]
        i = i - 1
        gap1_count += 1
    else:
        break

align1 = align1[::-1]
align2 = align2[::-1]

alignment_score = F_matrix[len(seq1), len(seq2)] + gap1_count + gap2_count

output = open(path, "w")
output.write("Sequence 1: ")
output.write(align1)
output.write("\n")
output.write("Sequence 2: ")
output.write(align2)
output.write("\n")
output.write("Number of gaps in sequence 1: ")
output.write(str(gap1_count))
output.write("\n")
output.write("Number of gaps in sequence 2: ")
output.write(str(gap2_count))
output.write("\n")
output.write("Alignment score: ")
output.write(str(alignment_score))
output.close

