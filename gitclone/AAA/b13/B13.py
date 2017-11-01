import csv
import random
from math import sqrt
from operator import itemgetter
from collections import Counter

f = open("iris.data",'r')
ar = f.read().split('\n')

database = []
for x in ar:
    database.append(x.split(','))
database = database[:-1]

random.shuffle(database)

database = database[:20]


X=[]
Y =[]

for d in database:
    X.append(d[:-1])
    Y.append(d[-1])

X_train = X[:15]
Y_train = Y[:15]

X_test = X[15:]
Y_test = Y[15:]


sample = 0

X_sample = X_test[sample];

dist = []



for i in range(len(X_train)):
    d=0
    for j in range(len(X_train[i])):
        d += pow(float(X_sample[j]) - float(X_train[i][j]),2)
    dist.append((sqrt(d),i))

#print dist

sorted_distances = sorted(dist,key=itemgetter(0))

print sorted_distances[:5]

print "Test Sample was of class "+ Y_test[sample]

d = {'Iris-versicolor':0, 'Iris-virginica':0, 'Iris-setosa':0}

top_dist = []
top_dist = sorted_distances[:5]

for dis,i in top_dist:
    d[Y_train[i]]+=1

print d

keys = d.keys()
values = d.values()

z = zip(keys,values)

print z
classes = sorted(z,key=itemgetter(1))
print classes

print ("\n")

print "FINAL CLASS ",classes[-1]
