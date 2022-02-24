class Project:
    def __init__(self, name, duration, score, best_before, roles):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __str__(self):
        project = 'self.name\n'
        for person in self.people:
            project += f'{person.__str__()} '
        
        return project


