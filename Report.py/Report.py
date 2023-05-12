import pandas as pd

# Read data stored in 'balance,txt into a  DataFrame
df = pd.read_csv('balance.txt', delim_whitespace=True)
print(df)

# Comparing the average income based on ethnicity
# You can use two methods, the first works on selecting a table based on ethnicity then finds the mean
# income_average = df[df.Ethnicity == 'African American']
# print(f"The average income of a African American is {income_average.Income.mean()}")  # mean = 47.682101

print("The average income of a African American is ", df[df.Ethnicity == 'African American'].loc[:, "Income"].mean())
print("The average income of a Caucasian is ", df[df.Ethnicity == 'Caucasian'].loc[:, "Income"].mean())
print("The average income of a Asian is ", df[df.Ethnicity == 'Asian'].loc[:, "Income"].mean())

# Comparing balance average between married or single people
print("\nThe average Balance of a Married person is ", df[df.Married == 'Yes'].loc[:, "Balance"].mean())
print("The average Balance of a Single person is ", df[df.Married == 'No'].loc[:, "Balance"].mean())
print("On Average single people have a higher balance @ 13.493509015134242")

# Highest income in our Dataset
print("\nThe Highest income in our dataset is ", df.loc[:, "Income"].max())
# Lowest income in our Dataset
print("The Lowest income in our dataset is ", df.loc[:, "Income"].min())

# The number of cards recorded in our dataset.
print("\nThe number of cards recorded in our dataset is ", df.loc[:, "Cards"].sum())

# Comparing how many males vs females we have information about
print("\nThe number of females recorded in our dataset is ", list(df['Gender']).count('Female'))
# print("\nThe number of males recorded in our dataset is ", list(df['Gender']).count('Male')) since this line does
# not want to print the correct number we will go a different route
# print(df.info()) # we will get there are 400 entries
males = int(400 - 207)
print(f"Number of males in the Dataset is {males}")
