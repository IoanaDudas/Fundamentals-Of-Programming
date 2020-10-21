from service import *
from sentence import *


class UI:

    def __init__(self):
        self._sentence = Sentence("hangman.txt")
        self._sen = self._sentence.getSentence()
        self._service = Service(self._sentence)

    def start(self):
        while True:
            print('1. Add a sentence')
            print('2. Start the game')
            print('3. Exit')
            try:
                try:
                    choice = int(input("-> "))
                except:
                    raise ValueError("Invalid option!")
                print('')
                if choice == 1:
                    self.addSentence()
                elif choice == 2:
                    self._sen = self._sentence.getSentence()
                    self.game()
                elif choice == 3:
                    break
                else:
                    raise ValueError("Invalid option!")
            except Exception as msg:
                print(msg, '\n')

    def addSentence(self):
        sen = input("Introduce a sentence, minimum 3 letters per word: ")
        try:
            self._service.addSentence(sen)
        except Exception as msg:
            print(msg, '\n')

    def game(self):
        letters = []
        letters.append(' ')
        letters.append(self._sen[0])
        letters.append(self._sen[-1])
        for each in range(len(self._sen)):
            if self._sen[each] == " ":
                letters.append(self._sen[each + 1])
                letters.append(self._sen[each - 1])
        string = ""
        missing = 0
        for each in range(len(self._sen)):
            if self._sen[each] not in letters:
                missing += 1
                string = string + "_"
            else:
                string = string + self._sen[each]
        print("Output: " + string)
        print()
        hang = "hangman"
        man = ""
        error = 0
        while missing > 0 and man != hang:
            guess = input("User guess: ")
            if guess in letters or guess not in self._sen:
                error += 1
                man = hang[0:error]
            else:
                newString = ""
                for each in range(len(self._sen)):
                    if guess == self._sen[each]:
                        missing -= 1
                        newString = newString + guess
                        letters.append(guess)
                    else:
                        newString = newString + string[each]
                string = newString
            print("Output: " + string)
            print("--> " + man)
            print()

        if missing == 0:
            print("Congrats! You won!")
            print()
        if man == hang:
            print("You lost! Try again!")
            print()
