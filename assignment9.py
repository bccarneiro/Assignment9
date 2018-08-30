import pandas as pd

# read the dataset
df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

# Delete unnamed columns
df.pop('Unnamed: 0')

# Show the distribution of male and female
df.Gender.value_counts()

# Show the top 5 most preferred names
df.Name.value_counts().sort_values(ascending=False).head()

# What is the median name occurence in the dataset?
df.groupby(['Name']).Count.sum().median()

# Distribution of male and female born count by states
df.groupby(['State','Gender']).Count.sum()
