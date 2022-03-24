#Function: calculate the triangle sequence and computes and displays the 
# first the first 10 values of the triangle sequence
#The nth number is 1+2+3+...+n
# Repeat:
#  let the nth number equals m
#  calcualte m
#  print it 
#  check if n>10
#  if yes: done
#  if no: let n+1 equals to n
n=1
for n in range(1,11):
    m = (1+n)*n/2
    print(m)
    n +=1
