# Function: calculate the total number of pizza slices that can be cut 
# from an increasing number of straight cut
# check if (n**2+n+2)/2<64
# if yes: let n equals n+1 
# if no: let (n**2+n+2)/2 equals to p
#        display the number of cuts required for 64 slices

n=1
while (n**2+n+2)/2<64:    
      n+=1
      p=(n**2+n+2)/2
print("The number of cuts required for 64 slices is "+str(n))
      
