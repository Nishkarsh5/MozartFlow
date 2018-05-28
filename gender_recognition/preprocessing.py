import csv
import numpy as np


class ProcessDataset:
    def __init__(self):
        pass

    def process_dataset(self):
        datalist = []
        featurelist = []
        labels = []

        with open('./dataset/voice.csv', 'r') as csvfile:
            data = csv.reader(csvfile)

            for d in data:  
                datalist.append(d)

        for i in range(len(datalist[0])-1):
            featuremap = (map(lambda n: n[i], datalist))
            flist = list(featuremap)

            del flist[0]

            featurearray = np.array(flist)
            featurelist.append(featurearray)


        labels = list(map(lambda n: n[len(datalist[0])-1], datalist))
        del labels[0]
        labels = np.array(labels)

        features = np.transpose(np.array(featurelist))

        return {'features': features, 'labels': labels}

if __name__=="__main__":
    p = ProcessDataset().process_dataset()