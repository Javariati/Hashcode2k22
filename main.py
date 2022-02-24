import math
import sys


if __name__ == "__main__":

    arr = ['a', 'b', 'c', 'd', 'e', 'f']

    for element in arr:
        path = 'input/${element}.txt '

        # Save a reference to the original standard output
        original_stdout = sys.stdout

        with open('output/' + element, 'w') as f:
            # Change the standard output to the file we created.
            sys.stdout = f

            print(n_antenna)

            for idx, antenna in enumerate(antenna_list):
                if antenna.x != -1:
                    print(antenna)

            sys.stdout = original_stdout  # Reset the standard output to its original value

        # print(antenna_list)
