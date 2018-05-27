## Instrument Classification

Classifying musical instruments with supervised machine learning, using K-nearest neighbors algorithm.

## Usage
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

## Dataset

- Dataset used to train this classifier was collected from [London Philharmonic Orchestra Dataset](http://www.philharmonia.co.uk/explore/sound_samples).
- Each audio file records one note from one of the five instruments and has a length from 0.25 seconds to 6 seconds. In total, over 600 audio pieces were used to train the classifier, and the distribution of each class was roughly the same. 

**For copyright reasons, the original data is not included in this repository.** But it is free to download.

- Instruments available are `["banjo", "bass clarinet", "bassoon", "cello", "clarinet", "contrabassoon", "cor anglais", "double bass", "flute", "french horn":, "guitar", "mandolin", "oboe", "percussion", "saxophone", "trombone", "trumpet", "tuba", "viola", "violin"]`.

## Terminal Terminology
- ```[.]``` : Info
- ```[#]``` : Debug
- ```[*]``` : Status
- ```[!]``` : Warning
- ```[/!/]``` : Critical / Error

## Implementation Details

#### Processing Dataset Features
#### Extracting Features from Datset
#### Classification with Machine Learning

## Performance Details