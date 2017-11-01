### Check other code for detailed comments B10.py
## B10 - APRIORI
import collections

def prune(last_table,min_sup):
    items = last_table.keys()
    for item in items:
        if last_table[item]<min_sup:
            last_table.pop(item,None)


def get_sup_count(db,line):
    items = line.split(',')
    count = 0
    for i in db:

        if(set(items).issubset(set(i))):
            count = count + 1
    return count



def self_join(db,last_key,k):
    items = last_key.keys()
    last_table.clear()

    for i in xrange(len(items)):
        j = i+1
        keysi = items[i].split(',')
        while j<(len(items)):
            keysj = items[j].split(',')

            nset = list(set(keysi)|set(keysj))
            #print nset
            if(len(nset)==k):
                line = ""
            for l in xrange(len(nset)-1):   ## len -1 remember
                line = line + str(nset[l])+','
            line = line + str(nset[l+1])

            last_table[line] = get_sup_count(db,line)

            j = j+1




f = open('transactions.csv','r')

db = []
last_table = {}

for line in f:
    line = line.replace('\n','')
    fline = line.split(',')
    db.append(fline)

#print db


for trans in db:
    for item in trans:
        if(last_table.has_key(item) and item!='-'):
            last_table[item] = last_table[item]+1
        elif not last_table.has_key(item) and item!='-':
            last_table[item] = 1
            k=2

while True:
    values = last_table.values()
    keys = last_table.keys()

    if len(keys)<1 :
        break
	print last_table
	print " "
    prune(last_table,3)
    print last_table
    self_join(db,last_table,k)

    k=k+1
