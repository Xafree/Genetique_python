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
phrase = "mathématique pour l'informatique"
print("La phrase a trouver et :",phrase)


gene = Genetique(phrase,nombrePersonne,listPersonne)
#New_personne = Personne(len(phrase))
#listPersonne.append(New_personne)
listPersonne = gene.selection(phrase,0.5)
while listPersonne[0].getResistance() != len(phrase)+1:
   #print("resistance",listPersonne[0].getResistance()) 
   #gene.toString(listPersonne,countGeneration)
    #le set de la resistance ce fait ici
   
   listeNewGen = gene.crossover(listPersonne)
   
   while len(listeNewGen) < 500:
       listeNewGen += gene.crossover(listPersonne)

   for i in range(0,len(listeNewGen)):
       listeNewGen[i].mutation(phrase)
   
   gene.updateList(listeNewGen)
   
   gene.toString(listPersonne,listPersonne[0].getResistance())
   countGeneration += 1
   listPersonne = gene.selection(phrase,0.5)
   
   if listPersonne[0].getResistance() == len(phrase):
       gene.toString(listPersonne,listPersonne[0].getResistance())
       print("dora c moi : ",listPersonne[0].getResistance())
       break
   
   
   
   
   
   
   



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
     

    