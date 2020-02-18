#import pdb

"""
original code

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n = 0:
                return False
            return True
is_prime(2)
"""

def is_prime(x):
    if x < 2:
        return True
    for n in range(2, x-1):
        if x % n == 0:
            return False
        else:
            return True 
       
is_prime(1)

#pdb.set_trace()