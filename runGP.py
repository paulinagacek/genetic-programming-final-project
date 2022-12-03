import sys
from src.GP import *

DIR = "examples/"
DEFAULT = "linear.txt"

if __name__ == "__main__":
    print("Tiny GP is running...")
    if len(sys.argv) == 1:  # no arguments
        file_name = DIR + DEFAULT
    elif len(sys.argv) > 1:
        file_name = DIR + sys.argv[1]
    f = open(file_name, "r")
    inputs_nr, outputs_nr = f.readline().split()
    inputs_nr, outputs_nr = int(inputs_nr), int(outputs_nr)

    inputs, outputs = [], []
    line = f.readline()
    while line:
        args = line.split()
        inp, outp = args[:inputs_nr], args[inputs_nr:]
        inputs.append(inp)
        outputs.append(outp)
        line = f.readline()
    print(inputs)
    print(outputs)

    gp = GP(inputs, outputs)