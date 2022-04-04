# import model, cite from the Practical7 guidance
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# change working directory to where the data is stored 
# learn the pattern from guidance, and use right pathway
os.chdir("/Users/cora/Downloads")
# use pandas library to read the content of the .csv file into a dataframe 
# object
covid_data = pd.read_csv("full_data.csv")

# function1: show the first and third columns from rows 10-20, include 10 
# and 20 
# because the first row is name and the second row's number is 0, so row 
# 10 number is 8
print(covid_data.iloc[8:19,0:4:2])

# function: show "total_cases" for all rows corresponding to Afghanistan
# read just the column "location" and all rows
# create a list represent rows Afghanistan belongs
# create a Boolean that is True when the "location" is "Afghanistan", but 
# false otherwise
# use the Boolean to find exactly the row needed in the dataframe
n = 0
my_rows = []
for n in range(0,7996):
    a = covid_data.loc[n,"location"]
    w = a == "Afghanistan"
    my_rows.append(w)
    n+=1 
my_columns = [False, False, False, False, True, False]
print(covid_data.iloc[my_rows,my_columns])

# function:compute the mean new cases and new deaths in China
# collect new cases and new deaths in China from covid_data
# use numpy to compute mean new cases and new deaths
n = 0
my_rows =[]
for n in range(0,7996):
    a = covid_data.loc[n,"location"]
    w = a == "China"
    my_rows.append(w)
    n+=1
my_columns1 = [True, False, True, True, False, False]
china = covid_data.iloc[my_rows,my_columns1]
my_columns2 = [False, True, True]
a = china.iloc[:,my_columns2]
# learn np.mean() from https://cloud.tencent.com/developer/ask/sof/1091397 
# in 2nd,Apr.
print(np.mean(a))

# function:plot the new cases and new deaths in China as a box plot
n = 0
A = []
B = []
for n in range(0,92): 
   a = china.iloc[n,1]   
   b = china.iloc[n,2]
   A.append(a)
   B.append(b)
   n+=1
Data = (A,B)
plt.boxplot(Data,
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

#function:plot new cases and new deaths in China 
plt.plot(A,'c+',B, 'y+')
plt.title('new cases and new deaths in China')
plt.xlabel('date')
plt.xticks(rotation= -90)

plt.show()
