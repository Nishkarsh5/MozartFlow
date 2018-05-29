import librosa
import random
import math

class Edited:

	def trim(self, file_pathlist):
		for file in file_pathlist:
			y,sr=librosa.load(file)
			self.yt,index=librosa.effects.trim(y)

	def duration(self):		
		length=len(i)/sr
		length=math.floor(length/10)
		r=random.randint(0,length-1)
		r=r*10
		self.yt=self.yt[r*sr:(r+1)*sr]
	
	def feature(self):		
		mfccs = librosa.feature.mfcc(y=self.yt)
        average = np.mean(mfccs, axis=1)
        features = average.reshape(20)
			

