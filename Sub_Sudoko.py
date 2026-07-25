size =int(input("Enter size of the grid: "))
grid =[]

for i in range(size):
    row = input(f"Enter row {1 + i}: "). split()
    row =[int(num) for num in row]
    grid.append(row)

def validateSudoku(grid):
    size = len(grid)
    correct = set(range(1, size +1))
    
    for row in grid:
       if set(row) != correct:
           return False
       
    for col in range(size):
        column = []
        
        for row in grid:
            column.append(row[column])
            
        if set(column) != correct:
            return False
        
        
    print(grid)    
    return True