from random import randint
import math

board = []
cost = 0
red = 'r'
white = 'w'

def check_fjump_right(piece,board,color):
	if(color == 'r' and piece+7<=55):
		if( board[piece+7] == 2 or board[piece+7] == 4):
			if(piece+14<=63 and board[piece+14] == 1):
				return True
			else:
				return False
		else:
			return False
	elif(color == 'w' and piece-7>=0):
		if( board[piece-7] == 3 or board[piece-7] == 5):
			if(piece-14>=0 and board[piece-14] == 1):
				return True
			else:
				return False
		else:
			return False
		
def check_fmove_right(piece,board,color):
	if(color == 'r'):
		if(piece+7<=63 and board[piece+7] == 1):
			return True
		else:
			return False
	elif(color == 'w'):
		if(piece-7>=0 and board[piece-7] == 1):
			return True
		else:
			return False
			
def check_fjump_left(piece,board,color):
	if(color == 'r' and piece+9<=55 ):
		if(board[piece+9] == 2 or board[piece+9] == 4):
			if(piece+18<=63 and board[piece+18] == 1):
				return True
			else:
				return False
		else:
			return False
	elif(color == 'w' and piece-9>=8 ):
		if(board[piece-9] == 3 or board[piece-9] == 5):
			if(piece-18>=0 and board[piece-18] == 1):
				return True
			else:
				return False
		else:
			return False

def check_fmove_left(piece,board,color):
	if(color == 'r'):
		if(piece+9<=63 and board[piece+9] == 1):
			return True
		else:
			return False
	elif(color == 'w'):
		if(piece-9>=0 and board[piece-9] == 1):
			return True
		else:
			return False
		
def check_bjump_right(piece,board,color):
	if(color == 'r'and piece-9>=8):
		if( board[piece-9] == 2 or board[piece-9] == 4):
			if(piece-18>=0 and board[piece-18] == 1):
				return True
			else:
				return False
		else:
			return False
	elif(color == 'w' and piece+9<=63):
		if( board[piece+9] == 3 or board[piece+9] == 5):
			if(piece+18<=63 and board[piece+18] == 1):
				return True
			else:
				return False
		else:
			return False
		
def check_bmove_right(piece,board,color):
	if(color == 'r'):
		if(piece-9>=0 and board[piece-9] == 1):
			return True
		else:
			return False
	elif(color == 'w'):
		if(piece+9<=63 and board[piece+9] == 1):
			return True
		else:
			return False
		
def check_bjump_left(piece,board,color):
	if(color == 'r' and piece-7>=8 ):
		if( board[piece-7] == 2 or board[piece-7] == 4):
			if(piece-14>=0 and board[piece-14] == 1):
				return True
			else:
				return False
		else:
			return False
	if(color == 'w' and piece+7<=55):
		if(board[piece+7] == 3 or board[piece+7] == 5):
			if(piece+14<=63 and board[piece+14] == 1):
				return True
			else:
				return False
		else:
			return False

def check_bmove_left(piece,board,color):
	if(color == 'r'):
		if(piece-7>=0 and board[piece-7] == 1):
			return True
		else:
			return False
	if(color == 'w'):
		if(piece+7<=63 and board[piece+7] == 1):
			return True
		else:
			return False

def make_fjump_right(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece+14]
		board[piece+14] = temp
		if(board[piece+7] == 2):
			cost =1
		else:
			cost = 5
		if piece+14 >= 56 and (board[piece+14] == 3):	
			board[piece+14] = 5
			if(board[piece+7] == 2):
				cost = 4
			else:
				cost = 8
		board[piece+7] = 1
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece-14]
		board[piece-14] = temp
		if(board[piece-7] == 3):
			cost = -1
		else:
			cost = -5
		if piece-14 <= 7 and (board[piece-14] == 4):
			board[piece-14] = 4
			if(board[piece-7] == 3):
				cost = -4
			else:
				cost = -8
		board[piece-7] = 1
	return board,cost
	
