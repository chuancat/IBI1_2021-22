# I met many difficulties and I learnt from classmates a lot
from xml.dom.minidom import parse 
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
print ('There are '+str(len(terms))+' terms.')

dic={}
for term in terms:
    is_as=[]
    for i in term.getElementsByTagName('is_a'):
        is_as.append(i.childNodes[0].data)
    ids=term.getElementsByTagName('id')[0].childNodes[0].data
    for is_a in is_as:
        if is_a in dic:
           dic[is_a].append(ids)
        else:
           dic[is_a]=[ids]

def number(list0):
    for i in list0:
        if i in list0:
           if i not in list1:
              list1.append(i)
              if i in dic:
                 number(dic[i])
        return len(list1)

total_list=[]
translation_list=[]
for term in terms:
    childnodes=0
    list1=[]
    ids=term.getElementsByTagName('id')[0].childNodes[0].data
    if ids in dic:
       childnodes=number(dic[ids])
       total_list.append(childnodes)
       if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:  
          translation_list.append(childnodes)

# first chart
plt.boxplot(total_list,
            labels=['GO'])
plt.title('childNodes distribution of term')
plt.ylabel('the number of childNodes')
plt.show()

# second chart
plt.boxplot(translation_list,labels=['translation GO'])
plt.title('childNodes distribution diagram of term related to translation')
plt.ylabel('childNodes number')
plt.xlabel('all GO terms')
plt.show()

aver1=sum(total_list)/len(total_list)
aver2=sum(translation_list)/len(translation_list)
if aver1>aver2:
   print("The translation terms contain, on average, a smaller number of childNodes than the overall Gene Ontology.")
else:
    print("The translation terms contain, on average, a greater number of childNodes than the overall Gene Ontology.")
