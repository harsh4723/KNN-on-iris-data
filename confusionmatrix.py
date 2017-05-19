

actual=['a','a','b','c','a','c','c','b']
pred=['a','a','a','c','a','b','c','a']
labels=[]

for x in actual:
	if x not in labels:
		labels.append(x)

la=len(labels)

dictlabels={}
i=0
for y in labels:
	dictlabels.update({y:i})
	i=i+1

print dictlabels

cmatrix=[]

for i in range(la):
	matrixsub=[]
	for j in range(la):
		matrixsub.append(0)
	cmatrix.append(matrixsub)


for y in range(len(actual)):
	cmatrix[dictlabels[actual[y]]][dictlabels[pred[y]]]=cmatrix[dictlabels[actual[y]]][dictlabels[pred[y]]]+1

print cmatrix
		
