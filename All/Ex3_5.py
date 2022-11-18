def do_twice(f):
    f()
    f()

def do_four(f):
    f()
    f()
    f()
    f()
def column():
    print ('+', ('- ' * 4), end = '')

def line():
    do_twice(column), print ('+')

def barLine():
    print ('|', (' '*7), '|', (' '*7), '|')

def fourSquare():
    line()
    do_four(barLine)
    line()
    do_four(barLine)
    line()

(fourSquare())