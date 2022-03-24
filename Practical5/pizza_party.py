# Function: calculate the total number of pizza slices that can be cut 
# from an increasing number of straight cut
# calculate p with (n**2+n+2)/2
# display p
# check if p>=64
# if yes: done
# if no: let n+1 equals to n
n=1
p=(n**2+n+2)/2
while p<64:
      n+=1

print(p)
      
