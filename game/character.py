

from random import random


class Character():
    def __init__(self, _race, _game_class, _name):
        self._name = _name
        self._class = _game_class
        self._race = _race
        self._stats = Character_Statistics()
    
    def get_health(self):
        return self._stats.health.value
    def get_attack(self):
        return self._stats.attack.value
    def get_name(self):
        return self._name
    def get_class(self):
        return self._class
    

class Game_Class(object):
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __repr__(self) -> str:
        return f"{self.name}: {self.description}"
        

class Character_Statistics(object):
    def __init__(self) -> None:
        self.health = Statistic("health", random.randint(1, 10))
        self.attack = Statistic("attack", random.randint(1, 10))


class Statistic(object):
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"

    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"
    