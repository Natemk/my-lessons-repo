"""''' 
 You are working on a logic game made up of a series of puzzles. The first type of puzzle you settle on is "sub-Sudoku", a game where the player has to position the
 numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix, returns true if  every row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters, so the matrix can contain any signed integer.

# The UI for the game doenst do any validation, therefore it is done in the backend.
# It validates the grid  if we have the numbers 1, 2, 3 otherwise it returns false.


grid1 = [[2, 3, 1],
         [1, 2, 3],
         [3, 1, 2]]                         -> True (A grid of size 3: every row and column contains the numbers 1,2,3)

#
# We want know the grid size, so our grid size is going to be our N, where N = size 
# print(grid1[0])

grid2 = [[2, 3, 1],
         [1, 2, 3],
         [3, 2, 1]]                         -> False (The second column is missing 1, and the third is missing 2.
                                                      They should all contain the numbers 1, 2, and 3)

grid3 = [[1]]                               -> True (A grid of size one: it contains 1 as the single value)

grid4 = [[0, 3],
         [3, 0]]                            -> False (All values should be 1 or 2)

grid5 = [[2, 3, 3],
         [1, 2, 1],
         [3, 1, 2]]                         -> False (The first row is missing the value 1 and the second row is missing the value 3)

grid6 = [[1, 4, 1, 4],
         [4, 1, 4, 1],
         [2, 3, 2, 3],
         [3, 2, 3, 2]]                      -> False (Each row and column should contain 1, 2, 3, and 4)

grid7 = [[2, 2, 2, 3],
         [2, 2, 3, 2],
         [2, 3, 2, 2],
         [3, 2, 2, 2]]                      -> False (Each row and column should contain 1, 2, 3, and 4, 
                                               but row 0 has three copies of 2 and is missing 1 and 4)

grid8 = [[-1, -2, 12, 1],
         [12, -1, 1, -2],
         [-2, 1, -1, 12],
         [1, 12, -2, -1]]                   -> False (Each row and column should contain 1, 2, 3, and 4.
                                               Row 0 contains -1 and -2, which are outside 1..4, and is missing 2 and 3)

grid9 = [[1, 2, 4, 4, 4, 5, 7, 9, 9],
         [2, 4, 4, 4, 5, 7, 9, 9, 1],
         [4, 4, 4, 5, 7, 9, 9, 1, 2],
         [4, 4, 5, 7, 9, 9, 1, 2, 4],
         [4, 5, 7, 9, 9, 1, 2, 4, 4],
         [5, 7, 9, 9, 1, 2, 4, 4, 4],
         [7, 9, 9, 1, 2, 4, 4, 4, 5],
         [9, 9, 1, 2, 4, 4, 4, 5, 7],
         [9, 1, 2, 4, 4, 4, 5, 7, 9]]       -> False (Each row and column should contain 1 through 9)

grid10 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
         [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
         [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
         [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
         [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
         [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
         [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
         [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
         [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]]   -> True

grid11 = [[0]]                              -> False
grid12 = [[2]]                              -> False

validateSudoku(grid1)     => True
validateSudoku(grid2)     => False
validateSudoku(grid3)     => True
validateSudoku(grid4)     => False
validateSudoku(grid5)     => False
validateSudoku(grid6)     => False
validateSudoku(grid7)     => False
validateSudoku(grid8)     => False
validateSudoku(grid9)     => False
validateSudoku(grid10)    => True
validateSudoku(grid11)    => False
validateSudoku(grid12)    => False

Complexity analysis variables:

N = The number of rows/columns in the matrix
'''
 
grid1 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 1, 2],
]
size = len(grid1)

#check if every row and column contains the numbers 1,2,3
# use size to check numbers 1 to 3 (one of each) are in grid1

def matrix(grid):
    for
    
    



grid2 = [
    [2, 3, 1],
    [1, 2, 3],
    [3, 2, 1],
]

grid3 = [
    [1],
]

grid4 = [
    [0, 3],
    [3, 0],
]

grid5 = [
    [2, 3, 3],
    [1, 2, 1],
    [3, 1, 2],
]

grid6 = [
    [1, 4, 1, 4],
    [4, 1, 4, 1],
    [2, 3, 2, 3],
    [3, 2, 3, 2],
]

grid7 = [
    [2, 2, 2, 3],
    [2, 2, 3, 2],
    [2, 3, 2, 2],
    [3, 2, 2, 2],
]

grid8 = [
    [-1, -2, 12, 1],
    [12, -1, 1, -2],
    [-2, 1, -1, 12],
    [1, 12, -2, -1],
]

grid9 = [
    [1, 2, 4, 4, 4, 5, 7, 9, 9],
    [2, 4, 4, 4, 5, 7, 9, 9, 1],
    [4, 4, 4, 5, 7, 9, 9, 1, 2],
    [4, 4, 5, 7, 9, 9, 1, 2, 4],
    [4, 5, 7, 9, 9, 1, 2, 4, 4],
    [5, 7, 9, 9, 1, 2, 4, 4, 4],
    [7, 9, 9, 1, 2, 4, 4, 4, 5],
    [9, 9, 1, 2, 4, 4, 4, 5, 7],
    [9, 1, 2, 4, 4, 4, 5, 7, 9],
]

grid10 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
    [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
    [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
    [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
    [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
    [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
    [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
    [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

grid11 = [
    [0],
]

grid12 = [
    [2],
]"""



size =int(input("Enter size of the grid: "))
grid =[]

for i in range(size):
    row = input(f"Enter row {1 + i}: ").split()
    row = [int(num) for num in row]
    grid.append(row)

def validateSudoku(grid):
    size = len(grid)
    correct = set(range(1, size + 1))
    
    for row in grid:
        if set(row) != correct:
            return False
       
    for col in range(size):
        column = []
        
        for row in grid:
            column.append(row[col])
            
        if set(column) != correct:
            return False
        
    return True

if validateSudoku(grid):
    print("Grid is valid:")
    for row in grid:
        print(row)
else:
    print("Grid is incorrect.")