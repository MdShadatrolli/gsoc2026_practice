import math

def bernoulli_pmf(x, p):
    if x == 1:
        return p
    elif x == 0:
        return 1 - p
    else:
        return 0


def nCr(n, r):
    from math import factorial
    return factorial(n) // (factorial(r) * factorial(n - r))


def binomial_pmf(k, n, p):
    if k < 0 or k > n:
        return 0
    return nCr(n, k) * (p ** k) * ((1 - p) ** (n - k))


def normal_pdf(x, mu, sigma):
    part1 = 1 / (math.sqrt(2 * math.pi) * sigma)
    part2 = math.exp(- ((x - mu) ** 2) / (2 * sigma * sigma))
    return part1 * part2


if __name__ == "__main__":
    print(bernoulli_pmf(1, 0.6))
    print(binomial_pmf(3, 10, 0.5))
    print(normal_pdf(0, 0, 1))
