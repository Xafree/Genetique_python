# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:25:40 2021

@author: emman
"""
import random
import string

class personne:
    
    _genetique=""
    
    def __init__(self, genetique):
        for i in range(0,15):
            self._genetique += random.choice(string.ascii_letters)
    
    