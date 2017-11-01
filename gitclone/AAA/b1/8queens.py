import json
inf=open("b1.json")
board=json.loads(inf.read())
board=board["matrix"]
n=8
#n=input()
#board=[[0 for x in range(n)] for y in range(n)] 

def issafe(row,col):
	for i in range(n):
		for j in range(n):
			if(board[i][j]==1):
				if(row==i):
					return False
				if(col==j):
					return False
				if(abs(row-i)==abs(col-j)):
					return False
	return True

def place(col):
	if(col>=n):
		print("completed")
		return True
	for i in range(n):
		if(issafe(i,col)):
			board[i][col]=1     # queen placed here
			if(place(col+1)==True):     # place next queen
				return True
			board[i][col]=0       # backtrack, set to 0 
	return False


if(place(1)==True):     #one queen should be there in first column
	print("solution found")
else:
	print("solution not found")
for i in board:
	print(i)
