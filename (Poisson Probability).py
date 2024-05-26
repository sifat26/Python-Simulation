import math
def poisson_probability(lmbda, k):

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
