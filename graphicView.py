def printLine(a, b, c):
    print "", a, "|", b, "|", c, ""

def printSep(n):
    if n != 2:
        print "--- --- ---"

def graphicView(tab):
    for iLine in range(3):
        printLine(tab[iLine*3], tab[iLine*3 + 1], tab[iLine*3 + 2])
        printSep(iLine)


# t = [" ", " ", "x", "o", "x", "o"," ", " ", "x"]

# graphicView(t)

