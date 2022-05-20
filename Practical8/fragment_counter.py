import re 
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
# EcoRI enzymes cuts G^AATTC
cut_seq = re.split(r'GAATTC',seq)
n=len(cut_seq)
print(n)

