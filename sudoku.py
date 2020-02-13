board = [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7],
]

# step1 -- pick empty squares
# step2 -- try all numbers
# step3 -- move to next empty square
# step4 -- Repeat
# step5 -- Backtrack


def print_board(board): #prints the board
	for i in range(len(board)):
			if i % 3==0 and i !=0:
				print("------  -------  -------")
			for j in range(len(board[i])):
				if j != 0 and j %3==0 :
					print (" | ", end="")
				if j==8 :	
					print(board[i][j])
				else:
					print(str(board[i][j]) + " ", end ="")

def find_empty(board): #finds the first empty element
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0 : 
				return i,j # row,col 
	return None				

def is_board_valid(board, num, pos): # Returns True/False (pos[0],pos[1])=(x,y)
	for k in range(len(board[0])):
		#check every row if found num
		if pos[1] != k and board[pos[0]][k] == num :
			return False
		#check every col if found num
		if pos[0] != k and board[k][pos[1]] == num :
			return False
		
	#check 3x3 square		
	x = pos[0] - (pos[0] % 3)		
	y = pos[1] - (pos[1] % 3)
	for i in range(3):	
		for j in range(3):
			if board[x+i][y+j] == num and (x+i,y+j) != pos :
				return False  
	return True


def solver(board): #recursion Returns True or False 
	#Base case of recursion
	find = find_empty(board)
	if not find:
		return True
	else: 
		row, col = find  

	for i in range(1,10):
		K = is_board_valid(board, i, (row,col))
		if K == True:
			board[row][col]=i
			# call solver on updated board
			if solver(board):
				return True
			else:
				board[row][col]=0

	return False	

print_board(board)
solver(board)	
print ("__________________")
print ("__________________")
print ("__________________")
print_board(board)