l=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in l:
    print(i)
co=len(l[0])-1
r=0
rm=len(l)
c=0
cm=len(l[0])
for _ in range(co):
    temp=[]
    
    if r<rm and c<cm:
        for i in range(c,cm):
            temp.append(l[r][i])
        for i in range(r+1,rm):
            temp.append(l[i][cm-1])
        for i in range(cm-1-1,c-1,-1):
            temp.append(l[rm-1][i])
        for i in range(rm-1-1,r,-1):
            temp.append(l[i][c])
        temp=temp[len(temp)-1:]+temp[:len(temp)-1]
        j=0
        for i in range(c,cm):
            l[r][i]=temp[j]
            j+=1
        for i in range(r+1,rm):
            l[i][cm-1]=temp[j]
            j+=1
        for i in range(cm-1-1,c-1,-1):
            l[rm-1][i]=temp[j]
            j+=1
        for i in range(rm-1-1,r,-1):
            l[i][c]=temp[j]
            j+=1
        r+=1
        rm-=1
        c+=1
        cm-=1
    else:
        break
print()
for i in l:
    print(i)
    