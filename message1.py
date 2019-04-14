# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:35:34 2019

@author: chloe
"""

#http://naelshiab.com/python-et-la-cryptographie-et-un-peu-de-piratage-aussi/


from math import ceil


with open ("message1.txt","r") as file:
    message = file.read()
    
    print(message)
    
    key = 3
    num_col = int(ceil(len(message) / float(key))) #ceil --> arrondit à l'entier supérieur
    num_lig = key
    num_vide = (num_col*num_lig) - len(message) #calcul cases vides à fin du tableau
# Notre message décrypté est un ensemble d'éléments correspondant au nombre de colonnes.
    decrypte = [''] * num_col
# On commence à la colonne zéro et à la ligne zéro.
    col = 0
    lig = 0
    
# On lance une boucle pour chaque
# caractère dans le message crypté.
    for i in message:
	# On répartit les caractères du message cypté dans les colonnes correspondantes.
        decrypte[col] += i
        col += 1
	# On impose une conditionne.
	# Si on a rempli toutes les colonnes,
	# on passe à la ligne suivante.
        if (col == num_col) or (col == num_col - 1 and lig >= num_lig - num_vide):
            col = 0
            lig += 1
 

print ("\n*** Message décrypté! ***\n")
print (''.join(decrypte) + "\n")