# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:38:28 2021

@author: emman
"""
from Personne import Personne
from random import randint

class Genetique:

    def __init__(self,phrase, numberPop,listPersonnes ):
        self._phrase = phrase
        self._numberPop = numberPop
        self._listPersonnes = listPersonnes
        for i in range(0,self._numberPop):
            New_personne = Personne(len(phrase))
            self._listPersonnes.append(New_personne)
 
    def selection(self,phrase,pourcentage):
        self._listPersonnes.sort(key=lambda x: x.fitness(phrase), reverse=True)
        decoupe = (len(self._listPersonnes))*pourcentage
        return self._listPersonnes[:int(decoupe)]
        
    def getList(self):
        return self._listPersonnes
    
    def updateList(self,listPersonnes):
        self._listPersonnes = listPersonnes

    def crossover(self,listPersonnes):
        newGenerator = []
        for i in range(0,len(listPersonnes)-1,2):
            
            personneX = Personne(len(self._phrase)) #l'objet enfant
            personneY = Personne(len(self._phrase)) #l'objet enfant
            
            personneX.setGenetique(listPersonnes[i].getGenetique())#Parent 1
            personneY.setGenetique(listPersonnes[i+1].getGenetique()) #Parent 2
            
            random = randint(0, len(self._phrase)) #Nombre aléatoire
            personneOut = Personne(len(self._phrase)) #l'objet enfant
            
            personneOut.setGenetique(personneX.getGenetique()[:random]+personneY.getGenetique()[random-len(self._phrase):])#Ajout de ADN
            newGenerator.append(personneOut)

                
        return newGenerator #Génération 2
        
    def toString(self,listPersonnes,generation):
        print("Génération ",generation," :",listPersonnes[1].getGenetique(),"nombre de charactère good :",listPersonnes[1].getResistance())
        