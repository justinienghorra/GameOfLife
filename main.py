import itertools

###############################################################################
def iterate(a):
    xmax = len(a)
    ymax = len(a[0])
    b = [[cell for cell in row] for row in empty]
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
                for i in range(max(x - 1, 0), min(x + 2, ymax)):
                    n += a[i][ymax-1]
            elif(y == ymax-1):
                for i in range(max(x - 1, 0), min(x + 2, ymax)):
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

###############################################################################
width = 4
empty = [[0 for y in range(width)] for x in range(4)]

def algoPremiereVersion():
    lst = list(map(list, itertools.product([0, 1], repeat=width)))
    finalElements = []
    finalElements.append(empty)
    turn = 0
    nbElem = 0
    # Avec une grille de X*8
    stop = False
    while(not stop):
        stop = True
        turn=turn+1
        print(turn)
        for e1 in lst:
            print(len(finalElements), nbElem)
            for e2 in lst:
                for e3 in lst:
                    for e4 in lst:
                        nbElem += 1 
                        state = [e1,e2,e3,e4]
                        #[e1,e2,e3,e4] est un etat du jeu de la vie
                        if(state not in finalElements):
                            ite = iterate(state)
                            if(ite in finalElements):
                                finalElements.append(state)
                                stop = False
    print(len(finalElements), turn)

if __name__ == '__main__':
	main()