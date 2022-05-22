import os
# get to thr fasta file directory
import re
os.chdir('/Users/cora/IBI1_2021-22/IBI1_2021-22/Practical8/')
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
# extract sequence and name
# identify sequences which can be cut by enzyme
# if yes:output the gene_name and calculate its length
new = open('cut_genes.fa','w')
seqs=[]
for line in file:
    seqs.append(line.replace('\n',''))
file.close()
# split each sequence
sum=''
for seq in seqs:
    sum+=(str(seq))
sum=re.split(r'>',sum)
# identify sequence
n=1
for n in range(1,len(sum)):
    if re.search('GAATTC',sum[n]):
       name=re.findall(r'gene:(.+?)\s',sum[n])
       gene=str(re.findall(r'](.+)',sum[n]))
       gene=gene.strip('[')
       gene=gene.strip(']')
       len=len(gene)
       new.write('>',str(name),'   ',len)
       new.write(gene)
new.close()

