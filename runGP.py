import sys
from src.GP import *
import importlib.util

EX_DIR = "examples/"
MODULE_DIR = "fitness/"

DEFAULT = "example11C.txt"
DEFAULT_FITNESS = "fitness_def.py"

if __name__ == "__main__":
    fitness_module_path = MODULE_DIR + DEFAULT_FITNESS
    example_path = EX_DIR + DEFAULT
    if len(sys.argv) == 2:
        example_path = EX_DIR + sys.argv[1]
    elif len(sys.argv) == 3:
        example_path = EX_DIR + sys.argv[1]
        fitness_module_path = MODULE_DIR + sys.argv[2]
        DEFAULT_FITNESS = sys.argv[2]

    spec = importlib.util.spec_from_file_location(DEFAULT_FITNESS[:-3], fitness_module_path)
    other = spec.loader.load_module()
    gp = GP(fitness_function=other.fitness)
    gp.get_train_data(example_path)
    gp.create_random_population()
    gp.evolve()