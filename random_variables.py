def pmf(probabilities, x):
    """PMF for discrete random variable"""
    return probabilities.get(x, 0)


def cdf(probabilities, x):
    """CDF for discrete random variable"""
    total = 0
    for value, prob in probabilities.items():
        if value <= x:
            total += prob
    return total


def pdf_uniform(a, b, x):
    """PDF for a continuous uniform distribution"""
    if a <= x <= b:
        return 1 / (b - a)
    return 0


def expectation(probabilities):
    """Expected value of a discrete RV"""
    return sum(x * prob for x, prob in probabilities.items())


def variance(probabilities):
    """Variance of a discrete RV"""
    mean = expectation(probabilities)
    ex2 = sum((x**2) * prob for x, prob in probabilities.items())
    return ex2 - (mean ** 2)


if __name__ == "__main__":
    # Example discrete distribution for a fair die
    probs = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}

    print(pmf(probs, 3))
    print(cdf(probs, 4))
    print(pdf_uniform(0, 1, 0.5))
    print(expectation(probs))
    print(variance(probs))
