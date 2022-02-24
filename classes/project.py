class Project:
    def __init__(self, name, duration, score, best_before, roles):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.people = []

    def add_people(self, people, day):
        for idx, person in enumerate(people):
            person.set_free(day+self.duration)
            self.people.append(person)

            role_name = self.roles[idx][0]
            skill_required = self.roles[idx][1]
            if skill_required >= person.get_skill(role_name):
                new_person_skill = person.get_skill(role_name)
                new_person_skill += 1
                person.skills[role_name] = new_person_skill

    def __str__(self):
        project = f'{self.name}\n'
        for person in self.people:
            project += f'{person.__str__()} '

        return project

    def should_we_do_it(self, days):
        return len(self.people) == 0 and days < self.best_before + self.score

