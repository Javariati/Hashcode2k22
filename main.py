import glob
import math
import os
import sys

from utils.gigi import zippoh

if __name__ == "__main__":

    arr = ['a_an_example.in', 'b_better_start_small.in', 'c_collaboration.in', 'd_dense_schedule.in', 'e_exceptional_skills.in', 'f']

    # glob in the folder output and get the name of last folder
    last_folder = max(glob.glob(f"output/*"), key=os.path.getctime)
    folder = int(last_folder.split('/')[1]) + 1

    os.mkdir(f"output/{folder}")
    zippoh(f"output/{folder}")

    for element in arr:
        path = f"input/{element}"

        # Save a reference to the original standard output
        original_stdout = sys.stdout

        with open(f"output/{folder}/{element}.txt", "w+") as f:
            # Change the standard output to the file we created.
            sys.stdout = f

            print("ciao")

            sys.stdout = original_stdout  # Reset the standard output to its original value
