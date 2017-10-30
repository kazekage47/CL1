from lxml import etree
file='parse.xml'

a=[]
f=1

def shift( s ):
   if(s=='I'):
	return 1
   if(s=='+'):
	return 2
   if(s=='*'):
	return 3
   if(s=='('):
	return 4
   if(s==')'):
	return 5
   if(s=='$'):
	return 6
   if(s=='E'):
	return 7
   if(s=='T'):
	return 8
   if(s=='F'):
	return 9

def reduce( r ):
	if(r=='1'):
		return 'E',6
	if(r=='2'):
		return 'E',2
	if(r=='3'):
		return 'T',6
	if(r=='4'):
		return 'T',2
	if(r=='5'):
		return 'F',6
	if(r=='6'):
		return 'F',2
	

tree = etree.parse(file)
root = tree.getroot()

tree=['I','+','*','(',')','$','E','T','F']
print tree
for k in range(0,12):
	tree=[]
	for l in range(0,10):
		x=root[k][l].text
		tree.append(x)
	print tree
		
		

str=raw_input("Enter input string")  #string to be parsed
y=list(str)
y.append("$")


j=0	#input string pointer 
top=0					#stack initially 0
a.append(0)

sym=shift(y[j])
x=root[top][sym].text
l=list(x)


while(l[0]!='A'):
	

	if(l[0]=="S"):
		a.append(y[j])
		a.append(l[1])
		top=int(l[1])
		j=j+1


	elif(l[0]=="R"):
		symbol,val=reduce(l[1])
		for k in range(0,val):
			a.pop()
		a.append(symbol)
		lens=len(a)
		op1=a[lens-2]
		op=int(op1)
		sym1=shift(a[lens-1])
		sym=int(sym1)
		x=root[op][sym].text
		a.append(x)
	
	stack=[]
	for i in range(j+1,len(y)):	
		stack.append(y[i])
	print "Input string:	",stack,"Stack:	",a
	
	

	sym=shift(y[j])
	lens=len(a)
	top1=a[lens-1]
	top=int(top1)
	x=root[top][sym].text
	l=list(x)
	if(l[0]=='E'):
		print "Invalid string!!"
		f=0
		break

if(f==1):
	print "Valid string!!"
	
	
'''

arnav@arnav:~/Downloads/RashiCL1/ExamCl1/b8$ python parsexml.py 
['I', '+', '*', '(', ')', '$', 'E', 'T', 'F']
['0', 'S5', 'E', 'E', 'S4', 'E', 'E', '1', '2', '3']
['1', 'E', 'S6', 'E', 'E', 'E', 'A', 'E', 'E', 'E']
['2', 'E', 'R2', 'S7', 'E', 'R2', 'R2', 'E', 'E', 'E']
['3', 'E', 'R4', 'R4', 'E', 'R4', 'R4', 'E', 'E', 'E']
['4', 'S5', 'E', 'E', 'S4', 'E', 'E', '8', '2', '3']
['55', 'E', 'R6', 'R6', 'E', 'R6', 'R6', 'E', 'E', 'E']
['6', 'S5', 'E', 'E', 'S4', 'E', 'E', None, '9', '3']
['7', 'S5', 'E', 'E', 'S4', 'E', 'E', 'E', 'E', '10']
['8', 'E', 'S6', 'E', 'E', 'S11', 'E', 'E', 'E', 'E']
['9', 'E', 'R1', 'S7', 'E', 'R1', 'R1', 'E', 'E', 'E']
['10', None, 'R3', 'R3', None, 'R3', 'R3', 'E', 'E', 'E']
['11', 'E', 'R5', 'R5', 'E', 'R5', 'R5', 'E', 'E', 'E']
Enter input stringI*I+I*I
Input string:	['I', '+', 'I', '*', 'I', '$'] Stack:	[0, 'I', '5']
Input string:	['I', '+', 'I', '*', 'I', '$'] Stack:	[0, 'F', '3']
Input string:	['I', '+', 'I', '*', 'I', '$'] Stack:	[0, 'T', '2']
Input string:	['+', 'I', '*', 'I', '$'] Stack:	[0, 'T', '2', '*', '7']
Input string:	['I', '*', 'I', '$'] Stack:	[0, 'T', '2', '*', '7', 'I', '5']
Input string:	['I', '*', 'I', '$'] Stack:	[0, 'T', '2', '*', '7', 'F', '10']
Input string:	['I', '*', 'I', '$'] Stack:	[0, 'T', '2']
Input string:	['I', '*', 'I', '$'] Stack:	[0, 'E', '1']
Input string:	['*', 'I', '$'] Stack:	[0, 'E', '1', '+', '6']
Input string:	['I', '$'] Stack:	[0, 'E', '1', '+', '6', 'I', '5']
Input string:	['I', '$'] Stack:	[0, 'E', '1', '+', '6', 'F', '3']
Input string:	['I', '$'] Stack:	[0, 'E', '1', '+', '6', 'T', '9']
Input string:	['$'] Stack:	[0, 'E', '1', '+', '6', 'T', '9', '*', '7']
Input string:	[] Stack:	[0, 'E', '1', '+', '6', 'T', '9', '*', '7', 'I', '5']
Input string:	[] Stack:	[0, 'E', '1', '+', '6', 'T', '9', '*', '7', 'F', '10']
Input string:	[] Stack:	[0, 'E', '1', '+', '6', 'T', '9']
Input string:	[] Stack:	[0, 'E', '1']
Valid string!!

'''
