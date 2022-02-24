import pandas as pd
from classes.person import Person
from classes.project import Project


def import_csv(filename):
    header = pd.read_csv(filename, header=None, nrows=1, sep=' ')
    header = header.to_numpy()

    n_contributors = header[0][0]
    n_projects = header[0][1]

    contributors = []
    projects = []

    line_read = 1

    for i in range(n_contributors):
        df = pd.read_csv(filename, header=None, skiprows=line_read, nrows=1, sep=' ')
        df = df.to_numpy()
        c_name = df[0][0]
        n_skills = df[0][1]

        line_read += 1

        skills = pd.read_csv(filename, header=None, skiprows=line_read, nrows=n_skills, sep=' ')
        skills = skills.to_numpy()

        line_read += n_skills

        dict_skills = {}
        for idx, skill in enumerate(skills):
            dict_skills[skill[0]] = skill[1]

        contributor = Person(c_name, dict_skills)
        contributors.append(contributor)

    max_time = 0

    for i in range(n_projects):
        df = pd.read_csv(filename, header=None, skiprows=line_read, nrows=1, sep=' ')
        df = df.to_numpy()
        p_name = df[0][0]
        p_duration = df[0][1]
        p_score = df[0][2]
        p_best_before = df[0][3]
        n_roles = df[0][4]

        p_time = p_best_before + p_score

        if p_time > max_time:
            max_time = p_time

        line_read += 1

        roles = pd.read_csv(filename, header=None, skiprows=line_read, nrows=n_roles, sep=' ')
        roles = roles.to_numpy()

        line_read += n_roles

        dict_roles = {}
        for idx, role in enumerate(roles):
            dict_roles[role[0]] = role[1]

        project = Project(p_name, p_duration, p_score, p_best_before, dict_roles)
        projects.append(project)



    return contributors, projects, max_time



if __name__ == "__main__":
    file = '../input/a_an_example.in'
    contributors, projects, max_time = import_csv(file)

    print(contributors)
    print("giac merda")
    print(projects)
    print(max_time)