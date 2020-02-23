import pytest
from Code import python1

def test_longString():
    assert python1.longString("hi","hello") == "hello"
    assert python1.longString("three", "two") == "three"
    assert python1.longString("three", "hello") == "three hello"
    assert python1.longString("echo", "print") == "print"
    assert python1.longString("fire","rib") == "fire"

def test_getBert():
    assert python1.getBert("bertclivebert") == "clive"
    assert python1.getBert("xxbertfridgebertyy") == "fridge"
    assert python1.getBert("xxBertfridgebERtyy") == "fridge"
    assert python1.getBert("xxbertyy") == ""
    assert python1.getBert("xxbeRTyy") == ""

def test_fizzBuzz():
    assert python1.fizzBuzz(3) == "fizz"
    assert python1.fizzBuzz(10) == "buzz"
    assert python1.fizzBuzz(15) == "fizzbuzz"
    assert python1.fizzBuzz(8) == "null"
    assert python1.fizzBuzz(75) == "fizzbuzz"

def test_largest():
    assert python1.largest("55 72 86") == 14
    assert python1.largest("15 72 80 164") == 11
    assert python1.largest("555 72 86 45 10") == 15
    assert python1.largest("98 63 34 1 13") == 17
    assert python1.largest("98 107 415") == 17

def test_csvScan():
    assert python1.csvScan("Jeff,private.key,False,1445") == ["Jeff"]
    assert python1.csvScan("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445") == ["Jeff"]
    assert python1.csvScan("Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") == ["Bert","Jeff"]
    assert python1.csvScan("Bert,private.key,False,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") == ["Bert","Jeff"]
    assert python1.csvScan("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,True,1445") == []

def test_iBeforeE():
    assert python1.iBeforeE("ceiling") == True
    assert python1.iBeforeE("believe") == True
    assert python1.iBeforeE("glacier") == False
    assert python1.iBeforeE("height") == False
    assert python1.iBeforeE("receive") == True

def test_getVowel():
    assert python1.getVowel("Hello") == 2 
    assert python1.getVowel("hEelLoooO") == 6
    assert python1.getVowel("WhitEboarD") == 4
    assert python1.getVowel("as") == 1
    assert python1.getVowel("pass") == 1

def test_factorial():
    assert python1.factorial(1) == 1
    assert python1.factorial(3) == 6
    assert python1.factorial(4) == 24
    assert python1.factorial(6) == 720
    assert python1.factorial(8) == 40320

def test_returnPosition():
    assert python1.returnPosition("This is a Sentence","s") == 4
    assert python1.returnPosition("This is a Sentence","S") == 8
    assert python1.returnPosition("Fridge for sale","z") == -1
    assert python1.returnPosition("I love Python", "L") == -1
    assert python1.returnPosition("I LOVE PYTHON", "L") == 2

def test_compares():
    assert python1.compares("The",2,"h") == True
    assert python1.compares("AAbb",1,"b") == False
    assert python1.compares("Hi-There",10,"e") == False
    assert python1.compares("HEY",2,"e") == True
    assert python1.compares("on-premise",3,"-") == True
