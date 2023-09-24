


from game.StoryElement.Story_Element import Question


class Player_Character(object):
    
    def create_character(self):
        self._name = input('What is your name?')
        self.__class = Question()('choose a class', ['warrior', 'mage', 'rogue'])