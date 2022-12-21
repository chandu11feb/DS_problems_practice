# program to find total number of ways to reach to source node to destination node without having any cycle.
from collections import deque

def is_not_visited(num,path):
    for i in range(len(path)):
        if path[i]==num:
            return 0
    return 1
def all_paths(graph,source,dest):
    # graph : 2D array with list containing connecting nodes placed at index of origin node.
    q=deque()
    path=[]
    path.append(source)
    pathlist=[]
    q.append(path.copy())

    while q:
        path=q.popleft()
        last=path[len(path)-1]
        if last==dest:
            pathlist.append(path)
        for i in range(len(graph[last])):
            if is_not_visited(graph[last][i],path):
                newpath=path.copy()
                newpath.append(graph[last][i])
                q.append(newpath)
    return pathlist

n,v=map(int,input("Enter number of Nodes and vertices").split())
graph=[[] for _ in range(n+1)]
for i in range(v):
    start,end=map(int,input().split())
    graph[start].append(end)
source=1
dest=n
all_paths_list=all_paths(graph,source,dest)
print(all_paths_list)

"""
# input1

7 11
1 5
5 2
1 4
4 6
2 1
6 7
3 7
7 5
3 6
2 3
2 4

# input2

7 11
1 2
1 3
2 4
2 6
3 5
4 3
4 5
4 6
4 7
5 7
6 7


#input3

10 20
1 2
1 3
2 4
2 6
3 5
4 3
4 5
4 6
4 7
5 7
6 7
1 4
1 6
3 7
2 7
5 6
6 3
7 2
8 10
9 10

"""
