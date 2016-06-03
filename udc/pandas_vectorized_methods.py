import pandas as pd

d = {'one': Series([1,2,3], index=['a','b','c']),
    'two': Series([1,2,3,4], index=['a','b','c','d'])}

df = DataFrame(d)

# to apply something to every column in the dataframe use map

print df.apply(numpy.mean)

# you can also use map to apply things to one or all columns

df['one'].map(lambda x: x>=1)

# this would apply it to all the columns

df.map(lambda x: x>=1)
