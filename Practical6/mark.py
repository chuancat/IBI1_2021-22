# create a list of mark
# sort the list
# display the sorted list
 
mark = [45,36,86,57,53,92,65,45]
L = sorted(mark)
print(L)

#function:boxplot
import numpy as np
import matplotlib.pyplot as plt
n = 8
mark = (45, 36, 86, 57, 53, 92, 65, 45)
plt.title('Rob's marks')
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
