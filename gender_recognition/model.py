import logging
import argparse

import preprocessing

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class Model:
    def __init__(self):
        pass

    def model(self):

        datasetdict = preprocessing.ProcessDataset().process_dataset()

        X_train, X_test, y_train, y_test = train_test_split(datasetdict['features'], datasetdict['labels'], random_state=42)
        
        self.forest = RandomForestClassifier(n_estimators=5, random_state=42)

        self.forest.fit(X_train, y_train)

        print('Accuracy on training set: {:.3f} %'.format(self.forest.score(X_train, y_train)*100))
        print('Accuracy on test set: {:.3f} %'.format(self.forest.score(X_test, y_test)*100))

if __name__ == "__main__":
    m = Model().model()