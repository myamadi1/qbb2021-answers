f = open('SRR072893.sam')
linecount = 0
reads = []
for line in f:
    if not line.startswith('@'):
        linecount = linecount + 1
        parsed = line.split('\t')
        reads.append(parsed)
print(linecount) #answer to 1


f = open('SRR072893.sam')
linecount = 0
reads = []
perfectmatch = 0
mapqsum = 0
reads2L = 0
uniquereads = set()
for line in f:
    if not line.startswith('@'):
        linecount = linecount + 1
        parsed = line.strip().split('\t')
        reads.append(parsed) 
        if len(parsed[9]) != 40:
            print("Error,there's a read that's not 40 bases")
        mapqsum = mapqsum + int(parsed[4])
        average = mapqsum/linecount
        location = int(parsed[3])
        if (parsed[2] == '2L') & (location >= 10000) & (location <= 20000):
            reads2L = reads2L + 1 
        poscigar = (parsed[3],parsed[5])
        uniquereads.add(poscigar)
        
for line in reads:
    if line[5] == '40M':
        perfectmatch = perfectmatch + 1
print(perfectmatch) #answer to 2
print(average) #answer to 3
print(reads2L) #answer to 4
print(linecount - len(uniquereads)) #answer to 5







    