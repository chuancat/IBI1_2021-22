# Function: calculate the total number of pizza slices that can be cut 
# from an increasing number of straight cut
# check if (n**2+n+2)/2<64
# if yes: let n+1 equals to n
# if no: let (n**2+n+2)/2 equals to p
#        display ("The number of pieces of pizza is"+ str(p))

n=1
while (n**2+n+2)/2<64:
      n+=1
      p = (n**2+n+2)/2
      
print("The number of pieces of pizza is"+ str(p))
      
