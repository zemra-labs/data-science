import numpy as np

# taking the dot product of two arrays or vectors

a = [1,2,3,4,5]
b = [2,3,4,5,6]

# 1*2 + 2*3 + 3*4 etc
# this can be done by using numpy.dot() for dot prod

print numpy.dot(a,b)

# multiplying arrays into matricies
# a = [1,2] b = [2 4 6]
#               3 5 7

# you can use numpy.dot for matrix multiplcation & dot notation
olympic_medal_counts = {'country_name' : Series(countries), 'gold': Series(gold),
                        'silver': Series(silver), 'bronze':Series(bronze)}

                        olympic_medal_counts_df = DataFrame(olympic_medal_counts)

medal_counts = olympic_medal_counts_df[['gold','silver','bronze']]
points = numpy.dot(medal_counts, [4,2,1])

olympics_points = {'country_name' : Series(countries), 'points': Series(points)}
olympics_points_df = DataFrame(olympics_points)
