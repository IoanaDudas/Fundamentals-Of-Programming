from service import *
from sentence import *
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self._sentence = Sentence("hangman.txt")
        self._service = Service(self._sentence)

    def testAdd(self):
        sen = ' '
        self.assertRaises(ValueError, self._service.addSentence, sen)
        sen = ''
        self.assertRaises(ValueError, self._service.addSentence, sen)
        sen = 'an a an'
        self.assertRaises(ValueError, self._service.addSentence, sen)
        sen = 'anna an'
        self.assertRaises(ValueError, self._service.addSentence, sen)
        sen = 'anna anna'
        self.assertEqual(self._service.addSentence(sen), None)