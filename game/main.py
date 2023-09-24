from game import Game
from game.StoryElement.Story_Element import StoryElement


game = Game()

turn1 = StoryElement()
print(game)
game.takeTurn()