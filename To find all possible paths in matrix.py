def printAllPathsUtil(mat, i, j, m, n, path, pi): 
  
    if (i == m - 1): 
        for k in range(j, n): 
            path[pi + k - j] = mat[i][k] 
  
        for l in range(pi + n - j): 
            print(path[l], end = " ") 
        print() 
        return
  
    
    if (j == n - 1): 
  
        for k in range(i, m): 
            path[pi + k - i] = mat[k][j] 
  
        for l in range(pi + m - i): 
            print(path[l], end = " ") 
        print() 
        return
  
     
    path[pi] = mat[i][j] 
    print(path)
    # Print all the paths  
    # that are possible after moving down 
    printAllPathsUtil(mat, i + 1, j, m, n, path, pi + 1) 
  
    # Print all the paths  
    # that are possible after moving right 
    printAllPathsUtil(mat, i, j + 1, m, n, path, pi + 1) 
  
    # Print all the paths  
    # that are possible after moving diagonal 
    # printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1); 
  

def printAllPaths(mat, m, n): 
  
    path = [0 for i in range(m + n)] 
    print(path)
    printAllPathsUtil(mat, 0, 0, m, n, path, 0) 
  

mat = [[1, 2, 3],  
       [4, 5, 6],[7,8,9]] 
  
printAllPaths(mat, 3, 3) 