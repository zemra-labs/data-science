### your solution
### overfitting = true
from sklearn import linear_model
ols = linear_model.LinearRegression()
import pandas as pd
import numpy as np
%pylab inline
import matplotlib.pyplot as plt

# specify path of file
path = "./data/Auto.csv"
# read csv
data = pd.read_csv(path, skiprows=1, names=["mpg","horsepower"])

# assign appropriate columns
predictor = data[["horsepower"]].astype(int)
response = data["mpg"].astype(float)

# scatter plot predictor and response
plt.scatter(predictor, response, c='k')
plt.xlabel('Horsepower')
plt.ylabel('MPG')

# fit linear model
ols.fit(predictor, response)

# plot prediction line
plt.plot(predictor, ols.predict(predictor), lw=2)
plt.scatter(predictor,response,c='k')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.show()

# find coefficient and intercept
b_zero = ols.intercept_
b_one = ols.coef_


# calculate rss
rss = np.sum((response - ols.predict(predictor)) ** 2)
# np.mean((response - ols.predict(predictor)) ** 2)

# coefficient of determination r^2
r_2 = ols.score(predictor, response)

# model
model = "B0 " + "+ B1 x (horsepower)" + " + e"
print b_zero
actual_model = "39.935" + " + " + "-0.158"  + "*" + "horsepower " + "e"
# least squares rss
print "(a): %.3f" %b_one
print "Higher horsepower means lower mpg."
print "(b): %.2f" %r_2
print "Horsepower entails 60% of variance.  The line somewhat fits the data."
print "(c): MPG = " + model
print "(c): MPG = " , actual_model
print "(d): %.3f" %ols.predict(98)
print "(e): %.3f" %rss
