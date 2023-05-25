def numCells(grid):
    # Write your code here
    
    domCell = 0
    for i in range(len(grid)):
        for j in range (len(grid[0])):
            val = grid[i][j]
            flag = 1
            for ii in range (max(0,i-1),min(len(grid),i+2)):
                for jj in range(max(0,j-1),min(len(grid[0]),j+2)):
                    if (ii,jj)!=(i,j) and val<= grid[ii][jj] :
                         flag=0
                         break 
                if flag == 0:
                     break
            else:
                domCell+=1
    return domCell
