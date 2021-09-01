
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
    
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

q_fasta = open(arg1)
t_fasta = open(arg2)
kmer_len = int(arg3)

q_fasta_list = FASTAReader(q_fasta)
t_fasta_list = FASTAReader(t_fasta)

query_dna = q_fasta_list[0][1]

#print(q_fasta_list)

def kmerize(sequence, kmer_len):
    kmer_dict = {}
    for i in range(len(sequence)-kmer_len +1):
        kmer = sequence [i:i+kmer_len]
        if kmer in kmer_dict:
            kmer_dict[kmer].append(i)
        else:
            kmer_dict[kmer]=[i]
    return kmer_dict

query_kmers = (kmerize(query_dna, kmer_len))

for tseq in t_fasta_list:
    target_name = t_fasta_list[0]
    target_dna = t_fasta_list[1]
    target_kmers = kmerize(target_dna, kmer_len)
    #for q_kmer, q_pos in query_kmers.items()
    for q_kmer in query_kmers:
        q_pos = query_kmers[q_kmer]
        if q_kmer in target_kmers: 
            print(target_name, t_kmers[q_kmer], q_pos)
        
    
    

