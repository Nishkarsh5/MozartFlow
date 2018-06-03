# MozartFlow
Using Machine Learning to Study Music.

## Table of Contents
1. [Musical Instrument Classifier](#one)
2. [Genre Classification](#two)
3. [Gender Recognition](#three)
4. [Audio Separation](#four)

## <a id="one"></a> Musical Instrument Classifier


Classifying musical instruments with supervised machine learning, using K-nearest neighbors algorithm.

### Usage
- Install dependencies as `pip3 install -r requirements.txt`

#### Argparse Usage

```console
gavy42@jarvis:~/MozartFlow/instrument_classification$ python3 model.py -h
usage: model.py [-h] [-k KNN] [-ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                [-p PATH]

MozartFlow: Observing the flow of music.

optional arguments:
  -h, --help            show this help message and exit
  -k KNN, --knn KNN     K in K-nearest neighbours algorithm
  -ll {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
  -p PATH, --path PATH  Filepath of the audio file, need to be labeled
gavy42@jarvis:~/MozartFlow/instrument_classification$ 
```

### Dataset

- Dataset used to train this classifier was collected from [London Philharmonic Orchestra Dataset](http://www.philharmonia.co.uk/explore/sound_samples).
- Each audio file records one note from one of the five instruments and has a length from 0.25 seconds to 6 seconds. In total, over 600 audio pieces were used to train the classifier, and the distribution of each class was roughly the same. 

**For copyright reasons, the original data is not included in this repository.** But it is free to download.

- Instruments available are `["banjo", "bass clarinet", "bassoon", "cello", "clarinet", "contrabassoon", "cor anglais", "double bass", "flute", "french horn":, "guitar", "mandolin", "oboe", "percussion", "saxophone", "trombone", "trumpet", "tuba", "viola", "violin"]`.

### Implementation Details

#### Processing Dataset Features
The music pieces have their leading and ending silence trimmed. The threshold of trimming is 0.001 - if the intensity of the sound in the frame is below 0.1% of the highest sound intensity in the audio file, then the frame is trimmed out.


#### Extracting Features from Datset
The Mel Frequency Cepstral Coefficents (MFCCs) of each music piece was extracted using Librosa. For each audio file, its MFCCs are averaged to produce the final, length-20 feature vector.


#### Classification with Machine Learning
K-nearest neighbors algorithm is used to train the classifier. And then predict the output of any given audio file.


### Terminal-Output Terminology
- ```[.]``` : Info
- ```[#]``` : Debug
- ```[*]``` : Status
- ```[!]``` : Warning
- ```[/!/]``` : Critical / Error

## <a id="two"></a> Genre Classification
- This is still in implementation phase, read more about it [here](https://github.com/techcentaur/MozartFlow/tree/master/genre_classification).

## <a id="three"></a> Gender Recognition
Recognizing gender using serveral machine learning algorithms.

### Performance
```console
[*] Accuracy on training set: 99.579 %
[*] Accuracy on test set: 98.106 %
```

### Usage

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
gavy42@jarvis:~/MozartFlow/gender_recognition$
``` 

### About Dataset
- This database was created to identify a voice as male or female, based upon acoustic properties of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from male and female speakers. The voice samples are pre-processed by acoustic analysis in R using the seewave and tuneR packages, with an analyzed frequency range of 0hz-280hz (human vocal range).

### Thanks to

[Kory Becker](https://www.kaggle.com/primaryobjects/voicegender) for this labeled dataset which I found on kaggle.

## <a id="four"></a> Audio Separation

### With-Librosa
Usage of the file `with_librosa.py`

```console
gavy42@jarvis:~/MozartFlow/audio_separation$ python3 with_librosa.py -h
usage: with_librosa.py [-h] -P PATH [-p PLOT] [-s SAVE]

Audio Separation with Librosa

optional arguments:
  -h, --help            show this help message and exit
  -P PATH, --path PATH  Path to the audio file (.mp3/.wav)
  -p PLOT, --plot PLOT  Plot the spectrograms
  -s SAVE, --save SAVE  Save as individual files
gavy42@jarvis:~/MozartFlow/audio_separation$
```

## Contributors
- [Nishkarsh Gangal](https://github.com/Nishkarsh5)
- [Techcentaur](https://github.com/techcentaur)

## Support
If you have any problem trying to understand the code, feel free to raise and issue or drop a mail [here](mailto:ankit03june@gmail.com).

## Contribution
Any better approach in efficiency, or accuracy, or majorly to complete the implementation remained is appreciated. Feel free to raise an issue and then make a pull request in continuation.