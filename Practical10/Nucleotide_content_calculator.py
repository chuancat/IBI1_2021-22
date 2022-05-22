def NC_calculator(nc):
    s=nc.upper()
    l=len(s)
    a=s.count('A')/l
    g=s.count('G')/l
    c=s.count('C')/l
    t=s.count('T')/l
    print('A is '+str(a))
    print('G is '+str(g))
    print('C is '+str(c))
    print('T is '+str(t))    
NC_calculator('ACGTGTCGTCA')     
