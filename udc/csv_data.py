baseball_data = pandas.read_csv('Master.csv')

# this pandas function will read the csv file master.csv and return
# a pandas dataframe

# to print the first name column in the csv
print baseball_data['name First']

# to add additional column to the dataframe
# for example sum of height and weight into a new column known as
# height_and_weight

baseball_data['height_and_weight'] = baseball_data['height'] + baseball_data['weight']

# write back to csv
baseball_date.to_csv('somefile.csv')
