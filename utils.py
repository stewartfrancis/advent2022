import sys
import os


def read_input():
    file_name = os.path.basename(sys.argv[0])
    input_name = f'{os.path.splitext(file_name)[0]}.txt'
    with open(input_name) as f:
        return f.read().splitlines()
