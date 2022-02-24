class Project:
    def __init__(self, name, duration, score, best_before, roles):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.people = []

    def add_people(self, people, day):
        for person in people:
            person.set_free(day+self.duration)
            self.people.append(person)

    def __str__(self):
        project = f'{self.name}\n'
        for person in self.people:
            project += f'{person.__str__()} '
        
        return project

    def should_we_do_it(self, days):
        return len(self.people) == 0 and days < self.best_before + self.score

