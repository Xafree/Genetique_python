# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:38:28 2021

@author: emman
"""
from Personne import Personne
from random import randint

class Genetique:
    
    listPersonnes = []
    _numberPop = 0
    _phrase = ""
    
    def __init__(self,phrase, numberPop):
        self._phrase = phrase
        self._numberPop = numberPop
        for i in range(0,numberPop):
            New_personne = Personne(len(phrase))
            self.listPersonnes.append(New_personne)
 
    def selection(self,phrase):
        self.listPersonnes.sort(key=lambda x: x.fitness(phrase), reverse=True)
        return self.listPersonnes[:100]
        
       
    def getList(self,phrase):
       for y in range(0,len(self.listPersonnes)):
           print("Génération 1 personne [",y,"] :",self.listPersonnes[y].getGenetique()," nombre de charactère good :",self.listPersonnes[y].getResistance())

    def crossover(self):
        newGenerator = []
        for i in range(0,len(self.listPersonnes)-1,2):
            personneX = self.listPersonnes[1].getGenetique() #Parent 1
            personneY = self.listPersonnes[2].getGenetique() #Parent 2
            
            random = randint(0, len(self._phrase)) #Nombre aléatoire
            personneOut = Personne(len(self._phrase)) #l'objet enfant
            
            personneOut.setGenetique(personneX[:random]+personneY[random-len(self._phrase):])#Ajout de ADN
            newGenerator.append(personneOut)
        return newGenerator #Génération 2
        
    def mutation(self):
        print("A faire")