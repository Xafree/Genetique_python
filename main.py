# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:55:09 2021

@author: emman
"""
from Personne import Personne
from Genetique import Genetique
listeNewGen = []
listPersonne = []
countGeneration = 1
phrase = "salut à tous, c'est lasalle"
print( " La phrase a trouver et :" ,phrase)


for i in range(0,500):
    New_personne = Personne(len(phrase))
    listPersonne.append(New_personne)


gene = Genetique(phrase,500,listPersonne)

while listPersonne[1] != phrase:
    gene.selection(phrase)
    gene.getList(phrase,countGeneration);
    while len(listeNewGen) < 500:
        listeGen = gene.crossover()
        for i in range(0,len(listeGen)):
            listeNewGen.append(listeGen[i].mutation(phrase))
    
    listPersonne = listeNewGen
    countGeneration+=1;
    



















# for Personne in listPersonne:
#     print("|",Personne.getGenetique(),"|") 

 
# new_personne = Personne(len(phrase))
# print("|",listPersonne[80].getGenetique(),"|")
# print(listPersonne[80].fitness(phrase))

# for y in range(0,2,1):
#       print(listPersonne[y].fitness(phrase))
     

    