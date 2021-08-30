bootcamp

1a: mkdir day1-lunch
1b: nano README.md 
1c: cp /Users/cmdb/qbb2021/data/*bed .
1c: cp /Users/cmdb/qbb2021/data/dm6.chrom.sizes .
1d: ls -l > directory.txt
2a: wc -l *.bed < feature_count.txt
2c: There are less features for K9/4 methylation than K27 methylation this could indicate that there is more gene repression than activation in this data set. Given that the total number of methylated features is less than half the features of the total number of genes would suggest that over half the genes aren't methylated
3a: sort fbgenes.bed | cut -f 1 | uniq -c > fbgenes.info
3c: The y chromosome and the mitochondrial DNA have the least number of genes. The chromosome 2R and 3R have the most genes

