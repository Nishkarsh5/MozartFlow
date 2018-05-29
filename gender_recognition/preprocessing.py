import csv
import click
import logging
import numpy as np

logger = logging.getLogger()

class ProcessDataset:
    def __init__(self, log):
        """Initalizses logging basic config"""

        logging.basicConfig(level=log)

    def process_dataset(self):
        """Start processing dataset from csv file"""

        datalist = []
        featurelist = []
        labels = []

        try:
            with open('./dataset/voice.csv', 'r') as csvfile:
                data = csv.reader(csvfile)

                for d in data:  
                    datalist.append(d)
        except FileNotFoundError:
            logger.error('[/!/] CSV file not found! Couldn\'t process dataset. Duh!!')

        print('[*] Training over {} instances ...'.format(len(datalist)))

        with click.progressbar(range(len(datalist[0])-1)) as progressbar:    
            for progress in progressbar:
                featuremap = (map(lambda n: n[progress], datalist))
                flist = list(featuremap)

                del flist[0]

                featurearray = np.array(flist)
                featurelist.append(featurearray)

        labels = list(map(lambda n: n[len(datalist[0])-1], datalist))
        del labels[0]
        labels = np.array(labels)

        features = np.transpose(np.array(featurelist))

        logger.info('[.] Dataset created; featured and labeled ')
        logger.debug('[!] Dictionary returned as {\'features\': features, \'labels\': labels}')

        return {'features': features, 'labels': labels}

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Processing dataset for gender voice recognition')
    parser.add_argument('-L', '--log', help='Set the logging level', type=str, choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
        
    args = parser.parse_args()
    logging.basicConfig(level=args.log)

    p = ProcessDataset(args.log).process_dataset()