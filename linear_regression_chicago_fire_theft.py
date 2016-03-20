### your solution
import pandas as pd
import numpy as np
%pylab inline
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
ols = linear_model.LinearRegression()

# specify path of file
path = "./data/slr05.csv"
# read csv
data = pd.read_csv(path, skiprows=1, names=["fire","theft"])

predictor = data[['fire']]
response = data['theft']

# scatter plot predictor and response
plt.scatter(predictor, response, c='k')
plt.xlabel('Fire')
plt.ylabel('Theft')

# fit linear model
ols.fit(predictor, response)

# plot prediction line
plt.plot(predictor, ols.predict(predictor), lw=2)
plt.scatter(predictor,response,c='k')
plt.xlabel('Chicago fires per 1,000 homes')
plt.ylabel('Chicago theft per 1,000 homes')
plt.show()

# coefficient & intercept
print('Coefficient: %.3f' %ols.coef_)
print('Intercept: %.3f' %ols.intercept_)

# residual sum of squares
print("Rss: %.2f" %np.sum((response - ols.predict(predictor)) ** 2))

# r_2 - coefficient determination
print('R^2: %.3f' %ols.score(predictor, response))

print("Coefficient determination is very low, the line does not quite fit the data.")
