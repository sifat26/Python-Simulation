import matplotlib.pyplot as plt
from collections import Counter

# List of ages
ages = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5]

# Count the frequency of each age
age_counts = Counter(ages)

# Construct the frequency distribution table
print("Age  Frequency")
for age, count in age_counts.items():
    print(f"{age}    {count}")

# Plot the histogram
plt.bar(age_counts.keys(), age_counts.values(), color='blue', edgecolor='black')
plt.xlabel('Age in days')
plt.ylabel('Frequency')
plt.title('Age Distribution of Newborn Babies')
plt.xticks(list(age_counts.keys()))  # Ensure all ages are shown on x-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
