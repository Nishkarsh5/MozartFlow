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
- This is still in implementation phase, read [more](https://github.com/techcentaur/MozartFlow/tree/master/genre_classification) about it here.

## <a id="three"></a> Gender Recognition

## <a id="four"></a> Audio Separation


## Contributors
- [Nishkarsh Gangal](https://github.com/Nishkarsh5)
- [Techcentaur](https://github.com/techcentaur)

## Support
If you have any problem trying to understand the code, feel free to raise and issue or drop a mail [here](mailto:ankit03june@gmail.com).

## Contribution
Any better approach in efficiency, or accuracy, or majorly to complete the implementation remained is appreciated. Feel free to raise an issue and then make a pull request in continuation.