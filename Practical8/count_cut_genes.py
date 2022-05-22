import os
import re
os.chdir('/Users/cora/IBI1_2021-22/IBI1_2021-22/Practical8/')
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
new=open('filename.fa','w')
seqs=[]
for line in file:
    seqs.append(line.replace('\n',''))
file.close()
sum=''
for seq in seqs:
    sum+=(str(seq))
sum=re.split(r'>',sum)
n=1
for n in range(1,len(sum)):
    name=re.findall(r'gene:.+?/s',sum[n])   
    gene=str(re.findall(r'](.+)',sum[n]))
    gene=gene.strip('[')
    gene=gene.strip(']')
    number=gene.count('GAATTC')
    new.write(str(name)+'   '+str(number)) 
    n+=1
new.close()
