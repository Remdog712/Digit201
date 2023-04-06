import os
import spacy
import re

nlp = spacy.load('en_core_web_lg')
workingDir = os.getcwd()
CollPath = "C:/github/Digit201/PYTHONTEST/SimspsonsFinalFiles"
outputFile = "output_PythonTest.txt"

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        print(filepath)
        readFile = f.read()
        stringFile = str(readFile)
        elementsRemoved = re.sub('<.+?>', '', stringFile)
        tokens = nlp(elementsRemoved)
        listAdjs = AdjCollector(tokens)
        writeToFile(listAdjs)

def AdjCollector(tokens):
    Adjs = set()
    for token in tokens:
        if token.pos_ == "ADJ" and token.text.islower():
            Adjs.add(token.text)
    return Adjs

def writeToFile(Adjs):
    with open(outputFile, 'a', encoding='utf8') as f:
        for Adjs in Adjs:
            f.write(Adjs + "\n")


for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        readTextFiles(filepath)



