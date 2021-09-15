import pandas as pd

index = pd.read_csv('~/Downloads/asm/asm/contigs.fasta.fai', sep = '\t', header = None, names = ['name','size',2,3,4]) #tells to organize based on name and size for all 4 contigs

print(index['size'].sum())
