def linear_congruential_generator(seed, multiplier, increment, modulo, n):
    # Initialize the sequence with the seed
    random_numbers = [seed]

    # Generate the sequence of n random numbers
    for _ in range(n - 1):
        next_num = (multiplier * random_numbers[-1] + increment) % modulo
        random_numbers.append(next_num)

    return random_numbers


# Parameters
seed = 27
multiplier = 17
increment = 43
modulo = 100
n = 10  # Length of the sequence

# Generate the sequence
random_sequence = linear_congruential_generator(seed, multiplier, increment, modulo, n)
print(random_sequence)
