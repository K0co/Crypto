# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:01:29 2019

@author: chloe
"""

from math import ceil
import collections

#encoding='utf-8' permet la lecture du message 
# /!\ changer l'emplacement du message
with open ("message2.txt","r",encoding='utf-8') as file:
    message = file.read()
    
    print(message)

    #permet de trouver la lettre ayant la plus grande fréquence 'à la main'    
#    decrypteDico = {}
#
#    for char in message:
#        
#        if char in decrypteDico :
#            
#            decrypteDico[char] += 1
#
#        else : 
#            
#            decrypteDico[char] = 1
#
#    print(decrypteDico)
    #affiche le counter du message (dico avec fréquence)   
#    print(collections.Counter(message))
    #affiche le premier charactère dans le counter
#    print(collections.Counter(message).most_common(1))


    def decode(messageLu):
        #utilise le premier charactère dans le counter soit le charactère ayant la plus grande fréquence
        freqCommon = collections.Counter(messageLu).most_common(1)
        #on suppose ici que ' ' est le charactère le plus utilisé dans un texte. On fait donc la différence de ord pour trouver la cle
        key = ord(freqCommon[0][0]) - ord(' ')
        #print(key)
        
        #chaine de charactère vide
        decrypte=""
        
        for char in messageLu :
            #on soustrait l'emplacement du charactère par la cle pour décoder
            decal = ord(char) - key
            #on ajoute le bon charactère dans le chaine de charactère
            decrypte = decrypte + chr(decal)
            
        return decrypte
        
    
    cesar = decode(message)
    print(cesar)
            




        
        



        


        
        
            
        
        
        
        