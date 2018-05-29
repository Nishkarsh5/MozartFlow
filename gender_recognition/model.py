import begin
import logging
import argparse
import speech_recognition as sr
import preprocessing

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

logger = logging.getLogger()


class Model:
    def __init__(self, no_DTrees=5):
        self.DTrees = no_DTrees

    def model(self):
        logger.info('[*] Processing dataset ...')
        datasetdict = preprocessing.ProcessDataset().process_dataset()

        logger.info('[*] Preparing model for classification ...')
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(datasetdict['features'], datasetdict['labels'], random_state=42)
        self.forest = RandomForestClassifier(n_estimators=self.DTrees, random_state=42)
        logger.infor('[.] Model formed' )

    def train(self):


        self.forest.fit(self.X_train, self.y_train)

        self.accuracy = self.forest.score(self.X_test, self.y_test)*100
        logger.info('\n[*] Accuracy on training set: {:.3f} %'.format(self.forest.score(self.X_train, self.y_train)*100))
        logger.info('[*] Accuracy on test set: {:.3f} %\n'.format(accuracy))

    def predict(self, filepath):

        predict = self.forest.predict(Pfeatures)
        print('[*] Predicted gender:', predict, 'with accuracy {:.3f} %'.format(self.accuracy))

    def predictnow(self):
        recog = sr.Recognizer()
        
        logger.info('[!] Please speak for a few seconds now ...')
        logger.info('[.] In case you do know what to say, say this:')
        logger.info('[.] The only way to live in this unfree world is to be so absoutely free that your very existence is an act of rebellion.')

        with sr.Microphone() as source:
            audio = recog.listen(source)
        try:
            audiofile = recog.recognize_google(audio)
        except sr.UnknownValueError:
            logger.error('[/!/] Could not understand the audio!')
        except sr.RequestError as e:
            logger.error('[/!/] Could not request results: {0}'.format(e))


if __name__ == "__main__":
        
    logging.basicConfig(level=args.loglevel)

    m = Model().model()