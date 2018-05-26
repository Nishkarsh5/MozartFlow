import librosa
import argparse
import numpy as np
import librosa.display
import matplotlib.pyplot as plt


class WithLibrosa:
    def __init__(self, path):
        self.path = path

    def separate(self, plot=True, save=True):
        y, sr = librosa.load(path)

        self.spec_mag, self.spec_phase = librosa.magphase(librosa.stft(y))

        if plot:
            index = slice(*librosa.time_to_frames([30, 35], sr=sr))
            plt.figure(figsize=(12, 4))

            librosa.display.specshow(librosa.amplitude_to_db(spec_mag[: index], ref=np.max), y_axis='log', x_axis='time', sr=sr)
            
            plt.colorbar()
            plt.tight_layout()

        spec_filter = librosa.decompose.nn_filter(spec_mag, aggregate=np.median, metrix='cosine', width=int(librosa.time_to_frames(2, sr=sr)))

        spec_filter = np.minimum(spec_mag, spec_phase)

        margin_i, margin_v = 2, 10
        power = 2

        mask_i = librosa.util.softmask(spec_filter, margin_i*(spec_mag - spec_filter), power=power)
        mask_v = librosa.util.softmask(spec_filter, margin_v*(spec_mag - spec_filter), power=power)

        s_foreground = mask_v * spec_mag
        s_background = mask_i * spec_mag


        if plot:                    
            plt.figure(figsize=(12, 8))
            plt.subplot(3, 1, 1)
            librosa.display.specshow(librosa.amplitude_to_db(spec_mag[:, idx], ref=np.max),
                                     y_axis='log', sr=sr)
            plt.title('Full spectrum')
            plt.colorbar()

            plt.subplot(3, 1, 2)
            librosa.display.specshow(librosa.amplitude_to_db(s_background[:, idx], ref=np.max),
                                     y_axis='log', sr=sr)
            plt.title('Background')
            plt.colorbar()
            plt.subplot(3, 1, 3)
            librosa.display.specshow(librosa.amplitude_to_db(s_foreground[:, idx], ref=np.max),
                                     y_axis='log', x_axis='time', sr=sr)
            plt.title('Foreground')
            plt.colorbar()
            plt.tight_layout()
            plt.show()        

        if save:
            librosa.output.write_wav(self.path+'/Foreground.wav', y=librosa.amplitude_to_db(s_foreground[:, idx], ref=np.max), sr=sr)
            librosa.output.write_wav(self.path+'/Background.wav', y=librosa.amplitude_to_db(s_background[:, idx], ref=np.max), sr=sr)

        return True


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Audio Separation with Librosa')

    parser.add_argument('-P', '--path', help='Path to the audio file (.mp3/.wav)', required=True)
    parser.add_argument('-p', '--plot', help='Plot the spectrograms', default=True)
    parser.add_argument('-s', '--save', help='Save as individual files', default=True)

    args = parser.parse_args()

    WithLibrosa(args.path).separate(args.plot, args.save)



