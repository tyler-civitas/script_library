'''
Scores any model given a model class and data

Originally writte by Shawn Terryah
'''

import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, average_precision_score, recall_score

def KFolds_any_model(X_train, y_train, k, model_to_fit):
    ''' k = number of folds. Returns mean accuracy, precision,
    and recall of any model (kNN(), LogisticRegression(),
    LinearRegression, etc...'''
    index = 0
    kf = KFold(n_splits = k)
    accuracy = np.empty(k)
    precision = np.empty(k)
    recall = np.empty(k)
    model = model_to_fit
    for train, test in kf.split(X_train, y_train):
        model.fit(X_train[train], y_train[train])
        pred = model.predict(X_train[test])
        accuracy[index] = accuracy_score(y_train[test], pred)
        precision[index] = average_precision_score(y_train[test], pred)
        recall[index] = recall_score(y_train[test], pred)
        index += 1
    return 'accuracy: {}, precision: {}, recall: {}'.format(round(accuracy.mean(), 3),
                round(precision.mean(), 3), round(recall.mean(), 3))
