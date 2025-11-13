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

def vector_projection(a, b):
    """Project vector a onto vector b"""
    # dot product
    dot = sum(a1 * b1 for a1, b1 in zip(a, b))
    # magnitude of b squared
    mag_b2 = sum(b1 ** 2 for b1 in b)
    # scalar multiplier
    scalar = dot / mag_b2
    # projection vector
    proj = [scalar * b1 for b1 in b]
    return proj

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def are_orthogonal(a, b, eps=1e-9):
    """
    Return True if vectors a and b are orthogonal (within numerical tolerance eps).
    - a, b: iterables of same length (extra elements past shortest are ignored).
    - eps: tolerance for floating point comparison.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length to compute orthogonality.")
    d = dot(a, b)
    return abs(d) < eps
    
def scalar_multiply(v, s):
    return [x * s for x in v]

def vector_sub(a, b):
    return [x - y for x, y in zip(a, b)]

def gram_schmidt(vectors):
    """Perform Gram-Schmidt orthonormalization on a list of vectors."""
    orthonormal = []
    
    for v in vectors:
        # Start with current vector
        u = v[:]
        for e in orthonormal:
            # Subtract projection on each previous orthonormal vector
            proj_coeff = dot(v, e)
            u = vector_sub(u, scalar_multiply(e, proj_coeff))
        
        # Normalize
        u_norm = norm(u)
        if u_norm == 0:
            raise ValueError("Vectors are linearly dependent")
        e = [x / u_norm for x in u]
        orthonormal.append(e)
    
    return orthonormal
      
def transpose(M):
    """Return the transpose of matrix M."""
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

    
def identity(n):
    """Return an identity matrix of size n×n."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def determinant_2x2(M):
    """Return determinant of a 2x2 matrix."""
    if len(M) == 2 and len(M[0]) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    else:
        raise ValueError("Only 2x2 matrices are supported in this function.")


def inverse_2x2(M):
    """Return inverse of a 2x2 matrix."""
    det = determinant_2x2(M)
    if det == 0:
        raise ValueError("Matrix is singular, no inverse exists.")
    
    a, b = M[0]
    c, d = M[1]
    return [[d/det, -b/det],
            [-c/det, a/det]]

def eigen_2x2(M):
    """Compute eigenvalues and eigenvectors of a 2x2 matrix."""
    a, b = M[0]
    c, d = M[1]

    # Characteristic equation: |A - λI| = 0 -> (a-λ)(d-λ) - bc = 0
    # λ^2 - (a+d)λ + (ad - bc) = 0
    trace = a + d
    determinant = a*d - b*c

    # Quadratic formula
    discriminant = math.sqrt(trace**2 - 4*determinant)
    λ1 = (trace + discriminant) / 2
    λ2 = (trace - discriminant) / 2

    return λ1, λ2


def eigenvector_2x2(M, λ):
    """Find eigenvector for given λ."""
    a, b = M[0]
    c, d = M[1]
    # Solve (A - λI)v = 0
    return [b, λ - a]  # Simplified for 2x2 symmetric case


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
    a = [2, 3]
    b = [1, 0]
    print("Projection of a on b:", vector_projection(a, b))


    a = [1.0, 2.0]
    b = [-2.0, 1.0]
    print("dot:", dot(a, b))                       # 0.0
    print("norm a:", norm(a))                     # sqrt(5)
    print("orthogonal?", are_orthogonal(a, b))    # True

    # a float example where dot is near zero
    a2 = [1e-10, 1.0]
    b2 = [0.0, 1.0]
    print("dot (near-zero):", dot(a2, b2))        # ~1.0
    print("orthogonal (tolerance):", are_orthogonal([1e-10, 1.0], [0.0, 1.0], eps=1e-9))


    
    vectors = [
        [1, 1],
        [1, 0]
    ]
    ortho = gram_schmidt(vectors)
    print("Orthonormal basis:")
    for e in ortho:
        print(e)


    A = [[1,2,3],
        [4,5,6]]

    print("Transpose of A:")
    for row in transpose(A):
        print(row)

    print("Identity Matrix (3x3):")
    for row in identity(3):
        print(row)


    A = [[1, 2],
         [3, 4]]

    I = identity(2)
    print("A × I =", matmul(A, I))
    print("I × A =", matmul(I, A))
    print("Transpose of A =", transpose(A))
    A = [[4, 6],
     [3, 8]]

    print("Determinant:", determinant_2x2(A))  # Expected 14



    A = [[4, 6],
        [3, 8]]

    invA = inverse_2x2(A)
    print("Inverse of A:")
    for row in invA:
        print(row)

    # Verify A * A^-1 = I
    print("Verification (A × A^-1):")
    for row in matmul(A, invA):
        print([round(x, 2) for x in row])


    A = [[2, 1],
        [1, 2]]

    λ1, λ2 = eigen_2x2(A)
    print("Eigenvalues:", λ1, λ2)

    print("Eigenvector for λ1:", eigenvector_2x2(A, λ1))
    print("Eigenvector for λ2:", eigenvector_2x2(A, λ2))