def make_fjump_left(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece+18]
		board[piece+18] = temp
		if(board[piece+9] == 2):
			cost = 1
		else:
			cost = 5
		if piece+18 >= 56 and (board[piece+18] == 3):
			board[piece+18] = 5
			if(board[piece+9] == 2):
				cost = 4
			else:
				cost = 8
		board[piece+9] = 1
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece-18]
		board[piece-18] = temp
		if(board[piece-9] == 3):
			cost = -1
		else:
			cost = -5
		if piece-18 <= 7 and (board[piece-18] == 2):
			board[piece-18] = 4
			if(board[piece-9] == 3):
				cost = -4
			else:
				cost = -8
		board[piece-9] = 1
	return board,cost
	
def make_bjump_left(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece-14]
		board[piece-14] = temp
		if(board[piece-7] == 2):
			cost = 1
		else:
			cost = 5
		board[piece-7] = 1
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece+14]
		board[piece+14] = temp
		if(board[piece+7] == 3):
			cost =-1
		else:
			cost = -5
		board[piece+7] = 1
	return board,cost

def make_bjump_right(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece-18]
		board[piece-18] = temp
		if(board[piece-9] == 2):
			cost = 1
		else:
			cost = 5
		board[piece-9] = 1
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece+18]
		board[piece+18] = temp
		if(board[piece+9] == 3):
			cost =-1
		else:
			cost =-5
		board[piece+9] = -1
	return board,cost

def make_fmove_right(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece+7]
		board[piece+7] = temp
		cost = 0
		if piece+7 >= 56 and (board[piece+7] == 3):
			board[piece+7] = 5
			cost = 3
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece-7]
		board[piece-7] = temp
		cost = 0
		if piece-7 <= 7 and (board[piece-7] == 2):
			board[piece-7] = 4
			cost = -3
	return board,cost
	
def make_fmove_left(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece+9]
		board[piece+9] = temp
		cost = 0
		if piece+9 >= 56 and (board[piece+9] == 3):
			board[piece+9] = 5
			cost = 3
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece-9]
		board[piece-9] = temp
		cost = 0
		if piece-9 <= 7 and (board[piece-9] == 2):
			board[piece-9] = 4
			cost = -3
	return board,cost
	
def make_bmove_left(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece-7]
		board[piece-7] = temp
		cost = 0
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece+7]
		board[piece+7] = temp
		cost = 0
	return board,cost

def make_bmove_right(piece,board,color):
	if(color == 'r'):
		temp = board[piece];
		board[piece] = board [piece-9]
		board[piece-9] = temp
		cost = 0
	elif(color == 'w'):
		temp = board[piece];
		board[piece] = board [piece+9]
		board[piece+9] = temp
		cost = 0
	return board,cost

def string_key_to_list(move):
	converted = []
	for i in move:
		if(i.isdigit()):
			converted.append(int(i))
	return converted

def get_best_move(moves,color):
	final = []
	if(not moves == {}):
		v = list(moves.values())
		k = list(moves.keys())
		if(color=='r'):
			final = k[v.index(max(v))]
		elif(color=='w'):
			final = k[v.index(min(v))]
	return final

