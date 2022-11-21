def do_twice(f):
    f()
    f()

def do_four(f):
    f()
    f()
    f()
    f()
def twoColumns():
    horizontal = ('- - - - +')
    print ('+', horizontal, horizontal),

def barLine():
    print ('|         |         |')

def fourSquare():
    twoColumns()
    do_four(barLine)
    twoColumns()
    do_four(barLine)
    twoColumns()

#(fourSquare())

# 2. Make four rows and four columns

def eightSquare():
    fourSquare(), fourSquare()

