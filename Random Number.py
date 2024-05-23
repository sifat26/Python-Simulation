
import random, pandas as pd

# input data for dict
cols = ['Serial', 'Random Number']
values = []

#max length of the random number to generate
max = 100

#unique random number generation using loop
for i in range(0, max):
  values.append(random.uniform(0,1))

# creating an empty dictionary
my_dict = []

#updating dictionary with data
for sl in range(0, max):
    data = {cols[0]: sl, cols[1]: values[sl]}
    my_dict.append(data)

#transforming dictionary into dataframe
df = pd.DataFrame.from_dict(my_dict)

#publishing dataframe as a .csv
df.to_csv('my_500_random_number_between_0_1.csv', index=False)

new_df = pd.read_csv('my_500_random_number_between_0_1.csv')

new_df