

from game.StoryElement.Story_Element import Question


class Start(object):
    def question(self):
        question_text = 'What is your name?'
        question_options = ['Enter your name:']
        return Question(question_text, question_options)

    def actions(self, response):
