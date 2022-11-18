# 1.  Type example into script and test it
def do_twice(f):
    f()
    f()

def print_spam():
    print ('spam')

do_twice (print_spam)

# 2.  Modify do_twice so it takes 2 arguments (function object and value), calls the function twice, passing the value
# as an argument
def do_twicemod(x, val):
    x(val)
    x(val)

(do_twicemod (print, 'solidsnake'))

#3.  Write a more general version of print_spam called print_twice that takes a string as a parameter and prints it 2x.
def print_twice(word):
    print (word)
    print (word)

(print_twice('matt'))

# 4. Use the modified version of do_twice to call print_twice twice, passing 'wolf' as an argument
do_twicemod(print_twice, ('wolf'))

#5. Define a new function called do_four that takes a function object and a value, calls the function four times,
# passing the value as a parameter.  Use only 2 lines.

def do_four(y, val):
    do_twicemod(y, val)
    do_twicemod(y, val)

do_four(print, ('mantis'))



