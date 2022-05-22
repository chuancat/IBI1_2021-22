def Cba_calculator(a,b):
    """
    Input:a,the total money that the user has, a positive int
          b,the pricr of one chocolate bar, a positive int    
    """
    m=a//b
    n=a%b
    print('the number of bars that can be bought is '+str(m))
    print('the change that will be left over is '+str(n))
Cba_calculator(100,7)
    
