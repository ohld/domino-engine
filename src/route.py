class Route(object):
    def __init__(self, bone):
        assert bone.a == bone.b  # start only from tuple
         
        self.start = None
        self.end = bone.a

        self.bones = [bone]

    def __str__(self):
        first_bone = self.bones[0]
        s = f"{first_bone.a}{first_bone.b}"
        prev_val = first_bone.b
        for b in self.bones[1:]:
            if b.a == prev_val:
                s += f"|{b.a}{b.b}"
                prev_val = b.b
            else:
                s += f"|{b.b}{b.a}"
                prev_val = b.a

        return s
            
        # top_row = "|".join([str(b.a) for b in self.bones])
        # bot_row = "|".join([str(b.b) for b in self.bones])
        # return f"""  {top_row}\n  {bot_row}"""
        # return f"Route [ends on {self.end}]"

    def __len__(self):
        return len(self.bones) - 1

    def put(self, bone):
        if bone.a != self.end and bone.b != self.end:
            raise ValueError(f"Can't Put this {bone} to this {self}.")

        self.bones.append(bone)
        
        self.start = self.end
        self.end = bone.a if bone.a != self.end else bone.b
