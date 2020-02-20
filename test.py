import pytest

def alphabet_position(text):
    l = text.split(" ")
    l2 = []
    for i in l:
        l2.append(sorted(l.item))
    return l2

print(alphabet_position("fdnvmnsmns jdsjjl  kj kjs klj lk l kj lkjwssaoiuoiu"))