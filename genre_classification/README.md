# Genre Classification
Using deep learning to classify the genre of a song.


## Approach

1. Getting a dataset of songs
2. For each song
	1. Create a spectogram
	2. Slice it up, for increase in data
	3. Make this labeled data, as a featured list
3. Use this data to train and test a multiclass classifier, probably, random forest.
4. Save the model
5. Predict for a song
	1. Create a spectogram and slice it up
	2. Test it using saved model for every slice
	3. Take an average, and vote with probability and accuracy.
6. Report the accuracy and work
