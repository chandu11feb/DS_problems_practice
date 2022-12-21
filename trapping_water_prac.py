def trapRainWater(List):
    length = []
    width = []
    for i in List:
        teml = []
        teml.append(i[0])
        for j in range(1, len(i)):
            teml.append(max(i[j], teml[j - 1]))
        length.append(teml)
    rev_length = []
    for i in List:
        teml = [0] * len(i)
        teml[len(i) - 1] = i[len(i) - 1]
        # print(teml)
        for j in range(len(i) - 2, -1, -1):
            teml[j] = max(i[j], teml[j + 1])
        rev_length.append(teml)
    for i in range(len(List[0])):
        teml = []
        teml.append(List[0][i])
        for j in range(1, len(List)):
            teml.append(max(List[j][i],teml[j-1]))
        width.append(teml)
    rev_width = []
    for i in range(len(List[0])):
        teml = [0] * len(List)
        teml[len(List) - 1] = List[len(List) - 1][i]
        for j in range(len(List) - 2, -1, -1):
            teml[j] = max(List[j][i],teml[j+1])
        rev_width.append(teml)
    print(length)
    print(width)
    print(rev_length)
    print(rev_width)
    capacity=0
    for i in range(1,len(List)-1):
        for j in range(1,len(List[0])-1):
            present_value=List[i][j]
            min_value=min(length[i][j],rev_length[i][j],width[j][i],rev_width[j][i])
            # print(present_value,min_value)
            if min_value>=present_value:
                capacity+=min_value-present_value

    return capacity
l=[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
print(trapRainWater((l)))



# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
# inputs
# [1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]