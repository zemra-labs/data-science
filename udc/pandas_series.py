import pandas as pd

series = pd.Series(['stuff', 123, 4, 'more stuff'])

print series


food = pd.Series(['ice cream', 'burger', 'fries', 'shake', 'banana'],
index=['most fav', 'fav', 'super fav', 'favv','least fav'])

# print food
print food.index
print food.values

print food[2:4]
print food.iloc[2:4]
