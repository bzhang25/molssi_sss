"""
A small set of functions for doing math operations 
"""

#Write a function named add that adds two values 
def add(a,b):
    """
    IF YOU PUT TEXT HERE THIS WILL SHOW UP WHEN YOU RUN HELP
    """
    return a + b

def mult(a,b):
    """
    Function that multiplies two arguments
    """
    return a * b

def divide(a,b):
    """
    Function that divides two arguments
    """
    return a/b

def subtract(a,b):
    """
    Function that subtracts the second element from the first
    """
    return a - b

def mod(a,b):
    if float(a/b) - int(a/b) != 0.0:
        while True: 
            if b*i < a:
                i++
            else: 
                return a - b * (i-1)
    elif b > a:
        return a

    else:
        return 0
            

    
