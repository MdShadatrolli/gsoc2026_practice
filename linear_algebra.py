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
print(l1_norm([3, -4, 2]))   # 9
print(l2_norm([3, 4]))       # 5
print(inf_norm([3, -4, 2]))  # 4
