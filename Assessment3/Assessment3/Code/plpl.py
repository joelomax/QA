def f(arg1):
    arg1 = arg1.lower()
    b = arg1.split(" ")
    count = 0
    for i in b:
        if i == "am":
            count+=1


    
    return count

print(f("am I in amsterdam"))