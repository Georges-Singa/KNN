import random
import csv
from os import  chdir

with open('iris.txt', 'r') as csvfile:
    lines = csv.reader(csvfile)

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

    for x in range(len(dataset)-1):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])

    if random.random() < split:
        pass

    else:
        pass


trainingSet=[]

testSet=[]

loadDataset('iris.txt', 0.66, trainingSet, testSet)

print ('Train: ' + repr(len(trainingSet)))

print ('Test: ' + repr(len(testSet)) )





