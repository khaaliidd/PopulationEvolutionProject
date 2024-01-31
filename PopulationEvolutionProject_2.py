# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:04:38 2024

@author: Khalid Hamada
"""


import matplotlib.pyplot as plt
# x=[0,1,2,3]
# y=[0,1,4,9]
# plt.figure()
# plt.plot(x,y)
# plt.savefig("courbe.png")
# plt.show()

# ___________Population Evolotion Project 2_______________


def croissance(p0, r, D):
    tab = []
    annee = []
    

    for i in range(D):
        annee.append(i)
        p1 = r*p0*(1-p0)
        p0 = p1
        tab.append(p1)

#print(tab)

    plt.figure()
    plt.plot(annee, tab)
    plt.savefig("evolution.png")
    plt.show()
    
    return tab
