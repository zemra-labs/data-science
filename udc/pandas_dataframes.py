import pandas as pd

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

football = pd.DataFrame(data)

# dataframe keys are columns
# use the keys to retreive values from DataFrame
# you can also use dot notation
print football['year']
print football.year

# to select more than one column from the dataframe you need
# to use list of lists notation, double brackets

print football[['year', 'wins', 'losses']]

# to access rows in a dataframe you can use slicing,iloc,loc
# or even boolean indexing

# the following will print the first row
print football.iloc[[0]]
print football.loc[[0]]

# slicing (not inclusive of the second number)
# will print rows 3,4
print football[3:5]

# boolean

print football[football.wins > 10]
print football[(football.wins > 10) & (football.team == "Packers")]
