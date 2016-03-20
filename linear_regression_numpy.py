### your solution
### overfitting = true
import pandas as pd
import numpy as np
%pylab inline
import matplotlib.pyplot as plt

# specify path of file
path = "./data/Auto.csv"
# read csv
data = pd.read_csv(path, skiprows=1, names=["mpg","horsepower"])

# assign appropriate columns
predictor = data["horsepower"].astype(int)
response = data["mpg"].astype(float)


# scatter plot predictor and response
plt.scatter(predictor, response, c='k')
plt.xlabel('Horsepower')
plt.ylabel('MPG')

# fit linear model
pf = np.polyfit(predictor, response, 1)
# plot line
plt.plot(predictor, np.polyval(pf,predictor), lw=2)
plt.scatter(predictor,response,c='k')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.show()

# r_2
fit = pf[0] * predictor + pf[1]
residual = response - fit
sum_residual = sum(pow(residual,2))
total = len(response) * var(response)
r_2 = 1 - sum_residual/total


print("Coefficient: %.3f" %pf[0])
print("Determination| R^2: %.2f" %r_2)
print("Residual: %.2f" %sum_residual)
print("TSS: %.2f" %total)
