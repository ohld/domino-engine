import random

from .bone import Bone

class Deck(object):
    def __init__(self):
        self.bones = []

        for i in range(7):
            for j in range(7):
                if i <= j:
                    self.bones.append(Bone(i,j))

        random.shuffle(self.bones)

    def is_empty(self):
        return len(self.bones) == 0

    def __len__(self):
        return len(self.bones)

    def take(self):
        if self.is_empty():
            return None
        return self.bones.pop()
