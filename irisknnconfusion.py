import csv
import random as rn
import math
import operator 
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def dataload(filename):													#load data and convert into a list
	with open(filename,'rb') as csvfile:
		dataset=csv.reader(csvfile)
		data=list(dataset)
		del(data[-1])
		rn.shuffle(data)
		#print data
		for x in range(len(data)):
			for y in range(4):
				data[x][y]=float(data[x][y])
	
		return data

		

	
	
def distanceeuclid(data1,data2,length):									#calculate the euclidean distance 
	distance=0
	for i in range(length):
		distance+=pow((data1[i]-data2[i]),2)
	return math.sqrt(distance)

def getNeighbours(trainingSet, testInstance, k):						#take top k nearset neigbours and stores in a list	
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = distanceeuclid(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):												# returns the nearest of the neigbours out of k neighbours

	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def accuracy(testvalue,testdata):										#calculate the accuracy 
	counter=0
	for x in range(len(testvalue)):
		if(testvalue[x]==testdata[x][4]):
			counter=counter+1
	acc=float(counter)/float(len(testdata))
	return acc*100.0


def confusionmatrix(testvalue,testdata):
	actualvalue=[]
	for x in testdata:
		actualvalue.append(x[-1])
	CM=confusion_matrix(actualvalue,testvalue)
	print CM
	sumoftrues=0
	f=0
	for x in CM:
		sumoftrues=sumoftrues+x[f]
		f=f+1
	acura=float(sumoftrues)/float(len(testvalue))
	return acura





traind=[] #training data for cross validation
traind1=[]
traind2=[]
testd=[] #test data for cross validation
accarray=[]
Data1=dataload('iris.data.csv')
datataken=Data1  #take whole data as sample rest for final test
kvalue=[]
ip=0
k=5
maxaccuracy=0.0
maxk=k
chunklen=150/5
while(ip<10):
	kvalue.append(k)
	sum=0.0
	for x in range(1,6):
		j=x*chunklen
		i=(x-1)*chunklen
		testd=datataken[i:j]
		traind1=datataken[0:i]
		traind2=datataken[j:]
		traind=traind1+traind2
		testvalue=[]  #this stores classified class
		for t1 in testd:
			neighbour=getNeighbours(traind,t1,k)
			testvalue.append(getResponse(neighbour))
		sum=sum+accuracy(testvalue,testd)
	meanaccu=sum/float(5)
	print 'for k= '+repr(k)+' meanaccuracy = '+repr(meanaccu)
	accarray.append(meanaccu)
	if(maxaccuracy<meanaccu):
		maxk=k
		maxaccuracy=meanaccu


	if(ip%2==0):
		k=k+2
	else:
		k=k+4
	ip=ip+1

print 'k for maximum accuracy by cross validation '+repr(maxk)

plt.plot(kvalue,accarray,'ro')
#plt.show()                      #plots graph between accuracy and k for cross validation

sum=0.0
for x in range(5):
		trainingdata=list()
		testdata=list()
		split=0.70
		Data=dataload('iris.data.csv')
		l=len(Data)
		l1=int(split*l)
		trainingdata=Data[0:l1]
		testdata=Data[l1:]
		testvalue=[]
		for t1 in testdata:
			neighbour=getNeighbours(trainingdata,t1,maxk)
			testvalue.append(getResponse(neighbour))
		sum=sum+accuracy(testvalue,testdata)  
meanaccuu=sum/float(5)

print 'accuracy for test data '+repr(meanaccuu)          #accuracy on final test data

sum1=0.0
for x in range(5):
		trainingdata=list()
		testdata=list()									#confusion matrix
		split=0.70
		Data=dataload('iris.data.csv')
		l=len(Data)
		l1=int(split*l)
		trainingdata=Data[0:l1]
		testdata=Data[l1:]
		testvalue=[]
		for t1 in testdata:
			neighbour=getNeighbours(trainingdata,t1,maxk)
			testvalue.append(getResponse(neighbour))
		sum1=sum1+confusionmatrix(testvalue,testdata)  
meanconfusionaccuracy=sum1/float(5)

print 'mean confusion accuracy for test data '+repr(meanconfusionaccuracy) 
print 'misclassification rate for test data'+repr(100.0-meanconfusionaccuracy)


















#accuracy for test data for various k
'''
ic=0
kvalue=[]
k=5
accarray=[]
while(ic<20):
	kvalue.append(k)
	sum=0.0
	for x in range(5):
		trainingdata=list()
		testdata=list()
		split=0.70
		Data=dataload('iris.data.csv')
		l=len(Data)
		l1=int(split*l)
		trainingdata=Data[0:l1]
		testdata=Data[l1:]
		testvalue=[]  #this stores classified class
		for t1 in testdata:
			neighbour=getNeighbours(trainingdata,t1,k)
			testvalue.append(getResponse(neighbour))
		sum=sum+accuracy(testvalue,testdata)
	meanaccu=sum/float(5)
	print 'for k= '+repr(k)+' meanaccuracy = '+repr(meanaccu)
	

	#print 'accuracy is:'+repr(accuracy(testvalue,testdata))
	accarray.append(meanaccu)
	if(ic%2==0):
		k=k+2
	else:
		k=k+4
	ic=ic+1

plt.plot(kvalue,accarray,'ro')
plt.show()


trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
testInstance = [5, 5, 5]
k = 1
neighbors = getNeighbors(trainSet, testInstance, 1)
print(neighbors)	

neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)

'''