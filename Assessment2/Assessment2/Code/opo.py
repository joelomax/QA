def f(input):
    if input == 3 or input == 1:
        return True
    else:
        for i in range(2, input-1):
            if input % i == 0:
                return False
            else:
                return True
print(f(72))