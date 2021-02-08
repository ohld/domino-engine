import random

from .hand import Hand

def get_random_name():
    NAMES = ["Anya", "Dan", "Prosolkin", "Dan's Papa", "Ivan Potylitcyn", "Lera Muravya", "Random dude"]
    return random.choice(NAMES)

class Player(object):
    def __init__(self, name: str=None):
        self.name = name or get_random_name()
        self.hand = Hand([])

    def __str__(self):
        return f"Player '{self.name}'"  # \n{self.hand}"

    def give(self, bone):
        self.hand.put(bone)

    def take(self, bone):
        self.hand.bones.remove(bone)

    def go(self, game_map):
        open_sides = game_map.get_available_sides()
        for bone in self.hand.bones:
            if bone.a in open_sides or bone.b in open_sides:
                return bone

        return None
        