def gen_red_play(board,turn):
	for i in reversed(range(len(board))):
		if(i%8==7):
			#print ("Enters end right")
			if(board[i]== 5):
				if(check_bjump_right(i,board,red)):
					gen_board,value = make_bjump_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i-18,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i-18,value)
					#print ("%d move back jump right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,red)
					if jumped == 5:
						board[i-9] = 4
					else: 
						board[i-9] = 2
					break
					
			if(board[i]== 5):		
				if(check_bmove_right(i,board,red)):
					gen_board,value = make_bmove_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move back move right"%(i))
					board,value = make_bmove_right(i,board,red)
					
			if(board[i] == 3 or board[i] == 5):
				if(check_fjump_right(i,board,red)):
					gen_board,value = make_fjump_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i+14,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i+14,value)
					#print ("%d move right jump"%(i) )
					jumped = value
					board,value = make_fjump_right(i,board,red)
					if jumped == 5:
						board[i+7] = 4
					else: 
						board[i+7] = 2
					break
	
			if(board[i] == 3 or board[i] == 5):		
				if(check_fmove_right(i,board,red)):
					gen_board,value = make_fmove_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move right"%(i))
					board,value = make_fmove_right(i,board,red)
					
		elif(i%8 == 0):
			#print ("Enters end left")
			if(board[i]==5):
				if(check_bjump_left(i,board,red)):
					gen_board,value = make_bjump_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i-14,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i-14,value)
					#print ("%d move left back jump"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,red)
					if jumped == 5:
						board[i-7] = 4
					else: 
						board[i-7] = 2
					break
			if(board[i]==5):	
				if(check_bmove_left(i,board,red)):
					gen_board,value = make_bmove_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move back left"%(i))
					board,value = make_bmove_left(i,board,red)
					
			if(board[i] == 3 or board[i] == 5):
				if(check_fjump_left(i,board,red)):
					gen_board,value = make_fjump_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i+18,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i+18,value)
					#print ("%d move left jump"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,red)
					if jumped == 5:
						board[i+9] = 4
					else: 
						board[i+9] = 2
					break
			
			if(board[i] == 3 or board[i] == 5):		
				if(check_fmove_left(i,board,red)):
					gen_board,value = make_fmove_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move left"%(i))
					board,value = make_fmove_left(i,board,red)
			
					
		else: 
			#print ("Enters normal piece")
			if(board[i] == 5):
				if(check_bjump_right(i,board,red)):
					gen_board,value = make_bjump_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i-18,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i-18,value)
					#print ("%d move jump back right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,red)
					if jumped == 5:
						board[i-9] = 4
					else: 
						board[i-9] = 2
					break
					
				if(check_bjump_left(i,board,red)):
					gen_board,value = make_bjump_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i-14,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i-14,value)
					#print ("%d move jump back left"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,red)
					if jumped == 5:
						board[i-7] = 4
					else: 
						board[i-7] = 2
					break
					
			if(board[i] == 5):	
				if(check_bmove_right(i,board,red)):
					gen_board,value = make_bmove_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move back right"%(i))
					board,value = make_bmove_right(i,board,red)
					
				if(check_bmove_left(i,board,red)):
					gen_board,value = make_bmove_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move back left"%(i))
					board,value = make_bmove_left(i,board,red)
					
			if(board[i] == 3 or board[i] == 5):
				if(check_fjump_right(i,board,red)):
					gen_board,value = make_fjump_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i+14,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i+14,value)
					#print ("%d move jump right"%(i))
					jumped = value
					board,value = make_fjump_right(i,board,red)
					if jumped == 5:
						board[i+7] = 4
					else: 
						board[i+7] = 2
					break
					
				if(check_fjump_left(i,board,red)):
					gen_board,value = make_fjump_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
						gen_red_multiple(gen_board,1,i+18,value)
					elif turn==2:
						red_play2[str(gen_board)] = value
						gen_red_multiple(gen_board,2,i+18,value)
					#print ("%d move jump left"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,red)
					if jumped == 5:
						board[i+9] = 4
					else: 
						board[i+9] = 2
					break
			
			if(board[i] == 3 or board[i] == 5):
				if(check_fmove_right(i,board,red)):
					gen_board,value = make_fmove_right(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move right"%(i))
					board,value = make_fmove_right(i,board,red)
					
				if(check_fmove_left(i,board,red)):
					gen_board,value = make_fmove_left(i,board,red)
					if turn==1:
						red_play1[str(gen_board)] = value
					elif turn==2:
						red_play2[str(gen_board)] = value
					#print ("%d move left"%(i))
					board,value = make_fmove_left(i,board,red)
			
						
	if turn == 1:
		#print ("red play 1")
		return red_play1
	else:
		#print ("red play 2")
		return red_play2
		
def gen_red_multiple(board,turn,i,prev_value):
	if(i%8==7):
		#print ("Enters end right")
		if(board[i]== 5):
			if(check_bjump_right(i,board,red)):
				gen_board,value = make_bjump_right(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move back jump right"%(i))
				jumped = value
				board,value = make_bjump_right(i,board,red)
				if jumped == 5:
					board[i-9] = 4
				else: 
					board[i-9] = 2
					
		if(board[i] == 3 or board[i] == 5):
			if(check_fjump_right(i,board,red)):
				gen_board,value = make_fjump_right(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move right jump"%(i) )
				jumped = value
				board,value = make_fjump_right(i,board,red)
				if jumped == 5:
					board[i+7] = 4
				else: 
					board[i+7] = 2

				
	elif(i%8 == 0):
		#print ("Enters end left")
		if(board[i]==5):
			if(check_bjump_left(i,board,red)):
				gen_board,value = make_bjump_left(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move left back jump"%(i))
				jumped = value
				board,value = make_bjump_left(i,board,red)
				if jumped == 5:
					board[i-7] = 4
				else: 
					board[i-7] = 2
					
		if(board[i] == 3 or board[i] == 5):
			if(check_fjump_left(i,board,red)):
				gen_board,value = make_fjump_left(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move left jump"%(i))
				jumped = value
				board,value = make_fjump_left(i,board,red)
				if jumped == 5:
					board[i+9] = 4
				else: 
					board[i+9] = 2

	else: 
		#print ("Enters normal piece")
		if(board[i] == 5):
			if(check_bjump_right(i,board,red)):
				gen_board,value = make_bjump_right(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move jump back right"%(i))
				jumped = value
				board,value = make_bjump_right(i,board,red)
				if jumped == 5:
					board[i-9] = 4
				else: 
					board[i-9] = 2
	
				
			if(check_bjump_left(i,board,red)):
				gen_board,value = make_bjump_left(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move jump back left"%(i))
				jumped = value
				board,value = make_bjump_left(i,board,red)
				if jumped == 5:
					board[i-7] = 4
				else: 
					board[i-7] = 2				
		
		if(board[i] == 3 or board[i] == 5):
			if(check_fjump_right(i,board,red)):
				gen_board,value = make_fjump_right(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move jump right"%(i))
				jumped = value
				board,value = make_fjump_right(i,board,red)
				if jumped == 5:
					board[i+7] = 4
				else: 
					board[i+7] = 2

				
			if(check_fjump_left(i,board,red)):
				gen_board,value = make_fjump_left(i,board,red)
				if turn==1:
					red_play1j[str(gen_board)] = value + prev_value
				elif turn==2:
					red_play2j[str(gen_board)] = value + prev_value
				#print ("%d move jump left"%(i))
				jumped = value
				board,value = make_fjump_left(i,board,red)
				if jumped == 5:
					board[i+9] = 4
				else: 
					board[i+9] = 2
				
				
		
				
	if turn == 1:
		#print ("red play 1 Multiple")
		return red_play1j
	else:
		#print ("red play 2 Multiple")
		return red_play2j

def gen_white_play(board):
	for i in range(len(board)):
		if(i%8==0):
			#print ("Enters end right")
			if(board[i]== 4):
				if(check_bjump_right(i,board,white)):
					gen_board,value = make_bjump_right(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i+18,value)
					#print ("%d move back jump right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,white)
					if jumped == 5:
						board[i+9] = 5
					else: 
						board[i+9] = 3
					break
					
				if(check_bmove_right(i,board,white)):
					gen_board,value = make_bmove_right(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move back move right"%(i))
					board,value = make_bmove_right(i,board,white)
					
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_right(i,board,white)):
					gen_board,value = make_fjump_right(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i-14,value)
					#print ("%d move right jump"%(i) )
					jumped = value
					board,value = make_fjump_right(i,board,white)
					if jumped == 5:
						board[i-7] = 5
					else: 
						board[i-7] = 3
					break
					
				if(check_fmove_right(i,board,white)):
					gen_board,value = make_fmove_right(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move right"%(i))
					board,value = make_fmove_right(i,board,white)
							
		elif(i%8 == 7):
			#print ("Enters end left")
			if(board[i]==4):
				if(check_bjump_left(i,board,white)):
					gen_board,value = make_bjump_left(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i+14,value)
					#print ("%d move left back jump"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,white)
					if jumped == 5:
						board[i+7] = 5
					else: 
						board[i+7] = 3
					break
					
				if(check_bmove_left(i,board,white)):
					gen_board,value = make_bmove_left(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move back left"%(i))
					board,value = make_bmove_left(i,board,white)
					
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_left(i,board,white)):
					gen_board,value = make_fjump_left(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i-18,value)
					#print ("%d move left jump"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,white)
					if jumped == 5:
						board[i-9] = 5
					else: 
						board[i-9] = 3
					break
					
				if(check_fmove_left(i,board,white)):
					gen_board,value = make_fmove_left(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move left"%(i))
					board,value = make_fmove_left(i,board,white)
								
		else: 
			#print ("Enters normal piece")
						
			if(board[i] == 4):
				if(check_bjump_right(i,board,white)):
					gen_board,value = make_bjump_right(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i+18,value)
					#print ("%d move jump back right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,white)
					if jumped == 5:
						board[i+9] = 5
					else: 
						board[i+9] = 3
					break
					
				if(check_bjump_left(i,board,white)):
					gen_board,value = make_bjump_left(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i+14,value)
					#print ("%d move jump back left"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,white)
					if jumped == 5:
						board[i+7] = 5
					else: 
						board[i+7] = 3
					break
					
				if(check_bmove_right(i,board,white)):
					gen_board,value = make_bmove_right(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move back right"%(i))
					board,value = make_bmove_right(i,board,white)
					
				if(check_bmove_left(i,board,white)):
					gen_board,value = make_bmove_left(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move back left"%(i))
					board,value = make_bmove_left(i,board,white)
					
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_right(i,board,white)):
					gen_board,value = make_fjump_right(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i-14,value)
					#print ("%d move jump right"%(i))
					jumped = value
					board,value = make_fjump_right(i,board,white)
					if jumped == 5:
						board[i-7] = 5
					else: 
						board[i-7] = 3
					break
					
				if(check_fjump_left(i,board,white)):
					gen_board,value = make_fjump_left(i,board,white)
					white_play[str(gen_board)] = value
					gen_white_multiple(gen_board,i-18,value)
					#print ("%d move jump left"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,white)
					if jumped == 5:
						board[i-9] = 5
					else: 
						board[i-9] = 3
					break
					
				if(check_fmove_right(i,board,white)):
					gen_board,value = make_fmove_right(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move right"%(i))
					board,value = make_fmove_right(i,board,white)
					
				if(check_fmove_left(i,board,white)):
					gen_board,value = make_fmove_left(i,board,white)
					white_play[str(gen_board)] = value
					#print ("%d move left"%(i))
					board,value = make_fmove_left(i,board,white)
		
					
				

	#print ("white play")
	return white_play

def gen_white_multiple(board,i,prev_value):
	for i in range(len(board)):
		if(i%8==0):
			#print ("Enters end right")
			if(board[i]== 4):
				if(check_bjump_right(i,board,white)):
					gen_board,value = make_bjump_right(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move back jump right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,white)
					if jumped == 5:
						board[i+9] = 5
					else: 
						board[i+9] = 3
					break
					
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_right(i,board,white)):
					gen_board,value = make_fjump_right(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move right jump"%(i) )
					jumped = value
					board,value = make_fjump_right(i,board,white)
					if jumped == 5:
						board[i-7] = 5
					else: 
						board[i-7] = 3
					break
				
					
			
					
		elif(i%8 == 7):
			#print ("Enters end left")
			if(board[i]==4):
				if(check_bjump_left(i,board,white)):
					gen_board,value = make_bjump_left(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move left back jump"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,white)
					if jumped == 5:
						board[i+7] = 5
					else: 
						board[i+7] = 3
					break
			
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_left(i,board,white)):
					gen_board,value = make_fjump_left(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move left jump"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,white)
					if jumped == 5:
						board[i-9] = 5
					else: 
						board[i-9] = 3
					break
					
		
		else: 
			#print ("Enters normal piece")
			if(board[i] == 4):
				if(check_bjump_right(i,board,white)):
					gen_board,value = make_bjump_right(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move jump back right"%(i))
					jumped = value
					board,value = make_bjump_right(i,board,white)
					if jumped == 5:
						board[i+9] = 5
					else: 
						board[i+9] = 3
					break
					
				if(check_bjump_left(i,board,white)):
					gen_board,value = make_bjump_left(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move jump back left"%(i))
					jumped = value
					board,value = make_bjump_left(i,board,white)
					if jumped == 5:
						board[i+7] = 5
					else: 
						board[i+7] = 3
					break
			
			if(board[i] == 2 or board[i] == 4):
				if(check_fjump_right(i,board,white)):
					gen_board,value = make_fjump_right(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move jump right"%(i))
					jumped = value
					board,value = make_fjump_right(i,board,white)
					if jumped == 5:
						board[i-7] = 5
					else: 
						board[i-7] = 3
					break
					
				if(check_fjump_left(i,board,white)):
					gen_board,value = make_fjump_left(i,board,white)
					white_playj[str(gen_board)] = value + prev_value
					#print ("%d move jump left"%(i))
					jumped = value
					board,value = make_fjump_left(i,board,white)
					if jumped == 5:
						board[i-9] = 5
					else: 
						board[i-9] = 3
					break
					
		
									
	#print ("white Multiple")
	return white_playj
	



def number_of_pieces(board):
	red_nos = 0
	white_nos = 0
	for i in board:
		if(i==2 or i == 4):
			white_nos+=  1
		elif(i == 3 or i == 5):
			red_nos+=  1
	return white_nos,red_nos
		
red_play1 = {}
red_play2 = {}
red_play1j = {}
red_play2j = {}
white_play = {}
white_playj = {}



def reshape_list(original_list):
    # assumes original_list is a perfect square length (e.g. 9 or 16)
    i = 0
    new_list = []
    while i < len(original_list):
        new_list.append(original_list[i:i+int(math.sqrt(len(original_list)))])
        i += int(math.sqrt(len(original_list)))
    return new_list


def minimax(board):
	global red_play1 
	global red_play2 
	global red_play1j 
	global red_play2j 
	global white_play 
	global white_playj 
	
	gen_red_play(board,1)
	for i in red_play1j:
		red_play1[i] = red_play1j[i]
	for i in red_play1:
		red1_value = red_play1[i]
		gen_white_play(string_key_to_list(i))
		for j in white_playj:
			white_play[j] = white_playj[j]
		if(not white_play == {}):
			best_white = get_best_move(white_play,white)
			best_white = string_key_to_list(best_white)
			white_value = white_play[get_best_move(white_play,white)]
			gen_red_play(best_white,2)
			for k in red_play2j:
				red_play2[k] = red_play2j[k]
			if(not red_play2 == {}):
				best_red2 = get_best_move(red_play2,red)
				red2_value = red_play2[best_red2]
				red_play1[i]= red1_value + white_play[get_best_move(white_play,white)]+red2_value
			else: 
				break
		else: 
			break
		
	final = get_best_move(red_play1,red)
	final = string_key_to_list(final)
	red_play1 = {}
	red_play2 = {}
	red_play1j = {}
	red_play2j = {}
	white_play = {}
	white_playj = {}
	return final






