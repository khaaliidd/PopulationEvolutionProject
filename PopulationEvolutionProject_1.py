# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:50:37 2024

@author: Khalid Hamada
"""
#___________hello world!! program_______________

#print("Hello world !!")

#__________Drawing figures syntax_______________


import matplotlib.pyplot as plt
# x=[0,1,2,3]
# y=[0,1,4,9]
# plt.figure()
# plt.plot(x,y)
# plt.savefig("courbe.png")
# plt.show()

#___________Population Evolotion Project_______________
td=float(input("td= "))
tn=float(input("tn= "))
p0=float(input(" initial popluation p0=  "))
D=int(input(" duration of evolution D= "))
tab=[]
annee=[]

for i in range(D):
    annee.append(i)
    p1=(tn-td)*p0+p0
    p0=p1
    tab.append(p1)
    
print(tab)

plt.figure()
plt.plot(annee,tab)
plt.savefig("evolution.png")
plt.show()    



