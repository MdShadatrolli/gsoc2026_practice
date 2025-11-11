import math
def l1_norm(v):
    # return sum of absolute values
    return sum(abs(x) for x in v)

def l2_norm(v):
    # return square root of sum of squares
    return math.sqrt(sum(abs(x)**2 for x in v))
def inf_norm(v):
    # return max absolute value
    return max(abs(n) for n in v)

def norm(v):
    """Day 2 of implementing vector norm Eucledian norm"""
    return math.sqrt(sum(abs(x)*abs(x) for x in v))
def cosine(a, b):
    """Implementing cosine similarity"""
    dotprdct=0
    for a1,b1 in zip(a,b):
        dotprdct+=a1*b1
    #||a|| and ||b||
    x=math.sqrt(sum(i*i for i in a))
    y=math.sqrt(sum(i*i for i in b))
    final=dotprdct/(x*y)
    return final


def matmul(A, B):
    """Matrix multiplication for 2D lists"""
    # Number of rows in A and columns in B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions do not match for multiplication")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result



    
        

    




if __name__== "__main__":
    #DAy 1
    # creating l1 ,l2 ,inf_normobjects to verify
    print(l1_norm([3, -4, 2]))   # 9
    print(l2_norm([3, 4]))       # 5
    print(inf_norm([3, -4, 2]))  # 4


    #Day 2

    #Eucledian norm: testing
    print(norm([3,4]))  # should print 5

    #Cosine similarity
    print(cosine([2,3,1],[1,0,-1]))

    #Matrix Multiplication
    A = [[1,2],
     [3,4]]

    B = [[2,0],
        [1,2]]

    print(matmul(A, B))  # expected: [[4,4],[10,8]]




    
