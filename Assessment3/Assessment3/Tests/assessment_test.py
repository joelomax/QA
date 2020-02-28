import pytest
from Code import python3

# The test for listGen is not the best but it works for this purpose.

def split(input):
    if len(input) != 5:
        return False
    else:
        for i in input:
            if i % 2 != 0 or 100 > i or i > 200:
                return False
        return True

def test_listGen():
    assert split(python3.listGen()) == True
    assert split(python3.listGen()) == True
    assert split(python3.listGen()) == True
    assert split(python3.listGen()) == True
    assert split(python3.listGen()) == True

def test_removeDupe():
    assert python3.removeDupe(["Dog"]) == ["Dog"]
    assert python3.removeDupe(["Dog","Cat"]) == ["Dog","Cat"]
    assert python3.removeDupe(["Dog","Dog","Cat"]) == ["Dog","Cat"]
    assert python3.removeDupe(["Dog","DoG","Cat"]) == ["Dog","DoG","Cat"]
    assert python3.removeDupe(["Cat","DOG","DOG"]) == ["Cat","DOG"]

def test_oddLetters():
    assert python3.oddLetters("Hello") == "el"
    assert python3.oddLetters("hi") == "i"
    assert python3.oddLetters("0H1e2l3l4o5w6o7r8l9d") == "Helloworld"
    assert python3.oddLetters("H1e2l3l4o5w6o7r8l9d") == "123456789"
    assert python3.oddLetters("ILovePython") == "LvPto"

def test_amISearch():
    assert python3.amISearch("Am I in Amsterdam") == 1
    assert python3.amISearch("I am in Amsterdam am I?") == 2
    assert python3.amISearch("I have been in Amsterdam") == 0
    assert python3.amISearch("I love when I am in Amsterdam") == 1
    assert python3.amISearch("Am I am in Amsterdam in the AM") == 3

def test_validCard():
    assert python3.validCard("0123-4567-8901-2345") == False
    assert python3.validCard("401234567890123") == False
    assert python3.validCard("4012 3456 7890 1234") == False
    assert python3.validCard("4444-0123-4567-8901") == False
    assert python3.validCard("4012-3456-7890-1234") == True
    assert python3.validCard("4012345678901234") == True

def test_email():
    assert python3.email("john@google.com", "person") == "john"
    assert python3.email("jane@Microsoft.com", "company") == "microsoft"
    assert python3.email("Dave@amazon.com", "person") == "dave"
    assert python3.email("FRied@mcdonalds.com", "person") == "fried"
    assert python3.email("doug@landscapegardening.com", "company") == "landscapegardening"

def test_superblock():
    assert python3.superBlock("hoopplla") == 2
    assert python3.superBlock("abbCCCddDDDeeEEE") == 3
    assert python3.superBlock("") == 0
    assert python3.superBlock("python") == 1
    assert python3.superBlock("doom") == 2

def test_f():
    assert python3.f(3) == 2
    assert python3.f(8) == 21
    assert python3.f(0) == 0
    assert python3.f(1) == 1
    assert python3.f(2) == 1

def test_headsLegs():
    assert python3.headsLegs(35,94) == (23,12)
    assert python3.headsLegs(2,6) == (1,1)
    assert python3.headsLegs(12,63) == "no solutions"
    assert python3.headsLegs(15,30) == (15,0)
    assert python3.headsLegs(10,40) == (0,10)

def test_endsPy():
    assert python3.endsPy("ilovepy") == True
    assert python3.endsPy("welovepy") == True
    assert python3.endsPy("welovepyforreal") == False
    assert python3.endsPy("pyiscool") == False
    assert python3.endsPy("hurrayforpY") == True