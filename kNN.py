# -*- coding: utf-8 -*-

from numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1,1],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
    
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet#deta
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    
    classCount={}#对最近的k个点的类别进行计数
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1

    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
    

group,labels=createDataSet()
print classify0([0,0],group,labels,3)