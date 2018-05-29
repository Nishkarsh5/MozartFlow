import begin
import logging
import argparse
import speech_recognition as sr
import preprocessing

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

logger = logging.getLogger()


class Model:
    def __init__(self, no_DTrees):
        self.DTrees = no_DTrees

    def model(self):
        logger.info('[*] Processing dataset ...\n')
        datasetdict = preprocessing.ProcessDataset().process_dataset()

        logger.info('[*] Preparing model for classification ...')
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(datasetdict['features'], datasetdict['labels'], random_state=42)
        self.forest = RandomForestClassifier(n_estimators=self.DTrees, random_state=42)
        logger.infor('[.] Model formed' )

        self.train()

    def train(self):

        self.forest.fit(self.X_train, self.y_train)

        logger.info('[.]-----------/-------------Accuracy-------------/-----------')
        self.accuracy = self.forest.score(self.X_test, self.y_test)*100
        logger.info('\n[*] Accuracy on training set: {:.3f} %'.format(self.forest.score(self.X_train, self.y_train)*100))
        logger.info('[*] Accuracy on test set: {:.3f} %\n'.format(accuracy))

        return True

    def predict(self, filepath):

        Pfeatures = self.get_audiofeatures(filepath)

        predict = self.forest.predict(Pfeatures)
        print('[*] Predicted gender:', predict, 'with accuracy {:.3f} %'.format(self.accuracy))

        return True

    def predictnow(self):
        recog = sr.Recognizer()
        
        logger.info('[!] Please speak for a few seconds now ...\n')
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

        return True

    def get_audiofeatures(self, filepath):

        Pfeatures = []

        return Pfeatures

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Gender Voice Recognition')

    parser.add_argument('-t', '--trees', help='No of decision trees (default=5)', default=5)
    parser.add_argument('-p', '--predict', help='Give a filepath and get prediction', type=str, default='')
    parser.add_argument('-P', '--predictnow', help='Start speaking and get prediction', default=False, action="store_true")
    parser.add_argument('-L', '--log', help='Set the logging level', type=str, choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
        
    args = parser.parse_args()
    logging.basicConfig(level=args.log)

    mod = Model(args.trees)

    if args.predictnow:
        mod.predictnow()
    elif args.predict is not '':
        mod.predict(args.predict)

        

