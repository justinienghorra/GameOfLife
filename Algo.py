


#*** Algorithme ***
listResults # liste des résultats menant vers l'état tout mort
listTemp = [] # liste temporaire
listEtats # liste de tous les états possibles
listLoop = []# liste de tous les états bouclant à l'infini
toutMort # etat tout mort, correspond à une grille de case vide
#Ajouter l'etat tout mort à la liste des resultats

stop = False

while len(listEtats) != 0: #tant qu'on a pas verifié tous les états
  etatFutur = GameOfLife(listEtats[0]) # Utilise la fonction Gameoflife pour obtenir l'etat au temps t+1

if(etatFutur == toutMort): # On vérifie que le prochain etat n'est pas l'etat tout mort
  listResults.append(listEtats[0]) # si c'est le cas alors on ajoute l'état à la liste des resultats
  listEtats.remove(listEtats[0]) # Supprime l'element de la liste

elif(etatFutur in listLoop): # On vérifie que l'etat suivant ne va pas nous mener à une boucle infini
    listLoop.append(listEtats[0]) # Si c'est le cas on ajoute l'etat au temps t = 0 comme etant allant finir en boucle infini
    listEtats.remove(listEtats[0]) # Supprime l'element de la liste

else: # Sinon on parcours les etat au temps t = t+1
    listTemp.append(listEtats[0]) # On ajoute l'etat de base dans une liste temporaire

    while(!stop): # Tant qu'on a pas trouve de resultat (boucle ou etat tout mort)
        etatFutur = GameOfLife(listTemp[-1]) # Recuppere le dernier element inseré dans la liste et regarde l'etat au temps t+1

        if (etatFutur == toutMort or etatFutur in listResults): # si on fini par arriver vers l'etat tout mort ou vers un etat y arrivant
            stop = True # On a trouvé un resultat plus besoin de chercher dans les successeurs
            listResults.extend(listTemp) # On ajoute tous les elements de la liste à la liste contenant les resultats
            #Supprime tous les etats de la liste temp des etats encore non parcouru de la liste listEtats
            for item in listTemp: # Supprime tous les elemets qui ont été parcouru de la liste contenant tous les etats possibles
                if(item in listEtats):
                    listEtats.remove(item)
            listTemp=[] # On réinitialise la liste

        elif(etatFutur in listTemp or etatFutur in listLoop): # On va boucler à l'infini
            stop = True # On a trouve un resultat plus besoin de chercher dans les successeurs
            listLoop = listLoop.extend(listTemp) # On ajoute à la liste des etats bouclant à l'infini la liste d'etats que l'on parcourait
            #Supprime tous les etats de la liste temp des etats encore non parcouru de la liste listEtats
            for item in listTemp: # Supprime tous les elemets qui ont été parcouru de la liste contenant tous les etats possibles
                if(item in listEtats):
                    listEtats.remove(item)
            listTemp=[] # On réinitialise la liste

        else:
            listTemp.append(etatFutur)
    stop = False # Reinitialise la variable