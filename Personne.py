# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:25:40 2021

@author: emman
"""
import random
import string

class Personne:
    
    _genetique=""
    _resistance=0
    _nom=""
    
    def __init__(self,defGen):
        self._genetique += self._generateGenetique(defGen)

    def _generateGenetique(self,defGen):
        out =""
        for i in range(0,defGen):
            out += random.choice(string.printable)
        return out
    
    def getNom(self):
        return self._nom
    
    def getGenetique(self):
        return self._genetique  
    
    def setGenetique(self,genetique):
        self._genetique = genetique
    
    def getResistance(self):
        return self._resistance
    
    def setResistance(self,number):
        self._resistance=number
    
    def fitness(self,phrase):
        gen = self.getGenetique()
        count = 0
        for i in range(0,len(phrase)):
           if phrase[i:i+1] == gen[i:i+1]:
                count+=1
        self.setResistance(count)        
        return count

    def mutation(self,phrase):
        
        indexString = random.randint(0, len(self._phrase))
        lettreMute = phrase[random.randint(0, len(self._phrase))]
        self._genetique[indexString] = lettreMute

            
    def toString(self):
        return "personne [ genetique = "+self.getGenetique()+"]"