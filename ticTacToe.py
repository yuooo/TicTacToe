from graphicView import graphicView
import sys

def isSameRow(tab):
    isS = False
    for iLin in range(3):
        nAligned = 0
        for iCol in range(3):
            if tab[iLin*3 + iCol] != " ":
                nAligned += 1
            if nAligned == 3:
                isS = True
                return isS 
    return isS 

t1 = [" ", " ", "x", "o", "x", "o"," ", " ", "x"]
t2 = [" ", " ", "x", " ", "o", "x", "o", " ", "x"]
t3 = [" ", " ", "x", " ", "o", " ", "o", "o", "x"]

# graphicView(t1)
# print
# graphicView(t2)
# print 
# graphicView(t3)
# print 

# print isSameRow(t1)
# print isSameRow(t2)
# print isSameRow(t3)

def isSameCol(tab):
    isS = False
    for iCol in range(3):
        nAligned = 0
        for iLin in range(3):
            if tab[iLin*3 + iCol] != " ":
                nAligned += 1
            if nAligned == 3:
                isS = True
                return isS 
    return isS 

# print isSameCol(t1)
# print isSameCol(t2)
# print isSameCol(t3)

def isSameDiag(tab):
    isS = False
    isS = (tab[0] != " ") and (tab[4] != " ") and (tab[8] != " ")
    isS = isS or ( (tab[2] != " ") and (tab[4] != " ") and (tab[6] != " ") )
    return isS 

t4 = ["o", " ", " ", " ", "o", " ", "o", "o", "x"]

# print isSameDiag(t1)
# print isSameDiag(t2)
# print isSameDiag(t3)
# print isSameDiag(t4)

def isAligned(tab):
    isS = isSameRow(tab) or isSameCol(tab) or isSameDiag(tab)
    return isS 

def printFirstMessage():
    print "******* Welcome to tic tac toe! *******"
    print "It's a highly boring game, but you do whatever you want with your life!"
    print
    print "Enter two numbers then press Return to indicate where you want to play." 
    print "For instance, if I want to play at the top left, enter 1 1. At the middle right, enter 2 3."

def printTurn(nTurn):
    print "Your turn, Player",
    if ((nTurn % 2) == 0):
        print 2
    else:
        print 1


printFirstMessage()

def twoPlayersGame():
    printFirstMessage()
    tabBoth = [" "]*9
    tabX = [" "]*9
    tabO = [" "]*9
    # print tabX
    # print tabO
    nTurn = 0

    while (nTurn < 9):
        nTurn += 1
        printTurn(nTurn)
        iLin, iCol = map(int, sys.stdin.readline().split())
        iLin -= 1
        iCol -= 1
        index = iLin*3 + iCol
        if ((nTurn % 2) == 1):
            letter = "X"
            tabX[index] = "X"
            if isAligned(tabX):
                print "Player 1 WON!!! Player 2, you're such a looser!"
                return
        else:
            letter = "O"
            tabO[index] = "O"
            if isAligned(tabO):
                print "Player 2 WON!!! Player 1, your life sucks!"
                return
        tabBoth[index] = letter
        graphicView(tabBoth)
    print "No one won. No one lost. So boring. Like tic tac toe."



twoPlayersGame()


