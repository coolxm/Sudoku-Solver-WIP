import time as t, pprint
import random as r
ptp = pprint.PrettyPrinter(width= 41, compact= True)
#in one square no two of the same can exist
#in one line no two of the same can exist
#every square needs to contain 1 - 9

#every line needs to contain 1 - 9
def make():
    for i in range(0, 9):
        for ii in range(0, 9):

            while True:
                n = r.randint(1, 9)
                if CheckNum(i, ii, n):
                    break
            
            sudoku[i][ii] = n

    for i in range(0, 9):
        for ii in range(0, 9):

            num = r.randint(0, 1000)
            if num in range(0, 500):
                sudoku[i][ii] = 0

#def solveIterative():
#    ptp.pprint("Solving")
#    i = 0
#    ii = 0
#    #initiate loop   
#    while ii < 9 and i < 9:
#        #check if need to be filled
#        if sudoku[i][ii] == 0:
#            solved[i][ii] = 0
#            DON = []
#            #check every possible number (random so more room for error)
#            while True:
#                #random number without those already tried
#                try:
#                    x = r.choice([i for i in range(1,10) if i not in DON])
#                #if every number tried iterateDown
#                except:
#                    i , ii = iterateDown(i, ii)
#                    DON = [solved[i][ii]]
#                    break
#                
#                #check if possible solutionµ
#                check = CheckNum(i, ii,x)
#                print(i, ii, "\n", check, "\n", DON, x)
#                
#                if check:
#                    solved[i][ii] = x
#                    i, ii = iterateUp(i, ii)
#                    break                        
#                else:
#                    DON.append(x)
#
#        else:
#            solved[i][ii] = sudoku[i][ii] 
#            i, ii = iterateUp(i, ii)

#def iterateUp(i, ii):
#    if i == 8:
#        return 85, 85
#    if ii == 8:
#        i += 1
#        ii = 0
#        return i , ii
#    else:
#        ii +=1
#        return i , ii
#
#def iterateDown(i, ii):
#    if i < 0:
#        i = 0
#        return i, ii
#    elif ii < 0:
#        ii = 0
#    elif ii == 0:
#        i -= 1
#        ii = 8
#    else:
#        ii -= 1        
#    if not sudoku[i][ii] == 0:
#        i, ii = iterateDown(i, ii)
#    return i, ii

#maintain numbers already tried
#maintain places visited
def solveRecursive():
    if len == 80:
        return

def CheckNum(x, y, n):
    rx = ry = 0
    Squares = 0
    for i in range(0,9,3):
        for ii in range(0,9,3):
            if x in range(ii, ii + 3):
                rx = ii
                break
        if y in range(i, i + 3):
            ry = i
            break

    for i in range(0,3):
        for ii in range(0,3):
            if not solved[rx + i][ry +ii] == n:
                Squares += 1

    linesV = 0
    for i in range(0,9):
        if not solved[x][i] == n:
            linesV += 1

    linesH = 0
    for i in range(0,9):
        if not solved[i][y] == n:
            linesH += 1

    if Squares == 9 & linesV ==  9 & linesH == 9:
        return True
    else:
        return False
                
def onStart():
    global sudoku
    make()
    ptp.pprint(sudoku)
    #solve()
    print("\n")
    ptp.pprint(solved)

    print(t.process_time())

sudoku = [
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0
]

solved = [
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0
]

onStart()