
def maskify(cc):
    firstnos = cc [0:-4]
    lastnos = cc [-4:]
    numofchar = 0
    for item in firstnos:
        numofchar+=1
    numofchar
    while numofchar > 0:
        newnum = 0
        newnum += "#"
        numofchar-1
    return newnum + lastnos

print(maskify("764363763774898"))
'''
def maskify(cc):
    firstnos = cc [0:-4]
    firstnos.replace()
    newnum = firstnos + cc [-4:]
    return newnum

print(maskify("4387487287"))
'''