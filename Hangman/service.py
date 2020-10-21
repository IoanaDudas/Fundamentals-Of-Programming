from sentence import *


class Service:

    def __init__(self, sentence):
        self._sentence = sentence
        self._sen = self._sentence.getSentence()

    def addSentence(self, sen):
        '''
        - validates the sentence given by the user and if it is valid
            the function calls the setSentence function from the Sentence class
            which checks for duplicates and then saves it into the file
        input:
            sen - the sentence from the user
        output:
            None
        '''
        number = 0
        if sen == '' or sen == ' ':
            raise ValueError("There must be at least one word!")
        for letter in sen:
            if letter != ' ':
                number += 1
            else:
                if number < 3:
                    raise ValueError("One of the words has less than 3 letters!")
                else:
                    number = 0
        if number < 3:
            raise ValueError("One of the words has less than 3 letters!")
        self._sentence.setSentence(sen)
