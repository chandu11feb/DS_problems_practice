def spiralprintingofmatrix(mat,rm,cm):
    r=0
    c=0
    while r<rm and c<cm:
        for i in range(c,cm):
            print(mat[r][i],end=" ")
        r+=1
        
        for i in range(r,rm):
            print(mat[i][cm-1],end=" ")
        cm-=1
        
        if r<rm:
            for i in range(cm-1,c-1,-1):
                print(mat[cm][i],end=" ")
            rm-=1
        if c<cm:
            for i in range(rm-1,r-1,-1):
                print(mat[i][c],end=" ")
            c+=1
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [12,14,15,16]]
m=len(matrix) # 4
n=len(matrix[0]) # 4
print(spiralprintingofmatrix(matrix,m,n))
