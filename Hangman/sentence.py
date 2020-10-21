from random import *


class Sentence:

    def __init__(self, filename):
        self._filename = filename
        self._loadFile()
        self._sentence = ''

    def _loadFile(self):
        f = open(self._filename, 'r')
        lines = f.readlines()
        rnd = randint(0, len(lines)-1)
        self._sentence = lines[rnd]
        self._sentence = self._sentence.strip("\n")
        f.close()

    def _saveFile(self):
        f = open(self._filename, 'r')
        lines = f.readlines()
        f = open(self._filename, 'w')
        exist = False
        for line in lines:
            if line.strip("\n") == self._sentence:
                exist = True
            f.write(line)
        if exist is True:
            f.close()
            return
        f.write(self._sentence)
        f.write("\n")
        f.close()

    def getSentence(self):
        self._loadFile()
        return self._sentence

    def setSentence(self, value):
        self._sentence = value
        self._saveFile()
