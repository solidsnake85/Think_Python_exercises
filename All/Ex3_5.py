# 1. Write four squares made up of + and - like in the 3.5 drawing
def do_twice(f):
    f()
    f()

def do_four(f):
    f()
    f()
    f()
    f()

def line():
    horizontal = ('- - - - +')
    print ('+', horizontal, horizontal)
def barLine():
    print ('|', (' '*7), '|', (' '*7), '|')

def fourSquare():
    line()
    do_four(barLine)
    line()
    do_four(barLine)
    line()

(fourSquare())