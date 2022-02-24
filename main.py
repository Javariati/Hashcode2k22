import glob
import math
import os
import sys
import time

from utils.gigi import zippoh
from utils.load_csv import import_csv

if __name__ == "__main__":

    arr = ['a_an_example.in', 'b_better_start_small.in', 'c_collaboration.in', 'd_dense_schedule.in', 'e_exceptional_skills.in', 'f']
    #arr = ['b_better_start_small.in']
    # glob in the folder output and get the name of last folder
    last_folder = max(glob.glob(f"output/*"), key=os.path.getctime)
    folder = int(last_folder.split('/')[1]) + 1

    os.mkdir(f"output/{folder}")
    zippoh(f"output/{folder}")

    for element in arr:

        start_time = time.time()
        start_time_f = time.strftime("%H:%M:%S")
        print(f"{start_time_f} Stampo il file: ", element)

        path = f"input/{element}"

        contributors, projects, max_time = import_csv(path)

        project_list = []
        day = 0

        for day in range(max_time):

            for project in projects:

                failed = False

                if project.should_we_do_it(day):
                    roles = project.roles.keys()
                    roles_assigned = []

                    free_people = [person for person in contributors if person.free < day]

                    for role in roles:
                        skill_value = project.roles[role]

                        for person in roles_assigned:
                            if person.get_skill(role) >= skill_value:
                                skill_value -= 1
                                break

                        skilled_free_people = [person for person in free_people if person.get_skill(role) >= skill_value and person not in roles_assigned]

                        if len(skilled_free_people) == 0:
                            failed = True
                            break
                        else:
                            skilled_free_people.sort(key=lambda x: x.get_skill(role))
                            roles_assigned.append(skilled_free_people[0])

                    if not failed:
                        project_list.append(project)
                        project.add_people(roles_assigned, day)

        end_time = time.time()
        end_time_f = time.strftime("%H:%M:%S")
        print(f"{end_time_f} Conclusa la stampa del file: ", element)

        print(f"Durata: {end_time - start_time}", element)

        # Save a reference to the original standard output
        original_stdout = sys.stdout

        with open(f"output/{folder}/{element}.txt", "w+") as f:
            # Change the standard output to the file we created.
            sys.stdout = f

            print(f'{len(project_list)}')

            for project in project_list:
                print(project.__str__())

            sys.stdout = original_stdout  # Reset the standard output to its original value
