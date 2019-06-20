import sys
import math

def readAndSplit(trainInput):
    inFile = open(trainInput)
    linesSplit = map(lambda row: map(lambda example: example.split("_"), row.rstrip().split(" ")), inFile.readlines())
    inFile.close()
    return linesSplit

def justRead(input):
    inFile = open(input)
    linesSplit = map(lambda line: line.rstrip(), inFile.readlines())
    inFile.close()
    return linesSplit

def writeToFile(stringVal,fname):
    outFile = open(fname,"w")
    outFile.write(stringVal)
    outFile.close()

def getTotalWords(labeledData):
    n = 0
    for line in labeledData:
        n += len(line)
    return n

def getIndDict(lines):
    res = dict()
    for count, value in enumerate(lines):
        res[value] = count
    return res

def greaterTuple(a,b):
    ((k0,v0),(k1,v1)) = (a,b)
    return b if (v1>v0) else a