paternal_age = {'30':1.03, '35':1.07, '40':1.11, '45':1.17, '50':1.23, 
'55':1.32, '60':1.42, '65':1.55, '70':1.72, '75':1.94}

# import necessary mudule
import numpy as np
import matplotlib.pyplot as plt
# import 
N = 10 
chd = (1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94)
paternal_age = (30, 35, 40, 45, 50, 55, 60, 65, 70, 75)

ply.ylabel('chd')
ply.xlabel('paternal_age')
ply.title('chd of different ages')
plt.scatter(x, y, marker='o')

plt.show()
