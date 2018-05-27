import glob
import pyyaml
import librosa
import numpy as np


class Classify:
    def __init__(self, loglevel):
        """reading config file and dataset names file, and instantiate self.loglevel"""

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


    def get_dataset(self):
        """create dataset with as [filepath, features, label], with initial trimming"""
        
        datalist = []

        files_pathlist = self.get_path()
        self.loglevel.info('[*] Iterating over instances of', str(len(files_pathlist)), 'file paths ...')
        
        for filepath in files_pathlist:
            DTFTarray, sampling_rate = librosa.load(filepath)

            begin_silence = self.get_silence(DTFTarray)
            end_silence = self.get_silence(np.flipud(DTFTarray))

            DTFTarray_trimmed = DTFTarray[begin_silence: (len(DTFTarray) - end_silence)]

            mfccs = librosa.feature.mfccs(y=DTFTarray_trimmed, sr=sampling_rate)
            average = np.mean(mfccs, axis=1)
            features = average.reshape(20)

            label = self.dataset_names[(filename[9:12])]
            
            datalist.append([filepath, feature, label])

        self.loglevel.info('[*] Dataset created and featured ...')
        
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

        self.loglevel.warning('[!] Only .mp3 files are included in dataset')
        
        files = glob.glob('./' + self.dataset_foldername + '/*/*.mp3')
        np.shuffle(files)

        if len(files) == 0:
            self.loglevel.warning('[!] No data files found! Application most likely will terminate ...')
            self.loglevel.critical('[/!/] No path found for data files')
        
        return files