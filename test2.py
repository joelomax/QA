def missing_char(str, n):
    l = []
    for i in str:
        l.append(i)
    l.pop(n)
    x = "".join(l)

    return x
print(missing_char("hello my name", 0))