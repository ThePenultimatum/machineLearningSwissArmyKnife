import sys
import math

def calcEntropy(probMap):
    """
    This function takes a map of probabilities represented as a dictionary with
    probabilities as the values. It then calculates and returns the entropy
    which is defined as the summation of the probabilities multiplied
    by the logs of those probabilities.
    """
    logBase = 2
    return -1 * reduce(lambda a,b: a+b, map(lambda val: (val * math.log(val,logBase)), probMap.values()))

def probabilityMap(data, column = 0):
    """
    Returns a mapping from values in input data to the probability that
    a random selection from the data will result in that value
    """
    dataValsInCol = map(lambda row: row[column], data)
    total = len(dataValsInCol)
    distinct = set(dataValsInCol)
    probabilities = map(lambda val: (val, probabilitySingleValue(dataValsInCol,val)), distinct)
    return dict((x,y) for x, y in probabilities)

def probabilitySingleValue(data, value):
    """
    Returns the probability as a float that a random selection from data will result
    in value
    """
    numValues = len(filter(lambda x: x==value, data))
    total = len(data)
    if numValues==0:
        return 0.0
    elif numValues == total:
        return 1.0
    else:
        return float(numValues)/len(data)

def getSpecCondEntropy(data,col,specificVal):
    (attribInd,labelInd) = (0,1)
    filteredData = filter(lambda row: row[attribInd]==specificVal, data)
    newLabelProbMap = probabilityMap(filteredData,labelInd)
    return calcEntropy(newLabelProbMap)

def getConditionalEntropy(data,valColumn):
    probMapAttribute = probabilityMap(data,valColumn)
    total = 0
    for specVal in probMapAttribute.keys():
        probOfThisVal = probMapAttribute[specVal]
        thisSpecificConditionalEntropy = getSpecCondEntropy(data,valColumn,specVal)
        total += probOfThisVal*thisSpecificConditionalEntropy
    return total

def getMutualInfo(data,dataValCol,labelCol):
    relevantData = map(lambda row: (row[dataValCol],row[labelCol]), data)
    probabilityMapLabels = probabilityMap(relevantData,1)
    conditionalEntropy = getConditionalEntropy(relevantData,0)
    return calcEntropy(probabilityMapLabels) - conditionalEntropy

def getAttribMaxInfo(data):
    maxMutualInfo = 0
    maxMutualInfoInd = 0
    lastNonLabelColumnInd = len(data[0])-1
    for i in xrange(0,lastNonLabelColumnInd):
        mutualInfo = getMutualInfo(data, i, lastNonLabelColumnInd)
        if mutualInfo > maxMutualInfo:
            maxMutualInfo = mutualInfo
            maxMutualInfoInd = i
    return (maxMutualInfoInd,maxMutualInfo)

    def getCounts(data,allDistinctLabels):
    distinct = set(data)
    counts = {}
    for val in distinct:
        numValues = len(filter(lambda x: x==val, data))
        counts[val] = numValues
    for val in allDistinctLabels:
        if val not in counts:
            counts[val] = 0
    return counts

    def getVocabularyMap(linesSplit):
    valsDistinct = set(map(lambda (value, label): value, linesSplit))
    valMap = dict()
    i = 1 ## because bias index is 0
    for v in valsDistinct:
        if (v not in valMap.keys()):
            valMap[v] = i
        i += 1
    #print valMap
    return valMap

def getDistinctLabelMap(linesSplit):
    labelsDistinct = set(map(lambda (value, label): label, linesSplit))
    labMap = dict()
    i = 0
    for l in labelsDistinct:
        if (l not in labMap.keys()):
            labMap[l] = i
        i += 1
    #print labMap
    return labMap

def reverseLabelMap(labelMap):
    newLabelMap = dict()
    for key in labelMap:
        newLabelMap[labelMap[key]] = key
    return newLabelMap