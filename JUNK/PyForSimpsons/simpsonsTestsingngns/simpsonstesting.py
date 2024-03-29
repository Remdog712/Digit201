import os
import spacy
import re

nlp = spacy.load('en_core_web_lg')
workingDir = os.getcwd()
CollPath = r"C:\github\Digit201\PyForSimpsons\simpsonsTestsingngns\SimpsonsTesting\Simpsons_S1"
outputFile = "output.txt"

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        print(filepath)
        readFile = f.read()
        stringFile = str(readFile)
        elementsRemoved = re.sub('<.+?>', '', stringFile)
        tokens = nlp(elementsRemoved)
        listEntities = entitycollector(tokens)
        writeToFile(listEntities)

def entitycollector(tokens):
    entities = set()  # use a set to store unique entities
    for entity in tokens.ents:
        if entity.label_ == "LOC":
            entities.add(entity.text)
    return entities

def writeToFile(entities):
    with open(outputFile, 'a') as f:
        for entity in entities:
            f.write(entity + "\n")

# process each XML file in the specified directory
for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        readTextFiles(filepath)





