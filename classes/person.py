class Person:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def get_skill(self, name):
        return self.skill[name]

    def __str__(self):
        return self.name