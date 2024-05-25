import math


def poisson_probability(lmbda, k):
    """
    Calculate the Poisson probability of observing k events given the average rate lmbda.

    Parameters:
    lmbda (float): The average rate (mean) of events.
    k (int): The number of events.

    Returns:
    float: The probability of observing k events.
    """
    log_p = k * math.log(lmbda) - lmbda - sum(math.log(i) for i in range(1, k + 1))
    return math.exp(log_p)


# Test cases
cases = [
    (250, 275),
    (300, 350),
    (100, 150)
]

for case in cases:
    lmbda, k = case
    probability = poisson_probability(lmbda, k)
    print(f"Case {cases.index(case) + 1}: {lmbda}, {k} {probability:.6f}")
