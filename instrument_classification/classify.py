import json
import yaml
import glob
import click
import librosa
import logging
import numpy as np

logger = logging.getLogger()

class Classify:
    def __init__(self, loglevel):
        """reading config file and dataset names file, and instantiate logger"""

        logging.basicConfig(level=loglevel)

        with open('../_config.yml', 'r') as outfile:
            try:
                self.read_yml = yaml.load(outfile)

            except yaml.YAMLError as error:
                logger.error('[/!/] _config.yml file not found:', error)
        
        with open(self.read_yml['_dataset']+"/"+self.read_yml['_dataFolderNames']+".json", 'r') as outfile:
            try:
                self.dataset_names = json.load(outfile)

            except FileNotFoundError:
                logger.error('[/!/] dataset labels not found')

    def get_dataset(self):
        """create dataset with as [filepath, features, label], with initial trimming"""
        
        datalist = []

        files_pathlist = self.get_path()
        logger.info('[*] Iterating over instances of {} file paths ...'.format(str(len(files_pathlist))))
        
        with click.progressbar(range(len(files_pathlist))) as progressbar:    
            
            for progress in progressbar:
                filepath = files_pathlist[progress]

                DTFTarray, sampling_rate = librosa.load(filepath)

                begin_silence = self.get_silence(DTFTarray)
                end_silence = self.get_silence(np.flipud(DTFTarray))

                DTFTarray_trimmed = DTFTarray[begin_silence: (len(DTFTarray) - end_silence)]

                mfccs = librosa.feature.mfcc(y=DTFTarray_trimmed, sr=sampling_rate)
                average = np.mean(mfccs, axis=1)
                features = average.reshape(20)

                label = self.dataset_names[(filepath.split("/"))[-2]]
                
                datalist.append([filepath, features, label])

        logger.info('[*] Dataset created and featured ...')
        
        return datalist

    @staticmethod
    def get_silence(DTFTarray, threshold=0.001):
        """find the position till which audio is silent, default threshold=0.001"""

        trim = 0

        DTFTarray = DTFTarray / max(DTFTarray)
        DTFTarray = np.array(DTFTarray)

        for i in range(len(DTFTarray)):
            if DTFTarray[trim] < threshold:
                trim += 1

        return trim

    def get_path(self):
        """getting path of all data file with glob"""

        logger.warning('[!] Only .mp3 files are included in dataset')
        
        files = glob.glob('./' + self.read_yml['_dataset'] + '/*/*.mp3')
        np.random.shuffle(files)

        if len(files) == 0:
            logger.warning('[!] No data files found! Application most likely will terminate ...')
            logger.critical('[/!/] No path found for data files')
        
        return files