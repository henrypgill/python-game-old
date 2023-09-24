from ast import Num


class Story_Action(object):
    def __init__(self, player_input, actions):
        self._player_input = player_input
        self._actions = actions
    
    def playTurn(self):
        for action in self._actions:
            if action.number == self._player_input:
                action._action.playTurn()
                break



class ActionsOption(object):
    def __init__(self, case_number) -> None:
        self._number = case_number

    def get_number(self):
        return self._number