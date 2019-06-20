import sys
import math

class Leaf():
    def showStr(self,attributeNames):
        print(self.labelCounts.items())
        pairs = map(lambda (k,v): (k.strip("\n"),v) ,self.labelCounts.items())
        [(k0,v0),(k1,v1)] = pairs
        return "[%s %d/%s %d]\n" % (k0,v0,k1,v1)        

    def __init__(self, guessVal, labelCounts, depth):
        self.guess = guessVal
        self.labelCounts = labelCounts
        self.depth = depth

class Node():
    def showStr(self,attributeNames):
        print(self.labelCounts.items())
        pairs = map(lambda (k,v): (k.strip("\n"),v) ,self.labelCounts.items())
        [(k0,v0),(k1,v1)] = pairs
        attributeName = attributeNames[self.attribute]
        return ("[%s %d/%s %d]\n" +
            ("| " * self.depth) + "%s = %s: %s" +
            ("| " * self.depth) + "%s = %s: %s") % (k0,v0,k1,v1,
            attributeName,self.values["left"],self.left.showStr(attributeNames),
            attributeName,self.values["right"],self.right.showStr(attributeNames))

    def __init__(self, attributes, attribute, attribVals, depth, labelCounts, left, right):
        self.attribute = attribute
        self.values = attribVals
        self.attributes = attributes
        self.depth = depth
        self.labelCounts = labelCounts
        self.left = left
        self.right = right

def showTree(tree, attributeNames):
    print tree.showStr(attributeNames)