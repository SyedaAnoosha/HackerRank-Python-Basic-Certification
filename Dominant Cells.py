def numCells(grid):
    # Write your code here
    
    res = 0
    for i in range(len(grid)):
        for k in range (len(grid[0])):
            val = grid[i][k]
            flag = 1
            for ii in range (max(0,i-1),min(len(grid),i+2)):
                for kk in range(max(0,k-1),min(len(grid[0]),k+2)):
                    if (ii,kk)!=(i,k) and val<= grid[ii][kk] :
                         flag=0
                         break 
                if flag == 0:
                     break
            else:
                res+=1
    return res
