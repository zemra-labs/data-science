import pandas as pd
import matplotlib.pyplot as plt

names2014 = pd.read_csv("names/yob2014.txt",names=["name","sex","birth"])

# names refers to column names
# print(names2014.head(10))
# returns pd dataframe 


def totalBirths(names):
	print names.sum()
	# built in sum

def totalBirthBySex(names):
	print names.groupby('sex').sum()
	# built in groupby

# totalBirths(names2014)
# totalBirthBySex(names2014)

years = range(1880, 2015)
data = []
columns = ["name","sex","birth"]

for year in years:
	path = "names/yob%d.txt" % year
	ingest_data = pd.read_csv(path, names=columns)

	ingest_data['year'] = year
	# create a new 'year' column to store data for each year
	data.append(ingest_data)


all_names = pd.concat(data, ignore_index=True)
# built in dataframe concat 


all_births = all_names.pivot_table('birth', columns='year', aggfunc=sum)
# built in dataframe - pivot_table

# built in dataframe - plot

def plot(data):
	data.plot(kind="line")
	plt.show(block=True)

plot(all_births)
# all_births.tail() 
# opposite of head()