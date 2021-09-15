#N50 measurement is the sequence length of the shortest contig at 50% of the total genome length


import pandas as pd

#import sorted_contigs
sorted_contigs = pd.read_csv('~/Downloads/asm/asm/contigs.sorted.fasta.fai', sep = '\t', header = None, names = ['name','size',2,3,4])

#divide genome size by 2 to get the 50% of the total genome length
total_genome = 233806
genome_half = total_genome/2
running_length = 0

for item in sorted_contigs['size']:
    running_length = running_length+item
    if running_length >= (total_genome/2):
        print("N50 is:")
        print(item)
        break





