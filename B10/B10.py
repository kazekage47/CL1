import collections
def prune(last_table,min_sup):
    items=last_table.keys()
    for item in items:
        if last_table[item]<min_sup:
            last_table.pop(item,None)

def get_sup_count(db,line):
    items=line.split(',')
    count=0
    for i in db:
    	#print set(items)
    	#print set(i)
        if set(items).issubset(set(i)):
            count=count+1
    return count

def self_join(db,last_table,k):
    items=last_table.keys()
    last_table.clear()
    for i in xrange(len(items)):
        j=i+1
        keysi=items[i].split(',')
        #print keysi
        #print '--'
        while j<(len(items)):
            keysj=items[j].split(',')
            #print keysj
            #print '================'
            nset=list(set(keysi)|set(keysj))
            #print nset
            if(len(nset)==k):
                line=""
            for l in xrange(len(nset)-1):
                line=line+str(nset[l])+','
            line=line+str(nset[l+1])
            #print line
            last_table[line]=get_sup_count(db,line)
            #print last_table[line]
            #print line
            j=j+1
      	#print "______________" 

f=open('transactions.csv','r')
db=[]					#list
last_table=dict()		#dictionary	

for line in f:
    line=line.replace('\n','')		
    fline=line.split(',')
    db.append(fline)
    
print db
#print "______________________________________"

    
#for trans in db:
#	print trans
#	print set(trans)
print "--------------------------------------"

#print last_table
for trans in db:
    for item in set(trans):
        if last_table.has_key(item) and item!='-':
            last_table[item]=last_table[item]+1
        elif not last_table.has_key(item) and item!='-':
            last_table[item]=1
            k=2
        


while True:
    values=last_table.values()    
    keys=last_table.keys()
    if len(keys)<1:
        break

    print last_table
    print ''
    prune(last_table,3)
    print last_table
    print "---"
    print ''
    self_join(db,last_table,k)
    k=k+1
    
