# Puzzle Solver
# Alex Mak
# 1/1/2025

# based on work from https://github.com/josephmaklc/wordsearchpuzzle
# puzzles of various dimensions can be generated from https://puzzlemaker.discoveryeducation.com/word-search
puzzle = []
solution = []
MAX_ROW = 0
MAX_COL = 0

def CheckWest(row, col, word):
	i = 0
	r = row
	c = col

	word_len = len(word)

	while (c >= 0 and i < word_len and puzzle[r][c] == word[i]) :
		c -= 1
		i+= 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row][col -n] = True

		return True

	return False

def CheckEast(row, col, word):
 
	i = 0
	r = row
	c = col

	word_len = len(word)
	
	while (c < MAX_COL and i < word_len and puzzle[r][c] == word[i]) :
		c += 1
		i += 1

	if (i == word_len):

		for n in range(0, word_len):
			solution[row][col + n] = True

		return True

	return False

def CheckNorth(row, col, word):

	i = 0
	r = row
	c = col

	word_len = len(word)
 
	while ( r >= 0 and i < word_len and puzzle[r][c] == word[i]):
		r -= 1
		i += 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row-n][col] = True

		return True

	return False  

def CheckSouth(row, col, word):

	i = 0
	r = row
	c = col
	word_len = len(word)
	
	while ( r < MAX_ROW and i < word_len and puzzle[r][c] == word[i]):
		r += 1
		i += 1

	if (i == word_len):

		for n in range(0, word_len):
			solution[row+n][col] = True

		return True

	return False

def CheckNorthWest(row, col, word):

	i = 0
	r = row
	c = col
	word_len = len(word)
	
	while ( r >= 0 and c >= 0 and i < word_len and puzzle[r][c] == word[i]):
		r -= 1
		c -= 1
		i += 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row-n][col-n] = True

		return True

	return False

def CheckNorthEast(row, col, word):

	i = 0
	r = row
	c = col
	word_len = len(word)
	
	while ( r >= 0 and c < MAX_COL and i < word_len and puzzle[r][c] == word[i]):
		r -= 1
		c += 1
		i += 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row-n][col+n] = True

		return True

	return False

def CheckSouthEast(row, col, word):

	i = 0
	r = row
	c = col
	word_len = len(word)

	while ( r < MAX_ROW and c < MAX_COL and i < word_len and puzzle[r][c] == word[i]):
		r += 1
		c += 1
		i += 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row+n][col+n] = True
		return True

	return False

def CheckSouthWest(row, col, word):
  
	i = 0
	r = row
	c = col
	word_len = len(word)
	
	while ( r < MAX_ROW and c >= 0 and i < word_len and puzzle[r][c] == word[i]):
		r += 1
		c -= 1
		i += 1

	if (i == word_len):
		for n in range(0, word_len):
			solution[row+n][col-n] = True
		return True

	return False

def ShowRuler():
	if (MAX_COL > 10):
		print("    " , end = "")
		for col in range(0, MAX_COL):
			if col % 10 == 0:
				print(int(col/10), end = "")
			else:
				print("-", end = "")

		print()

	print("    " , end = "")
	for col in range(0, MAX_COL):
		print(f"{col % 10}", end = "")

	print()

def ShowPuzzle():
  
	ShowRuler()

	for row in range(0, MAX_ROW):

		print (f" {row:2} ", end = "")
		for col in range(0, MAX_COL):
			
			print (puzzle[row][col], end="")
			#print(f"({row}, {col}) ", end = "")
		print()
		

def ShowSolution():

	print()

	ShowRuler()

	for row in range(0, MAX_ROW):

		print (f" {row:2} ", end = "")
		for col in range(0, MAX_COL):
			
			if (solution[row][col] == True):
				print (puzzle[row][col], end="")
			else:
				print(".", end = "")
			
		print()


def FindWord(word):

	word = word.upper()

	for row in range(0, MAX_ROW):
		for col in range(0, MAX_COL):
			
			w = CheckWest(row, col, word)
			e = CheckEast(row, col, word)
			n = CheckNorth(row, col, word)
			s = CheckSouth(row, col, word)
			nw = CheckNorthWest(row, col, word)
			ne = CheckNorthEast(row, col, word)
			se = CheckSouthEast(row, col, word)
			sw = CheckSouthWest(row, col, word)

			if any([w, e, n, s, nw, ne, se, sw]):
				return True

	return False

def ReadPuzzle(filename):

	global puzzle
	global MAX_ROW
	global MAX_COL
	global solution

	puzzle = [] 

	with open(filename) as f:
		for line in f.readlines():
			line = line.strip()
			puzzle.append(line.split('\t'))
	
	# zip iterate simutaneously multiple arrays
	columns = list(zip(*puzzle))

	MAX_ROW = len(puzzle)
	MAX_COL = len(columns)

	solution = [[False for _ in range(MAX_COL)] for _ in range(MAX_ROW)]

	print(f'puzzle file {filename} successfully read')

def menu():
	print('----------------')
	print('f. find word')
	print('p. show puzzle')
	print('s. show found words')
	print('q. quit')
	try:
		choice = input("Your choice: ")
	except:
		print("not valid")
		return menu()


	return choice

def main():
  
	ReadPuzzle('puzzle.txt')
	
	c = 1

	while c != 'q':
		c = menu()

		if (c == 'f'):
			word = input("Find a word: ")
			if FindWord(word) == True:
				print("### Word found! ###")
			else:
				print("--- Word not found ---")
		elif (c == 'p'):
			ShowPuzzle()
		elif (c == 's'):
			ShowSolution()


if __name__ == "__main__":
	main()
