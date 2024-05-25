import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Given data
data = [67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49, 78, 77, 83, 47, 67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49]

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Number of bins
num_bins = 6

# Create bins and calculate observed frequencies
obs_freq, bin_edges = np.histogram(data, bins=num_bins)

# Calculate expected frequencies using normal distribution
bin_probs = [stats.norm.cdf(bin_edges[i+1], mean, std_dev) - stats.norm.cdf(bin_edges[i], mean, std_dev) for i in range(num_bins)]
exp_freq = np.array(bin_probs) * len(data)

# Calculate Chi-Square statistic
chi_square_stat = ((obs_freq - exp_freq) ** 2 / exp_freq).sum()

# Degrees of freedom
dof = num_bins - 1 - 2  # subtracting 2 for mean and std deviation

# Critical value from Chi-Square distribution table for 24% significance level
critical_value = stats.chi2.ppf(0.76, dof)

# Print results
print(f"Observed Frequencies: {obs_freq}")
print(f"Expected Frequencies: {exp_freq}")
print(f"Chi-Square Statistic: {chi_square_stat}")
print(f"Degrees of Freedom: {dof}")
print(f"Critical Value at 24% significance level: {critical_value}")

# Decision
if chi_square_stat < critical_value:
    print("Fail to reject the null hypothesis: Data fits normal distribution")
else:
    print("Reject the null hypothesis: Data does not fit normal distribution")
