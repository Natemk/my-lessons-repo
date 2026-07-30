grid1 = [[2, 3, 1],
         [1, 2, 3],
         [3, 1, 2]]                         #-> True (A grid of size 3: every row and column contains the numbers 1,2,3)

#
# We want know the grid size, so our grid size is going to be our N, where N = size 


#print(list(grid1[0]))

#second row
#print(list(grid1[1]))

#how to get the first number in every row
#print(grid1[0][0])

#for i in range(len(grid1))

#for i in range(len(grid1)):
#    print(grid1[i][2])
    
    
size = len(grid1)

for col in range(1, size + 1):
    print(list(grid1))
    
