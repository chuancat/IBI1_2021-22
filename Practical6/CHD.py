# dictionary
paternal_age = {'30':1.03, '35':1.07, '40':1.11, '45':1.17, '50':1.23, 
'55':1.32, '60':1.42, '65':1.55, '70':1.72, '75':1.94}

# plt.scatter
# import necessary mudule
import numpy as np
import matplotlib.pyplot as plt
# import parameter 
N = 10 
x = (30, 35, 40, 45, 50, 55, 60, 65, 70, 75)
y = (1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94)

plt.ylabel('chd')
plt.xlabel('paternal_age')
plt.title('chd of different ages')
plt.scatter(x, y, marker='o')

plt.show()

# create a variable of the paternal age
x = 30
paternal_age = (30, 35, 40, 45, 50, 55, 60, 65, 70, 75)
risk = paternal_age[x]
print(risk)
