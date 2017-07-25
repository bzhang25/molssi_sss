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
    """
    Function that return the modulus of two numbers (a%b) 
    Takes arguments mod(a,b)
    """
    i = 1
    if float(a/b) - int(a/b) != 0.0:
        while True: 
            if b*i < a:
                i +=1
            else: 
                return a - b * (i-1)
                break
    elif b > a:
        return a

    else:
        return 0
            

    
