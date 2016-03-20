import pandas as pd
import numpy as np
from sklearn import linear_model
logit_1 = linear_model.LogisticRegression()
logit_1.set_params(C=1e4)
train = pd.read_csv('data/spam_train.csv')
test = pd.read_csv('data/spam_test.csv')
## separate the predictors and response in the training data set
x = np.array(train.iloc[:, 0:57])
y = np.ravel(train.iloc[:, -1])

## separate the predictors and response in the test data set
x2 = np.array(test.iloc[:, 0:57])
y2 = np.ravel(test.iloc[:, -1])

## fit the model using logistic regression
logit_1.fit(x, y)
print("(1): logistic regression accuracy")
print(logit_1.score(x, y))

## predict output on test data set with logistic regression
predict = logit_1.predict(x2)
print("(2): logistic regression test accuracy")
print(logit_1.score(x2, y2))
