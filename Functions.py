import itertools
import copy

def nextState(a, allDead):
    xmax = len(a)
    ymax = len(a[0])
    b = [[cell for cell in row] for row in allDead]
    for x in range(xmax):
        for y in range(ymax):
            n = 0
            for i in range(max(x - 1, 0), min(x + 2, xmax)):
                for j in range(max(y - 1, 0), min(y + 2, ymax)):
                    n += a[i][j]
            if(x == 0):
	            for j in range(max(y - 1, 0), min(y + 2, ymax)):
	            	n += a[xmax-1][j]
            elif(x == xmax-1):
	            for j in range(max(y - 1, 0), min(y + 2, ymax)):
	            	n += a[0][j]
            if(y == 0):
                for i in range(max(x - 1, 0), min(x + 2, xmax)):
                    n += a[i][ymax-1]
            elif(y == ymax-1):
                for i in range(max(x - 1, 0), min(x + 2, xmax)):
                    n += a[i][0]
            n -= a[x][y]
            if a[x][y]:
                if n < 2 or n > 3:
                    b[x][y] = 0 # living cells with <2 or >3 neighbors die
                else:
                	b[x][y] = 1
            elif n == 3:
                b[x][y] = 1 # dead cells with 3 neighbors ar born
    return(b)

def show(a):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in a]) + '\n')

def generateStates(length):
	lst = list(map(list, itertools.product([0, 1], repeat=length)))
	finalElements= []
	for e1 in lst:
	    #print(len(finalElements))
	    for e2 in lst:
	        for e3 in lst:
	            for e4 in lst:
	                found = False
	                i=0
	                newState = [e1,e2,e3,e4] #chaque e est une ligne de la grille
	                #print("A : ")
	                #print('\n'.join([' '.join([str(cell) for cell in row]) for row in newState]) + '\n')
	                while not found and i<length: #on s'arrete si on a fait length decalages
	                    item = newState.pop()
	                    newState.insert(0, item) #la derniere ligne devient la premiere
	                    #print("B : ", newState)
	                    if newState in finalElements: #arret si cette nouvelle grille a deja ete ajoutee precedemment
	                        found = True
	                    i+=1
	                i=0
	                while not found and i<length: 
	                    for line in newState: #le dernier element de chaque ligne devient le premier
	                        item = line.pop() 
	                        line.insert(0, item)
	                    #print("B : ", newState)
	                    if newState in finalElements: #arret si cette nouvelle grille a deja ete ajoutee precedemment
	                        found = True
	                    i+=1
	                if not found: # si l'element n'a pas ete trouve precedemment, on l'ajoute aux etats possibles
	                    #print("B : ")
	                    #print('\n'.join([' '.join([str(cell) for cell in row]) for row in newState]) + '\n')
	                    finalElements.append(newState)
	print("Final : ",len(finalElements))
	return finalElements


#generateStates(5)