def classical_probability(favourable, total):
    """Classical probability = favourable/total"""
    if total == 0:
        raise ValueError("Total outcomes cannot be zero")
    return favourable / total


def empirical_probability(event_count, total_trials):
    """Empirical probability based on observed data"""
    if total_trials == 0:
        raise ValueError("Total trials cannot be zero")
    return event_count / total_trials


def conditional_probability(p_a_and_b, p_b):
    """Conditional probability P(A|B)"""
    if p_b == 0:
        raise ValueError("P(B) cannot be zero")
    return p_a_and_b / p_b


def bayes_theorem(p_a, p_b_given_a, p_b):
    """Bayes theorem formula"""
    if p_b == 0:
        raise ValueError("P(B) cannot be zero")
    return (p_b_given_a * p_a) / p_b


if __name__ == "__main__":
    print(classical_probability(1, 6))  # P(rolling a 3 on a fair die)
    print(empirical_probability(55, 100))  # P(heads)
    print(conditional_probability(0.2, 0.5)) 
    print(bayes_theorem(0.01, 0.9, 0.1))
