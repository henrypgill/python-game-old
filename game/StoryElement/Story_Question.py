

class QuestionOption(object):
    def __init__(self, text, number):
        self.text = text
        self.number = number
    
    def printOption(self):
        print(f'Option {self.number}: {self.text}')


class Question(object):
    def __init__(self, questionText, optionsText):
        self.text = questionText
        self.options = self.createOptions(optionsText)

    def createOptions(self, optionsStrings):
        i = 1
        for optionString in optionsStrings:
            QuestionOption(optionString, i)
            i += 1

    def askQuestion(self):
        print(self.text)
        for option in self.options:
            option.printOption()
        response = input(self.options)
        return response