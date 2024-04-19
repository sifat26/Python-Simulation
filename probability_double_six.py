def probability_double_six(num_rolls):

    prob_not_double_six = 1 - (1 / 36)


    prob_not_double_six_all_rolls = prob_not_double_six ** num_rolls



    prob_at_least_one_double_six = 1 - prob_not_double_six_all_rolls

    return prob_at_least_one_double_six


num_rolls = 24

probability = probability_double_six(num_rolls)
print(f"Probability of getting at least one double six in {num_rolls} rolls: {probability:.4f}")
