def add_vectors(a, b):
    return [a1+b1 for a1,b1 in zip(a,b)]

def mul_vectors(a, b):
    return [a1*b1 for a1,b1 in zip(a,b)]


def scalar_mul(c, v):
    return [c * x for x in v]
    
print(add_vectors([1,2,3], [4,5,6]))      # [5,7,9]
print(mul_vectors([1,2,3], [4,5,6]))      # [4,10,18]
print(scalar_mul(3, [1,2,3]))             # [3,6,9]
