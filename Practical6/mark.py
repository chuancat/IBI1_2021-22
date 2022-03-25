# create a list of mark
# sort the list
# display the sorted list
 
mark = [45,36,86,57,53,92,65,45]
L = sorted(mark)
print(L)

#function:boxplot
#import module
import numpy as np
import matplotlib.pyplot as plt
#import parameter
n = 8
mark = (45, 36, 86, 57, 53, 92, 65, 45)
plt.boxplot(mark,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = True,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False  
               )
plt.show()

#pass
#calculate the average mark
#check  if it is higher than 60
# if yes: print pass
# if no: print fail
mark = [45, 36, 86, 57, 53, 92, 65, 45]
avg = sum(mark)/len(mark)
if avg>=60:
   print("pass")
else:
   print("fail")
     
