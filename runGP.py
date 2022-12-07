import sys
from src.GP import *

DIR = "examples/"
# DEFAULT = "linear.txt"
DEFAULT = "example_1_2_A.txt"

if __name__ == "__main__":
    if len(sys.argv) == 1:  # no arguments
        file_name = DIR + DEFAULT
    elif len(sys.argv) > 1:
        file_name = DIR + sys.argv[1]
    gp = GP()
    gp.get_train_data(file_name)
    gp.create_random_population()
    gp.evolve(copy=True)