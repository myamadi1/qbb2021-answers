import sys

gtf_file = sys.argv[1]
mut_chrom = sys.argv[2]
mut_pos = int(sys.argv[3])
f = open(gtf_file)

genes = []
for line in f:
    if line.startswith("#"):
        continue
    fields = line.strip("\r\n").split("\t")
    start = int(fields[3])
    end = int(fields[4])
    if (fields[0] == mut_chrom) and (fields[2] == "gene") and ('gene_biotype "protein_coding"' in line):
        subfields = fields[-1].split(';')
        for field in subfields:
            if "gene_name" in field:
                gene_name = field.split()[1]
        genes.append((gene_name, start, end))
#print(genes)
high = len(genes) -1
low = 0
current_index = high//2
counter = 0

while True:
    counter +=1
    # current_gene = genes[current_index][0]
    current_pos = genes[current_index][1]
    if current_pos < mut_pos: 
        if low == current_index:
            high_pos = genes[high][1]
            low_pos = genes[low][1]
            if abs(high_pos - mut_pos) < abs(low_pos - mut_pos):
                print("Nearest protein coding gene:",genes[high][0]) #prints nearest protein coding gene
                print("Genomic distance:", abs(high_pos - mut_pos)) #prints gene's linear genomic distance
            else:
                print("Nearest protein coding gene:", genes[low][0])
                print("Genomic distance:", abs(low_pos - mut_pos))
            break
        low = current_index
        current_index = (high + low)//2
        
    else:
        if high == current_index:
            high_pos = genes[high][1]
            low_pos = genes[low][1]
            if abs(high_pos - mut_pos) < abs(low_pos - mut_pos):
                print("Nearest protein coding gene:", genes[high][0])
                print("Genomic distance:", abs(high_pos - mut_pos))
            else:
                print("Nearest protein coding gene:", genes[low][0])
                print("Genomic distance:", abs(low_pos - mut_pos))
            break
        high=current_index
        current_index = (high + low)//2
print("Iterations:", counter) #prints iterations it took to find the nearest gene

# print(current_gene, current_pos)
        
#gtf file is list of genes and their position in the genome sorted
#make list of genes and their positions argument tells which chromosome (above script)
#set initial high and low
#initial high = length of the list -1
#initial low = 0
#current_index = int(high/2)
#while loop specify when our stopping condition is in the while loop
#current_gene = genes[][0] 
#current_pos = genes[][1]
#check if current_pos < target position:
#low = current_index
#current_index = (high + low)//2
#else: if it's higher replace the high with current index
#else: high = current_index current_index = int((high+low)/2)




