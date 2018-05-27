import glob
import pyyaml
import librosa
import numpy as np


class Classify:
    def __init__(self):
        with open('../config.yml', 'r') as outfile:
            try:
                read_yml = yaml.load(outfile)
            except yaml.YAMLError as error:
                print(error)

        self.dataset_foldername = read_yml['_datasetFolderName']

    def trimming(self, files_pathlist):
        datalist = []

        for filepath in files_pathlist:
            DTFTarray, sampling_rate = librosa.load(filepath)

            begin_silence = self.get_silence(DTFTarray)
            end_silence = self.get_silence(np.flipud(DTFTarray))

            DTFTarray_trimmed = DTFTarray[begin_silence: (len(DTFTarray) - end_silence)]

            mfccs = librosa.feature.mfccs(y=DTFTarray_trimmed, sr=sampling_rate)
            average = np.mean(mfccs, axis=1)

            features = average.reshape(20)

            label = self.get_label(filepath)
            datalist.append([filepath, feature, label])

        return datalist

    @staticmethod
    def get_label(filename):
            if filename[9:12] is 'cel':
                return 1
            elif filename[9:12] is 'cla':
                return 2
            elif filename[9:12] is 'flu':
                return 3
            elif filename[9:12] is 'vio':
                return 4
            else:
                raise NameError

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
