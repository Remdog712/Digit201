# Python and Documentation Test - Remington Orange
**My Goal - Find adjectives in the Simpsons Files so that I could set them up for find and replace**

**My Problem - Some Adjectives were connected to names due to spacing issues within the orginal text files**

**My Solution - Remove the Adjectives with names attached as they as came in the same format**

## My Python Code
```
import os
import spacy
import re
```

Import the necessary "equipment" to find our files and use spacy to find our adjectives

```
nlp = spacy.load('en_core_web_lg')
```
Load the large English language model from spacy

```
workingDir = os.getcwd()
```
Get the current working directory.

```
CollPath = "C:/github/Digit201/PYTHONTEST/SimspsonsFinalFiles"
```
Put the path to the xml files

```
outputFile = "output_PythonTest.txt"
```
Personal choice here but made an output file to see a nice long list of my adjectives

```
def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        print(filepath)
        readFile = f.read()
        stringFile = str(readFile)
        elementsRemoved = re.sub('<.+?>', '', stringFile)
        tokens = nlp(elementsRemoved)
        listAdjs = AdjCollector(tokens)
        writeToFile(listAdjs)
```
This is was created with CHATGPT for some musical note issues with writing to text files

```
def AdjCollector(tokens):
    Adjs = set() 
    for token in tokens:
        if token.pos_ == "ADJ" and token.text.islower():
            Adjs.add(token.text)
    return Adjs
```
This function collects all the adjectives from the tokens and returns them in a set format. It checks if the adjective is in lowercase to avoid collecting proper nouns or acronyms since there was an issue with things such as PRINCESSget and other strange occurences in the original output

```
def writeToFile(Adjs):
    with open(outputFile, 'a', encoding='utf8') as f:
        for Adjs in Adjs:
            f.write(Adjs + "\n")
```
This function takes the set of adjectives taken and puts them in the output file.

```
for file in os.listdir(CollPath):
    if file.endswith(".xml"):
        filepath = f"{CollPath}/{file}"
        readTextFiles(filepath)
```
This loop goes over all files in the directory and checks if the file is an XML file, and tells the readTextFiles() function to take the adjectives from the file. The taken adjectives are put in the output file.


*I did not however include the find and replace as I did this only to see the outputs. I did create real ones on the acutal Simpsons Project for PERSONS and LOCATIONS. That code is the Python folder*


[![](https://mermaid.ink/img/pako:eNp9kcGOgjAQhl9l0svuJvoCHHajQRDRxax7Kx4aOgortKQMa4jx3bcUTHQPcmiY__vamaYXlmmJzGOHUp-zXBiCbz9VYL8Z33aUawU7svEeptP3-WtU1drQ22DM-8znTS2ybn8XLbhu7uuAGxxrv68h5GstJFCOUApzRKjsEOWoLJyy5CGSM7KzHEngSMQ34oSQtFS3BEFR3s4On-Plcxw5vOJBoYbJZvIHMyp-8XaXlTNia1ADgTaVoI8HtOa-xka99OfSPyN2xoZvbddCgXb9R7Z27JPHiDXYnRaCPjw6G-ck_AtrFLcwGWZOlSv7hU1YhbZvIe2bXvokZfYyFabMs79SmFPKUnW1nmhJ7zqVMY9MixPW1lIQ-oU4GlEN4fUP8SKjRg?type=png)](https://mermaid.live/edit#pako:eNp9kcGOgjAQhl9l0svuJvoCHHajQRDRxax7Kx4aOgortKQMa4jx3bcUTHQPcmiY__vamaYXlmmJzGOHUp-zXBiCbz9VYL8Z33aUawU7svEeptP3-WtU1drQ22DM-8znTS2ybn8XLbhu7uuAGxxrv68h5GstJFCOUApzRKjsEOWoLJyy5CGSM7KzHEngSMQ34oSQtFS3BEFR3s4On-Plcxw5vOJBoYbJZvIHMyp-8XaXlTNia1ADgTaVoI8HtOa-xka99OfSPyN2xoZvbddCgXb9R7Z27JPHiDXYnRaCPjw6G-ck_AtrFLcwGWZOlSv7hU1YhbZvIe2bXvokZfYyFabMs79SmFPKUnW1nmhJ7zqVMY9MixPW1lIQ-oU4GlEN4fUP8SKjRg)

**MMMM...Code**