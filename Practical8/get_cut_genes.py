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
seqs=''
for seq in seqs:
    seqs+=(str(seq))
seqs=re.split(r'>',seqs)
# identify sequence
n=1
for n in range(1,len(seqs)):
    if re.search('GAATTC',seqs[n]):
       name=re.findall(r'gene:(.+?)\s',seqs[n])
       gene=re.findall(r'].+',seqs[n])
       gene=gene.strip(']')
       len=len(gene)
       new.write('>',str(name),'   ',len)
       new.write(gene)
new.close()

