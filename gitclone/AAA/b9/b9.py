# B9 TEXT CLASSIFICATION

from math import sqrt
from math import log
from collections import Counter
from operator import itemgetter

def tf(kt,doc):
    return (doc.count(kt))

def idf(kt,all_docs):
    num = 0
    for x in all_docs:
        if kt in x:
            num +=1
    if num>0:
        return round(float(log(float(len(all_docs))/float(num))),3)

def tfidf(kt,doc):
    return (tf(kt,doc)*idf(kt,all_docs))

def cos_sim(infile,doc,ktrms):
    a=0
    for x in ktrms:
        a = a + (tfidf(x,doc)*tfidf(x,infile))
    b = doclen(infile,ktrms)*doclen(doc,ktrms)

    if not b:
        return 0
    else:
        return (round((a/b),3))

def doclen(doc, kterms):
    val = 0
    for x in kterms:
        val = val + pow(tfidf(x,doc),2)
    return sqrt(val)

files = []
all_docs = []
key_terms = []

documents=['doc1.txt','doc2.txt','doc3.txt','doc4.txt','doc5.txt','doc6.txt']
result=[['doc1.txt','animals'],['doc2.txt','animals'],['doc3.txt','animals'],
        ['doc4.txt','sports'],['doc5.txt','sports'],['doc6.txt','sports']]

for x in documents:
    files.append(open(x,'r').read())


for x in files:
    all_docs.append(x.lower().rstrip('\n'))

for x in all_docs:
    key_terms = key_terms+ x.split()

key_terms = list(set(key_terms))

#filename = raw_input("Enter test file :")
filename = 'test1.txt'
inputfile = open(filename,'r').readline().lower()

cnt = 0
for x in all_docs:
    result[cnt] = result[cnt] + [cos_sim(inputfile,x,key_terms)]
    cnt = cnt + 1
print result
