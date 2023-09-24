from os import system, name
from time import sleep


class Interface():
    def __init__(self):
        self.active = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux
        else:
            _ = system('clear')

        





class StoryElement():
    def __init__(self, storyText, question, actions):
        self.storyText = storyText
        self.question = question
        self.actions = actions

    def playTurn(self):
        self.storyText.printStory()
        answer = self.question.askQuestion()
        print(answer)

