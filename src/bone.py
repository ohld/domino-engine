

class Bone(object):
    def __init__(self, a: int, b: int):
        self.a = min(a, b)
        self.b = max(a, b)

    def __str__(self):
        # if self.a == self.b == 1:
        #     __name = "🀹"
        # elif self.a == self.b == 6:
        #     __name = "🁡"
        # else:
        __name = f"[{self.a}|{self.b}]"
        return f"Bone {__name}"

    def __eq__(self, b):
        return self.a == b.a and self.b == b.b  # always sorted

    def is_duble(self):
        return self.a == self.b