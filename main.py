import math
import sys


if __name__ == "__main__":

    #arr = ['a', 'b', 'c', 'd', 'e', 'f']
    arr = ['a']

    for element in arr:
        path = f"input/{element}.txt"

        # Save a reference to the original standard output
        original_stdout = sys.stdout

        with open(f"output/{element}.txt") as f:
            # Change the standard output to the file we created.
            sys.stdout = f

            print("ciao")

            sys.stdout = original_stdout  # Reset the standard output to its original value
