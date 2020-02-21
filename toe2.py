"""
TOE: Return the string (backwards) that is between the first and last appearance of “bert” in the given string, or return the empty string “” if there is not 2 occurances of “bert”
Ignore Case
For Example:
getBert(“bertclivebert”) → “evilc”
getBert(“xxbertfridgebertyy”) → “egdirf”
 getBert(“xxBertfridgebERtyy”) → “egdirf”
 getBert(“xxbertyy”) → “”
 getBert(“xxbeRTyy”) → “”
"""

def getBert(string):
    string1 = string.lower()
    substring = "bert"
    z = string1.count(substring)
    if z < 2:
        return ""
    else:
        x = string1.find("bert")
        y = string1.find("bert", x+4)
        return string1[x+4:y]

print(getBert("xxxbErtClivebertxxx"))


#string = "udibbvkhredbsdkdbk"
#string = "udiGB bvkh redb sd kKJdbk"
#string1 = str(string.lower)

#print(string1)
#print(string.count("red"))


