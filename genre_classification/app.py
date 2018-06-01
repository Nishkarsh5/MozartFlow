import librosa
import random
import math
import csv
import glob
import numpy as np

class Edited:

	def trim(self, file_pathlist):
		y, sr = librosa.load(file_pathlist)
		self.yt,index=librosa.effects.trim(y)

	def duration(self):
		length=len(i)/sr
		length=math.floor(length/10)
		r=random.randint(0, length-1)
		r=r*10
		self.yt=self.yt[r*sr:(r+1)*sr]
	
	def feature(self):
		mfccs = librosa.feature.mfcc(y=self.yt)
		average = np.mean(mfccs, axis=1)
		features = average.reshape(20)
		return features

	def files(self):
		files=glob.glob('.\dataset\*\*.mp3')
		return files

	def label(self,file_path):
		fp=file_path.split('\\')
		fdict={"Classical": 0, "Hip hop": 1, "Pop": 2, "Rock": 3}
		return fdict[fp[2]]





