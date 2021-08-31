import sys

#flymap = open("/Users/cmdb/qbb2021/data/fly_mapping.txt")
flymap = open(sys.argv[1], 'r')
flydict = dict()
for line in flymap:
    parsed = line.strip().split('\t')
    flydict[parsed[0]] = parsed[1] 


#ctab = open("/Users/cmdb/qbb2021/data/SRR072893.t_data.ctab")
ctab = open(sys.argv[2], 'r')
for line in ctab:
    parsed = line.strip().split('\t')
    print(parsed)
    gene_name = parsed[8]
    if gene_name in flydict:
        value = flydict[gene_name]
        print(gene_name, value)
        parsed[8]=value
        print(parsed)
    else:
        if len(sys.argv) == 4:
            parsed[8] = sys.argv[3]
            print(parsed)
        else:
            continue
