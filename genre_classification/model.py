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
		data_list= []
		e=app.Edited()
		f=e.files(self)

		for i in f:
			e.trim(self, i)
			e.duration(self)
			feature= e.feature(self)
			lab= e.label(self,i)
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

		data= get_data(self)
		self.knn_model= KNeighborsClassifier(n_neighbors=5)
		self.train_n_test(data)

	def train_n_test(self, data):

		np.random.shuffle(data)
        datadict = self.unpack_data(data)	

        X_train, X_test, Y_train, Y_test= train_test_split(datadict['features'], datadict['label'], random_state=50)

        self.knn_model.fit(X_train, Y_train)
        accuracy= self.knn_model.score(X_test, Y_test)
        print('Test set accuracy is {:.2f}'.format(accuracy*100))

        