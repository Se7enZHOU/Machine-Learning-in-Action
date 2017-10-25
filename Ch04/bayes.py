'''
Naive Bayes: naive means we can asuume all the features are independent and equally important.
'''

def loadDataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],\
                ['maybe','not','take','him','to','dog','park','stupid'],\
                ['my','dalmation','is','so','cute','I','love','him'],\
                ['stop','posting','stupid','worthless','garbage'],\
                ['mr','licks','ate','my','steak','how','to','stop','him'],\
                ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1] #1 is abusive
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        # | operator means set union
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print('the word:%s is not in my Vocabulary!'%word)
    return returnVec

listOPosts,listClasses=loadDataSet()
myVocabList=createVocabList(listOPosts)
print(myVocabList)

#testList=['my','cat','dog']
#setOfWords2Vec(myVocabList,testList)
#print(setOfWords2Vec(myVocabList,listOposts[2]))

import numpy as np

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    #zeros() method is not a native python method
    p0Num=np.zeros(numWords)
    p1Num=np.zeros(numWords)
    p0Denom=0.0
    p1Denom=0.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive

trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList,postinDoc))

p0V,p1V,pAb=trainNB0(trainMat,listClasses)
print(pAb)
print(p0V)
print(p1V)















