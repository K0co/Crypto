# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:07:21 2019

@author: chloe
"""

from math import ceil
import collections

#encoding='utf-8' permet la lecture du message 
# /!\ changer l'emplacement du message
with open ("message5.txt","r",encoding='utf-8') as file:
    message = file.read()
    
    #print(message)
    
    
    def cleVigenere(messageLu, longueur):
        '''Trouve la Cle pour n'importe quel message
        '''
    
        cle = [0] * longueur
        chaine = [''] *longueur
        i = 0
        
        for charac in message :
            
            chaine[i%longueur] = chaine[i%longueur] + charac

            i += 1
          
        for i in range(longueur) :
            
            freqCommon = collections.Counter(chaine[i]).most_common(1)

            cle[i] = ord(freqCommon[0][0]) - ord(' ')
            
        return cle
        
        
    def decodeVigenere(messageLu, cle):
        '''Récupère la cle pour déchiffrer le message
        '''
        
        longueur = len(cle)
        decrypte = ""
        i = 0
        
        for charac in messageLu :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal = ord(charac) - cle[i%longueur]
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte = decrypte + chr(decal)
            
            i += 1
            
        return decrypte
        
        
key = cleVigenere(message, 3)
texte = decodeVigenere(message, key)

print(key,'\n', texte)
        
        
        
        
        
            
            
            
            
    
    