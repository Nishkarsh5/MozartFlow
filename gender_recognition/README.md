# Gender Recognition by Voice and Speech Analysis

Recognizing gender using serveral machine learning algorithms.


## About Dataset
- This database was created to identify a voice as male or female, based upon acoustic properties of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from male and female speakers. The voice samples are pre-processed by acoustic analysis in R using the seewave and tuneR packages, with an analyzed frequency range of 0hz-280hz (human vocal range).


- The following acoustic properties of each voice are measured and included within the CSV:

	meanfreq: mean frequency (in kHz) <br>
	sd: standard deviation of frequency <br>
	median: median frequency (in kHz) <br>
	Q25: first quantile (in kHz) <br>
	Q75: third quantile (in kHz) <br>
	IQR: interquantile range (in kHz) <br>
	skew: skewness (see note in specprop description) <br>
	kurt: kurtosis (see note in specprop description) <br>
	sp.ent: spectral entropy <br>
	sfm: spectral flatness <br>
	mode: mode frequency <br>
	centroid: frequency centroid (see specprop) <br>
	peakf: peak frequency (frequency with highest energy) <br>
	meanfun: average of fundamental frequency measured across acoustic signal <br>
	minfun: minimum fundamental frequency measured across acoustic signal <br>
	maxfun: maximum fundamental frequency measured across acoustic signal <br>
	meandom: average of dominant frequency measured across acoustic signal <br>
	mindom: minimum of dominant frequency measured across acoustic signal <br>
	maxdom: maximum of dominant frequency measured across acoustic signal <br>
	dfrange: range of dominant frequency measured across acoustic signal <br>
	modindx: modulation index. Calculated as the accumulated absolute difference between adjacent measurements of fundamental frequencies divided by the frequency range <br>
	label: male or female <br>


## Thanks to

[Kory Becker](https://www.kaggle.com/primaryobjects/voicegender) for this labeled dataset, I found on kaggle.