##Step 1: Index the sacCer3 genome

bwa index sacCer3.fa

##Step 2: Align your reads against the sacCer3 reference genome

1: bwa mem -R "@RG\tID:Sample9\tSM:Sample9" -t4 sacCer3.fa A01_09.fastq > aln-se9.sam
2: bwa mem -R "@RG\tID:Sample11\tSM:Sample11" -t4 sacCer3.fa A01_11.fastq >aln-se11.sam
3: bwa mem -R "@RG\tID:Sample23\tSM:Sample23" -t4 sacCer3.fa A01_23.fastq >aln-se23.sam
4: bwa mem -R "@RG\tID:Sample24\tSM:Sample24" -t4 sacCer3.fa A01_24.fastq >aln-se24.sam
5: bwa mem -R "@RG\tID:Sample27\tSM:Sample27" -t4 sacCer3.fa A01_27.fastq >aln-se27.sam
6: bwa mem -R "@RG\tID:Sample31\tSM:Sample31" -t4 sacCer3.fa A01_31.fastq >aln-se31.sam
7: bwa mem -R "@RG\tID:Sample35\tSM:Sample35" -t4 sacCer3.fa A01_35.fastq >aln-se35.sam
8: bwa mem -R "@RG\tID:Sample39\tSM:Sample39" -t4 sacCer3.fa A01_39.fastq >aln-se39.sam
9: bwa mem -R "@RG\tID:Sample62\tSM:Sample62" -t4 sacCer3.fa A01_62.fastq >aln-se62.sam
10:bwa mem -R "@RG\tID:Sample63\tSM:Sample63" -t4 sacCer3.fa A01_63.fastq >aln-se63.sam

##Step 3: Create a sorted bam file with samtools, for input to variant callers

1: samtools sort -O bam -o sample9.bam aln-se9.sam
2: samtools sort -O bam -o sample11.bam aln-se11.sam
3: samtools sort -O bam -o sample23.bam aln-se23.sam
4: samtools sort -O bam -o sample24.bam aln-se24.sam
5: samtools sort -O bam -o sample27.bam aln-se27.sam
6: samtools sort -O bam -o sample31.bam aln-se31.sam
7: samtools sort -O bam -o sample35.bam aln-se35.sam
8: samtools sort -O bam -o sample39.bam aln-se39.sam
9: samtools sort -O bam -o sample62.bam aln-se62.sam
10:samtools sort -O bam -o sample63.bam aln-se63.sam

for I in *sam; do samtools sort -O bam $I > ${I/sam/bam}; done
##Step 4: Variant calling with freebayes

-First made bam files into indexed files 

1: samtools index sample9.bam
2: samtools index sample11.bam
3: samtools index sample23.bam
4: samtools index sample24.bam
5: samtools index sample27.bam
6: samtools index sample31.bam
7: samtools index sample35.bam
8: samtools index sample39.bam
9: samtools index sample62.bam
10:samtools index sample63.bam

-Freebayes

freebayes -f sacCer3.fa *.bam > var.vcf

##Step 5: Filter variants based on genotype quality 

vcffilter -f "QUAL > 20" var.vcf > vars_filtered.vcf

##Step 6: Decompose complex haplotypes 

vcfallelicprimitives -k -g vars-filtered.vcf > var_decompose.vcf

##Step 7: Variant effect prediction 

First command: snpeff download R64-1-1.99
Second command: snpeff ann R64-1-1.86 var-decompose.vcf > vars_annotate.vcf
Third command: head -n 1000 vars-annotate.vcf > submitvars.vcf
Fourth command: grep -v '##' vars-annotate.vcf > pd_input.vcf

##Step 8: Exploratory data analysis through plotting

jupyter notebook pushed to github
1000 lines of annotated vcf (submitvars.vcf) pushed to github