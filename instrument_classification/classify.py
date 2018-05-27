import glob
import pyyaml
import librosa
import numpy as np


class Classify:
    def __init__(self, loglevel):
        self.loglevel = loglevel

        with open('../_config.yml', 'r') as outfile:
            try:
                self.read_yml = yaml.load(outfile)

            except yaml.YAMLError as error:
                self.loglevel.error('[!] _config.yml file not found:', error)
        
        with open(self.read_yml['_dataset']/self.read_yml['_dataFolderNames']+".json", 'r') as outfile:
            try:
                self.dataset_names = json.load(outfile)

            except FileNotFoundError:
                self.loglevel.error('[!] dataset labels not found')


    def get_dataset(self):
        datalist = []

        files_pathlist = self.get_path()

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

        return datalist


    @staticmethod
    def get_silence(DTFTarray, threshold=0.001):
        trim = 0

        DTFTarray = DTFTarray / max(DTFTarray)
        DTFTarray = np.array(DTFTarray)

        for i in range(len(DTFTarray)):
            if DTFTarray[trim] < threshold:
                trim += 1

        return trim

    def get_path():
        files = glob.glob('./' + self.dataset_foldername + '/*/*.mp3')
        np.shuffle(files)

        return files
