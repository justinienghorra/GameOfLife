import itertools
import copy

length=4
lst = list(map(list, itertools.product([0, 1], repeat=length)))
finalElements= []
for e1 in lst:
        print(len(finalElements))
        for e2 in lst:
            for e3 in lst:
                for e4 in lst:
                    found = False
                    i=0
                    newState = [e1,e2,e3,e4] #chaque e est une ligne de la grille
                    print("A : ")
                    print('\n'.join([' '.join([str(cell) for cell in row]) for row in newState]) + '\n')
                    while not found and i<length-1: #on s'arrete si on a fait length decalages
                        item = newState.pop()
                        newState.insert(0, item) #la derniere ligne devient la premiere
                        #print("B : ", newState)
                        if newState in finalElements: #arret si cette nouvelle grille a deja ete ajoutee precedemment
                            found = True
                        i+=1
                    i=0
                    while not found and i<length-1: 
                        for line in newState: #le dernier element de chaque ligne devient le premier
                            item = line.pop() 
                            line.insert(0, item)
                        #print("B : ", newState)
                        if newState in finalElements: #arret si cette nouvelle grille a deja ete ajoutee precedemment
                            found = True
                        i+=1
                    if not found: # si l'element n'a pas ete trouve precedemment, on l'ajoute aux etats possibles
                        print("B : ")
                        print('\n'.join([' '.join([str(cell) for cell in row]) for row in newState]) + '\n')
                        finalElements.append(newState)
print(len(finalElements))