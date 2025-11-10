def dot(a, b):
    total = 0
    for ai, bi in zip(a, b):
        total += ai * bi
    return total


def matvec(M, v):
    result = []
    for row in M:
        total = 0
        for i in range(len(v)):
            total += row[i] * v[i]
        result.append(total)
    return result


print(dot([2,3,4], [1,0,-1]))            # -2
print(matvec([[1,2],[3,4]], [5,6]))      # [17, 39]
