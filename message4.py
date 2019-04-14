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
        
        for char in pair :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal = ord(char) - key1
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte1 = decrypte1 + chr(decal)
            
        #chaine de charactère vide
        decrypte2 =""
        
        for char in impair :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal = ord(char) - key2
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte2 = decrypte2 + chr(decal)
            
        return decrypte1, decrypte2

cesar = decode(message)
print(cesar)
        
                
                
                
        
        
#        #utilise le premier charactère dans le counter soit le charactère ayant la plus grande fréquence
#        freqCommon = collections.Counter(messageLu).most_common(1)
#        #on suppose ici que ' ' est le charactère le plus utilisé dans un texte. On fait donc la différence de ord pour trouver la cle
#        key = ord(freqCommon[0][0]) - ord(' ')
#        #print(key)
#        
#        #chaine de charactère vide
#        decrypte=""
#        
#        for char in messageLu :
#            #on soustrait l'emplacement du charactère par la cle pour décoder
#            decal = ord(char) - key
#            #on ajoute le bon charactère dans le chaine de charactère
#            decrypte = decrypte + chr(decal)
#            
#        return decrypte
#        
#    
#    cesar = decode(message)
#    print(cesar)