import classify

import logging
import argparse
import numpy as np

from collections import namedtuple
from sklearn.neighbors import KNeighborsClassifier


class Model:
    def __init__(self, knn, loglevel):
        self.knn = knn
        self.loglevel = loglevel

        with open('../config.yml', 'r') as outfile:
            try:
                self.read_yml = yaml.load(outfile)

            except yaml.YAMLError as error:
                self.loglevel.error('[!] _config.yml file not found:', error)
        
        with open(self.read_yml['_dataset']/self.read_yml['_dataFolderNames']+".json", 'r') as outfile:
            try:
                self.dataset_names = json.load(outfile)

            except FileNotFoundError:
                self.loglevel.error('[!] dataset labels not found')

    def model(self):
        self.KNN = KNeighborsClassifier(n_neightbors = self.knn)
        train_and_test(data)


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