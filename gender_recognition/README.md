# Gender Recognition by Voice and Speech Analysis
Recognizing gender using serveral machine learning algorithms.

## Performance
```console
[*] Accuracy on training set: 99.579 %
[*] Accuracy on test set: 98.106 %
```

## Usage

- Run `pip3 install -r requirements.txt` to install the dependencies.

#### Argparse Usage
```console
gavy42@jarvis:~/MozartFlow/gender_recognition$ python3 model.py -h
usage: model.py [-h] [-t TREES] [-p PREDICT] [-P]
                [-L {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Gender Voice Recognition

optional arguments:
  -h, --help            show this help message and exit
  -t TREES, --trees TREES
                        No of decision trees (default=5)
  -p PREDICT, --predict PREDICT
                        Give a filepath and get prediction
  -P, --predictnow      Start speaking and get prediction
  -L {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
```

### Running Script Help

- Run `python3 model.py` to simply train and test the model (using random forest algorithm with default 5 decision trees), the results will be like
```console
gavy42@jarvis:~/MozartFlow/gender_recognition$ python3 model.py
[*] Training over 3169 instances ...
  [####################################]  100%

----------Accuracy-----------

[*] Accuracy on training set: 99.579 %
[*] Accuracy on test set: 98.106 %
``` 

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

[Kory Becker](https://www.kaggle.com/primaryobjects/voicegender) for this labeled dataset which I found on kaggle.