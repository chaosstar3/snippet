[[version manager#python]]

#optparse
```python
# https://docs.python.org/ko/3.13/library/optparse.html
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-o', '--output')
    parser.add_option('-v', dest='verbose', action='store_true')
    opts, args = parser.parse_args()
    process(args, output=opts.output, verbose=opts.verbose)

import sys
#sys.argv[1]

```
## jupyter
#cheatsheet
```python
import math
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

## pandas
```python
import pandas as pd

csv_path = os.path.join(dir, file)
df = pd.read_csv(csv_path)
 
# DATA
df.head()     # first n
df.info()     # 
df.describe() # count, mead, std, min

col = df[column]
col.value_counts() # group by count

# PLOT
df.hist(bins=50, figsize=(20,15)) # need backend
df.plot(kind="scatter", x="longitude", y="latitude")

# data
pd.cut()

# feature
df.corr() # correlation (linear)

# processing
df.dropna()
df.drop()
df.fillna()



```
## matplotlib

```python
import matplotlib.pyplot as plt
%matplotlib inline # jupyter notebook

def f(x):
    return x

xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)

# df.hist(bins=50, figsize=(20,15))
plt.show()
# save to image
plt.savefig(path, format="png", dpi=300);
plt.legend()

```

## sklearn

설계 철학
- 일관성: estimator, transformer, predictor
- 검사 가능
- 클래스 남용 방시
- 조합성
- 합리적 기본값

transform: 변환
fit: 훈련
fit_transform

### testset
```python
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
```

```python
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
```

### pipeline

imputer: 빈값 채우기
커스텀 변환기: inherit TransformerMixin, impl fit_transform()
> from sklearn.base import BaseEstimator, TransformerMixin
> class CombinedAttributesAdder(BaseEstimator, TransformerMixin):

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])
```

### Model Training
```python 
model = Model(params)
model.fit(prepared, labels)

data = pipeline.transform(data)
model.predict(data)

# save
import joblib
joblib.dump(model, "mode.pkl")
model = joblib.load("model.pkl")
```
models
```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import SGDClassifier
```

### Model Verification
```python
from sklearn.model_selection import StratifiedKFold
skfolds = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
# for train_index, test_index in skfolds.split(X_train, y_train_5):

from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy") 
# = array([accuracy1, accuracy2, accuracy3])

from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)


from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
# cm = confusion_matrix(y_train_5, y_train_pred)
precision_score(y_train_5, y_train_pred) # = cm[1, 1] / (cm[0, 1] + cm[1, 1])
recall_score(y_train_5, y_train_pred)    # = cm[1, 1] / (cm[1, 0] + cm[1, 1])
f1_score(y_train_5, y_train_pred)        # = cm[1, 1] / (cm[1, 1] + (cm[1, 0] + cm[0, 1]) / 2)

from sklearn.metrics import precision_recall_curve, roc_curve
```

### Tuning


### linear regression

sklrean.preprocessing::PolynomialFeatures


## keras
> pip3 install -U tensorflow

```python
import tensorflow as tf
from tensorflow import keras
```

```python
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28,28]))
model.add(keras.layers.Dense(300, activation="relu"))
model.add(keras.layers.Dense(100, activation="relu"))
model.add(keras.layers.Dense(10, activation="softmax"))
# or
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])


model.compile(loss="sparse_categorical_crossentropy",
        optimizer="sgd", 
        metrics=["accuracy"])
# keras.losses.sparse_categorical_crossentropy
# keras.optimizers.SGD
# keras.metrics.sparse_categorical_accuracy

history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))

model.evaluate(X_test, y_test)
y_pred = np.argmax(model.predict(x_new), axis=-1)


```