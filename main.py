# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:55:09 2021

@author: emman
"""
from Personne import Personne

listPersonne = []
phrase = "salut à tous, c'est lasalle"

for i in range(0,500):
    New_personne = Personne(len(phrase))
    listPersonne.append(New_personne)

# for Personne in listPersonne:
#     print("|",Personne.getGenetique(),"|") 

 
new_personne = Personne(len(phrase))
print("|",listPersonne[80].getGenetique(),"|")
print(listPersonne[80].fitness(phrase))

for y in range(0,500):
     print(listPersonne[y].fitness(phrase))
    