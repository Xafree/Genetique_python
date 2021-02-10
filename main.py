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
nombrePersonne = 500
phrase = "salut à tous, c'est lasalle"
print("La phrase a trouver et :",phrase)


gene = Genetique(phrase,nombrePersonne,listPersonne)

listPersonne = gene.selection(phrase,0.3)
gene.toString(listPersonne,countGeneration)

while countGeneration != 500:
   
   listeNewGen = gene.crossover(listPersonne)
   
   for i in range(0,len(listeNewGen)):
       listeNewGen[i].mutation(phrase)
   for y in range(len(listeNewGen),nombrePersonne,1):
       New_personne = Personne(len(phrase))
       listeNewGen.append(New_personne)
   countGeneration += 1  
   gene.toString(listPersonne,countGeneration)   
   gene.updateList(listeNewGen)
   listPersonne = gene.selection(phrase,0.5)



# while listPersonne[1] != phrase:
#     gene.selection(phrase)
#     
#     while len(listeNewGen) < 500:
#         listeGen = gene.crossover()
#         for i in range(0,len(listeGen)):
#             listeGen[i].mutation(phrase)
#             listeNewGen.append(listeGen[i].mutation(phrase))
    
#     listPersonne = listeNewGen
#     countGeneration+=1;
    



















# for Personne in listPersonne:
#     print("|",Personne.getGenetique(),"|") 

 
# new_personne = Personne(len(phrase))
# print("|",listPersonne[80].getGenetique(),"|")
# print(listPersonne[80].fitness(phrase))

# for y in range(0,2,1):
#       print(listPersonne[y].fitness(phrase))
     

    