# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:55:09 2021

@author: emman
"""
from Personne import Personne
from Genetique import Genetique

listPersonne = []
phrase = "salut à tous, c'est lasalle"

gene = Genetique(phrase,500)

gene.selection(phrase)
gene.getList(phrase);

# for Personne in listPersonne:
#     print("|",Personne.getGenetique(),"|") 

 
# new_personne = Personne(len(phrase))
# print("|",listPersonne[80].getGenetique(),"|")
# print(listPersonne[80].fitness(phrase))

# for y in range(0,500):
#      print(listPersonne[y].fitness(phrase))
     

    