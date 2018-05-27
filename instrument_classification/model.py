import logging
import argparse
import numpy as np

import classify

from collections import namedtuple
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

class Model:
    def __init__(self, knn, loglevel):
        self.knn = knn
        self.loglevel = loglevel

        with open('../_config.yml', 'r') as outfile:
            try:
                self.read_yml = yaml.load(outfile)

            except yaml.YAMLError as error:
                self.loglevel.error('[/!/] _config.yml file not found:', error)
        
        with open(self.read_yml['_dataset']/self.read_yml['_dataFolderNames']+".json", 'r') as outfile:
            try:
                self.dataset_names = json.load(outfile)

            except FileNotFoundError:
                self.loglevel.error('[/!/] dataset labels not found')

    def model(self):
        self.loglevel.info('[*] Starting processing of dataset ...')
        cl = classify.Classify(self.loglevel)
        data = cl.get_dataset()

        self.KNN = KNeighborsClassifier(n_neightbors = self.knn)
        train_and_test(data)

        return True


    def train_and_test(self, data):
        np.random.shuffle(data)
        datatuple = unpack_data(data)

        self.loglevel('[*] 75-25 partition of datasets ...')
        train_features, test_features, train_labels, test_labels = train_test_split(datatuple.features, datatuple.labels, random_state=0)
        self.loglevel.info('[*] Training started with 75% dataset ...')

        self.KNN.fit(train_features, train_labels)

        self.loglevel.info('[*] Testing started with 25% dataset ...')
        print('/---------------Accuracy------------/') 
        
        accuracy = self.KNN.score(train_features, train_labels)
        print('Test set accuracy','{:.2f}'.format(accuracy*100), '%')

        return True


    def train(self, data):
        datatuple = unpack_data(data)
        self.KNN.fit(datatuple.features, datatuple.labels)


    def test(self, data):
        datatuple = unpack_data(data)
        predicted = self.KNN.predict(datatuple.features)
        print('accuracy:', self.KNN.score(datatuple.features, datatuple.labels))


    def unpack_data(self, data):        
        filenames = np.array(map(lambda n: n[0], data))
        features = np.array(map(lambda n: n[1], data))
        labels = np.array(map(lambda n: n[0], data))

        Tup = namedtuple('Tup', 'filenames features labels')
        return Tup(filenames = filenames, features = features, labels = labels)


def main():
    self.logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='MozartFlow: Observing the flow of music.')

    parser.add_argument('-k', '-knn', help='K in K-nearest neighbours algorithm', default=5)
    parser.add_argument('-ll', '-loglevel', help='Set the logging level', type=str, choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    model = Model(args.knn, args.loglevel)

    print('----/---- Created by ----/----')
    for creator in model.read_yml['creator']:
        print('Lord', creator)

if __name__=="__main__":
    main()
