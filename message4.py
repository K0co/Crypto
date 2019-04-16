# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:07:01 2019

@author: chloe
"""

from math import ceil
import collections

#encoding='utf-8' permet la lecture du message 
# /!\ changer l'emplacement du message
with open ("message4.txt","r",encoding='utf-8') as file:
    message = file.read()
    
    #print(message)


    def decode(messageLu):
        
        chiffre = 0
        pair = ""
        impair = ""
        for char in messageLu :
        
            
            if chiffre % 2 == 0 :
                
                pair = pair + char
                
            else :
                
                impair = impair + char
                
            chiffre += 1
            
        ##vérification  
        ##print(pair)
        ##print(impair)
        
        #utilise le premier charactère dans le counter, soit le charactère ayant la plus grande fréquence, pour chaque nb pair/impair
        freqCommon1 = collections.Counter(pair).most_common(1)
        ##print(freqCommon1)
        freqCommon2 = collections.Counter(impair).most_common(1)
        ##print(freqCommon2)
        
        #on suppose ici que ' ' est le charactère le plus utilisé dans un texte. On fait donc la différence de ord pour trouver chaque cle
        key1 = ord(freqCommon1[0][0]) - ord(' ')
        ##print(key1)
        key2 = ord(freqCommon2[0][0]) - ord(' ')
        ##print(key2)
        
        #chaine de charactère vide
        decrypte1 =""
        
        for charac1 in pair :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal1 = ord(charac1) - key1
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte1 = decrypte1 + chr(decal1)

            
        #chaine de charactère vide
        decrypte2 =""
        
        for charac2 in impair :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal2 = ord(charac2) - key2
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte2 = decrypte2 + chr(decal2)
            
        decrypteEntier= ""
    
        taille = max (len(impair), len(pair))
            
        
        for i in range(taille):
            
            if i < len(pair):
                
                decrypteEntier = decrypteEntier + decrypte1[i]

                
            if i < len(impair):
                
                decrypteEntier = decrypteEntier + decrypte2[i]
        
        return decrypteEntier
        
        
cesar = decode(message)
print(cesar)
        
