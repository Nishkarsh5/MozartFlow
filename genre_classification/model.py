import app
import librosa
import random
import math
import csv
import glob
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


class Model:
	
	def get_data(self):
		data_list = []
		
		e = app.Edited()
		f = e.files()

		for i in f:
			e.cut(i)
			break
			e.trim(i)
			feature= e.feature()
			lab= e.label(i)
			data_list.append([i, feature, lab])
		return data_list

	def unpack(self, data):
		datadict= {'filenames': [], 'features': [], 'label': []}
		
		for n in data:

			datadict['filenames'].append(n[0])
			datadict['features'].append(n[1])
			datadict['label'].append(n[2])

		return datadict	

	def model(self):
		data= self.get_data()
		self.knn_model= KNeighborsClassifier(n_neighbors=5)
		self.train_n_test(data)

	def train_n_test(self, data):

		np.random.shuffle(data)
		datadict = self.unpack(data)

		X_train, X_test, Y_train, Y_test= train_test_split(datadict['features'], datadict['label'], random_state=50)

		self.knn_model.fit(X_train, Y_train)
		accuracy= self.knn_model.score(X_test, Y_test)
		print('Test set accuracy is {:.2f}'.format(accuracy*100))


if __name__=="__main__":
	o = Model()
	o.model()




