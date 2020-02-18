'''

def pos_neg(a, b, negative): 
    if a < 0 or b < 0:
        if a < 0 and b < 0:
            if negative == True:
                return True
        else:
            return True
    else:
        return False

print(pos_neg(1, 1, False))

'''

x = -1 * 1
print(x)