import argparse
import numpy
import os
import math

def cube(n: int) -> int:
    cube_sum = 0
    i = 1
    while i < n+1:
        cur_cube = i**3 
        cur_cube_copy = cur_cube
        first_digit = cur_cube_copy
        while (cur_cube_copy > 9):
            cur_cube_copy = int(cur_cube_copy/10)
            first_digit = int(cur_cube_copy%10)
        if (first_digit%2 == 0):
            cube_sum = cube_sum + cur_cube
        i += 1
    return cube_sum

def main(number: int) -> int:
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the 
    # terminal output of the example given on the instructions.

    result = cube(number)

    print("cube(%d) = %d" % (number, result))

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)