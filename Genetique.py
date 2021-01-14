# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:38:28 2021

@author: emman
"""
from Personne import Personne

class Genetique:
    
    listPersonnes = []
    
    def __init__(self,phrase, numberPop):
        for i in range(0,numberPop):
            New_personne = Personne(len(phrase))
            self.listPersonnes.append(New_personne)
 
    def selection(self,phrase):
        
        self.listPersonnes.sort(key=lambda x: x.fitness(phrase), reverse=True)
        return self.listPersonnes[:10]
        
       
    def getList(self,phrase):
       for y in range(0,500):
           print(self.listPersonnes[y].fitness(phrase))

    def crossover():
        
        
    def mutation():
        print("A faire")