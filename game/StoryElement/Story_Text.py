
class StoryText(object):
    def __init__(self, textList):
        self.textList = textList

    def printStory(self):
        for textLine in self.textList:
            print(textLine)