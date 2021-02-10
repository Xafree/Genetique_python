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
nombrePersonne = 1000
phrase = "salut à tous, c'est lasalle"
print("La phrase a trouver et :",phrase)


gene = Genetique(phrase,nombrePersonne,listPersonne)
New_personne = Personne(len(phrase))
#listPersonne.append(New_personne)

while listPersonne[0].getResistance() != len(phrase):
   #print("resistance",listPersonne[0].getResistance()) 
   #gene.toString(listPersonne,countGeneration)
   listPersonne = gene.selection(phrase,0.5)
   listeNewGen = gene.crossover(listPersonne)
   gene.toString(listPersonne,countGeneration)
   while len(listeNewGen) < 500:
       listeNewGen += gene.crossover(listPersonne)

   for i in range(0,len(listeNewGen)):
       listeNewGen[i].mutation(phrase)
    
   gene.updateList(listeNewGen)
   
   countGeneration += 1

   
   
   
   
   



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
     

    