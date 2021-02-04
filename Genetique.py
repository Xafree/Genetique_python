# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:38:28 2021

@author: emman
"""
from Personne import Personne

class Genetique:
    
    listPersonnes = []
    _numberPop = 0
    
    def __init__(self,phrase, numberPop):
        self._numberPop = numberPop
        for i in range(0,numberPop):
            New_personne = Personne(len(phrase))
            self.listPersonnes.append(New_personne)
 
    def selection(self,phrase):
        self.listPersonnes.sort(key=lambda x: x.fitness(phrase), reverse=True)
        return self.listPersonnes[:100]
        
       
    def getList(self,phrase):
       for y in range(0,len(phrase)):
           print("Génération 1 personne [",y,"] :",self.listPersonnes[y].getGenetique()," nombre de charactère good :",self.listPersonnes[y].getResistance() )

    def crossover(self, listPersonne):
        print("todo")
        
    def mutation():
        print("A faire")