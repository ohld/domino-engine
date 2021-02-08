from typing import List

from .bone import Bone

class Hand(object):
    def __init__(self, bones: List[Bone] = []):
        self.bones = bones

    def __len__(self):
        return len(self.bones)

    def __str__(self):
        top_row = "|".join([str(b.a) for b in self.bones])
        bot_row = "|".join([str(b.b) for b in self.bones])
        return f"""  {top_row}\n  {bot_row}"""

    def put(self, bone):
        self.bones.append(bone)

    def does_have(self, bone):
        return bone in self.bones