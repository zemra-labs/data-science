import pandas as pd
import numpy as np
from sklearn.lda import LDA

## read files
train = pd.read_csv('data/spam_train.csv')
test = pd.read_csv('data/spam_test.csv')

x = np.array(train.iloc[:, 0:57])
y = np.ravel(train.iloc[:, -1])

## separate the predictors and response in the test data set
x2 = np.array(test.iloc[:, 0:57])
y2 = np.ravel(test.iloc[:, -1])



## fit the model using lda
lda_cls = LDA()
lda_cls.fit(x,y)
print("(1): lda accuracy")
print(lda_cls.score(x, y))

## predict output on test data set with lda
predict = lda_cls.predict(x2)
print("(2): lda test accuracy")
print(lda_cls.score(x2, y2))
