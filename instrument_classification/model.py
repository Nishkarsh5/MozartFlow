import logging
import argparse
import numpy as np
from collections import namedtuple
from sklearn.neighbors import KNeighborsClassifier

class Model:
    def __init__(self):
        with open('../config.yml', 'r') as outfile:
            try:
                self.read_yml = yaml.load(outfile)
            except yaml.YAMLError as error:
                print(error)
        with open(self.read_yml['_dataset']/self.read_yml['_dataFolderNames']+".json", 'r') as outfile:
            self.dataset_names = json.load(outfile)

    self.logger = logging.getLogger()


    def model(self, n_neightbors):
        # consider we have labeled data here, named, data

        self.KNN = KNeighborsClassifier(n_neightbors = n_neightbors)
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
    parser = argparse.ArgumentParser(description='MozartFlow: Observing the flow of music.')

    parser.add_argument('-k', '-knn', help='K in K-nearest neighbours algorithm', default=5)
    parser.add_argument('-ll', '-loglevel', help='Set the logging level', type=str, choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
