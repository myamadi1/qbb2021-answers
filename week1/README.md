mkdir week1
mate README.md
conda install - c bioconda jellyfish conda install spades mummer

## **Question 1a: How long is the reference genome?

ref.fa is the reference genome file
first command: samtools faidx ~/Downloads/asm/ref.fa
This generates another file
second command: mate ~/Downloads/asm/ref.fa.fai
Indicates length of the reference genome is 233806 bp

## **Question 1b: How many reads are provided and how long are they?

first command: fastqc ~/Downloads/asm/frag180.1.fq ~/Downloads/asm/frag180.2.fq ~/Downloads/asm/jump2k.fq ~Downloads/asm/jump2k.fq

This command generated a folder for each file which I opened the fastqc_data.txt file to get the following values 

frag180.1.fg : 35178 sequences that are 100bp
frag180.2.fg : 35178 sequences that are 100bp
jump2k.1.fg  : 70355 sequences that are 50bp
jump2k.2.fg  : 70355 sequences that are 50bp

## **Question 1c: How much coverage do you expect to have

You can estimate coverage by dividing total basepairs of reads by the total length of the reference genome

Frag180 files: (35178 sequences)(100bp) = 3517800 bp = (3517800/233806) = 15.046x coverage

jump2k files: (70355 sequences)(50bp) = 3517750 bp = (3517750/233806) = 15.046x coverage

## **Question 1d: Plot average quality value across the length of reads

See uploaded screenshots

example
cp ~/Downloads/asm/frag180.2_fastqc/images/per-base-quality-frag180.2.png ~/qbb2021-answers/week1
did this for each file and git pushed them

## **Question 2a: How many kmers occur exactly 50 times

first command: jellyfish count -m 21 -C -s 1000000 ~/Downloads/asm/*.fq 
second command: jellyfish histo mer_counts.jf > reads.histo
third command: mate reads.histo
Shows histogram points revealing 1030 21 kmers occur 50 times

## **Question 2b: What are the top 10 most frequently occurring kmers

first command: jellyfish dump -c mer_counts.jf | sort -n -r -k 2 | head

jellyfish dump puts kmer counts into a binary format
-n uses numerical value to sort by counts
-r to reverse sort so that we can see the highest counts at the top
-k 2 sort by the second field (counts)

GCCCACTAATTAGTGGGCGCC 104
CGCCCACTAATTAGTGGGCGC 104
CCCACTAATTAGTGGGCGCCG 104
ACGGCGCCCACTAATTAGTGG 102
AACAGGCCAGCTTATAAGCTG 100
ACAGGCCAGCTTATAAGCTGG 99
CAGGCCAGCTTATAAGCTGGC 96
AGGCCAGCTTATAAGCTGGCC 94
AGCATCGCCCACATGTGGGCG 82
GCATCGCCCACATGTGGGCGA 80

## **Question 2c: What is the estimated genome size based on the kmer frequencies?

Based on the Genome Haploid Length (from GeneomeScope) the estimated genome size based on the kmer frequencies is between 233,510bp and 233,799 bp

## **Question 2d: How well does the GenomeScope genome size estimate compare to the reference genome?

The GenomeScope estimate is less than the reference genome but only by a few basepairs

## **Question 3a: How many contigs were produced? 

First command: spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31 

Second command: grep -c '>' contigs.fasta

Showed 4 contigs were produced

## **Question 3b: What is the total length of the contigs?

first command: cd ~/Downloads/asm/asm (where spades output was sent)
second command: samtools faidx contigs.fasta
third command: mate denovo.py (pushed to github)
samtools made an index of contigs.fasta denovo.py makes the index into a pandas data frame to be able to sum it and determine the total length of the contigs

Total length of contigs = 234467

## **Question 3c: What is the size of your largest contig?

command: sort contigs.fasta.fai -n | head > contigs.sorted.fasta.fai

Size of largest contig: 105830 bp

## **Question 3d: What is the contig N50 size?

see N50.py script (pushed to github)
N50 = 47860

## **Question 4a: What is the average identity of your assembly compared to the reference? 

first command: dnadiff ref.fa asm/contigs.fasta
second command: mate out.report

AlignedSeqs = 100%
AlignedBases = 99.70%
Average Identity = 100

## **Question 4b: What is the longest alignment?

first command: show-coords out.delta

[S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
  127965   233794  |        1   105830  |   105830   105830  |    99.99  |Halomonas	NODE_1_length_105830_cov_20.649108
   40651    88510  |        1    47860  |    47860    47860  |   100.00  | Halomonas	NODE_2_length_47860_cov_20.367392
       3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas	NODE_3_length_41351_cov_20.528098
   26790    40641  |    27500    41351  |    13852    13852  |   100.00  | Halomonas	NODE_3_length_41351_cov_20.528098
   88532   127957  |        1    39426  |    39426    39426  |   10
   
Longest alignment is Node_1 105830 bp

## **Question 4c: How many insertions and deletions are in the assembly?

command: mate out.report

								 [REF]                [QRY]
Insertions                         5                    1

The assmbly has one insertion relative to the reference, and because it has 4 less insertions than the reference that means it also has 4 deletions. 

## **Question 5a: What is the position of the insertion in your assembly? Provide the corresponding position in the reference

command: show-coords out. delta
(see above table from question 4b)

The position of the insertion:
	Query sequence: 26788 - 27499
	Ref sequence: 26790 - 27498

## **Question 5b: How long is the novel insertion?

712

From above: (27499-26788)+1 = 712

## **Question 5c: What is the DNA sequence of the encoded message? 

first command:samtools faidx ~/Downloads/asm/asm/contigs.fasta  NODE_3_length_41351_cov_20.528098:26788-27499

CGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATGT
CTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAATG
CATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAGA
CAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTAT
CTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATCG
CGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACACG
AATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGGC
GGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCCG
AGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTTA
GGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTGG
AGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATTA
GCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTA


second command: samtools faidx ~/Downloads/asm/asm/contigs.fasta  NODE_3_length_41351_cov_20.528098:26788-27499 > node3insertion

put insertion sequence in a text file called node3insertion


## **Question 5d: What is the secret message? 

command: python dna-decode.py -d --input ~/Downloads/asm/node3insertion

Congratulations to the 2021 CMDB @ JHU class!  Keep on looking for little green aliens...



