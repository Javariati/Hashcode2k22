import numpy as np

class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.free = -1

    def __str__(self):
        return self.name

    def set_free(self, day):
        self.free = day

    def get_skill(self, skill):
        if skill in self.skills:
            return self.skills[skill]
        else:
            return 0
