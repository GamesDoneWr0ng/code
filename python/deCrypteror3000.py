import numpy as np
import re

encrypted = input("encrypted: ")

settings = {"ignoreSpecial": True,
            "ignoreCapitilization": True}

wordlists = {"dictonaryEn": False,
             "ordliste_banneord": False,
             "ordliste_folkeeventyr": False,
             "ordliste_gamle_norske_fornavn": False,
             "ordliste_passord_topp_125": False,
             "ordliste_snl_datoer": False,
             "ordliste_snl_egennavn": False,
             "ordliste_snl_fellesord": True,
             "ordliste_ssb_norske_etternavn": False,
             "ordliste_ssb_norske_fornavn": False
             }

if settings["ignoreSpecial"]:
    encrypted = re.sub(r'[^a-zA-Z ]', '', encrypted)
if settings["ignoreCapitilization"]:
    encrypted = encrypted.lower()

alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
alfabet = alfabet + (alfabet.upper() if not settings["ignoreCapitilization"] else "")
alfabet = {i: alfabet.index(i) for i in alfabet}

wordlist = []
for name, enabled in wordlists.items():
    if enabled:
        with open(f"/Users/askborgen/Desktop/code/resources/ordliste-master/{name}.txt") as f:
            wordlist += re.sub(r'[^a-z\\]', '', f.read().lower()).split("\n")

def getShape(word):
    word = re.sub(r'[^a-zA-Z ]', '', word)
    if len(word) == 0:
        return []
    shape = []
    lastIndex = alfabet[word[0]]
    for letter in word[1:]:
        shape.append(alfabet[letter] - lastIndex)
        lastIndex = alfabet[letter]
    return shape

def makeShapes(wordlist):
    """Converts a list of word to their shapes. Eksample Hei -> [7, -3, 4]"""
    shapes = {}
    for word in wordlist:
        shape = getShape(word)
        if len(word) == 0:
            return []
        
        key = str(shape[1:])
        if key in shapes:
            shapes[key].append((word, alfabet[word[0]]))
        else:
            shapes[key] = [(word, alfabet[word[0]])]

    return shapes

shapes = makeShapes(wordlist)

def findSameShapes(encrypted, shapes):
    print("Same Shape:")
    for i in encrypted.split(" "):
        if str(getShape(i)[1:]) in shapes:
            print(shapes[getShape(i)[1:]])

    print("\nNegative Shape:")
    for i in encrypted.split(" "):
        if str([-i for i in getShape(i)[1:]]) in shapes:
            print(shapes[[-i for i in getShape(i)[1:]]])

findSameShapes(encrypted, shapes)