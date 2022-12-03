import sys

DIR = "examples/"
DEFAULT = "linear.txt"

if __name__ == "__main__":
    print("Tiny GP is running...")
    if len(sys.argv) == 1:  # no arguments
        file_name = DIR + DEFAULT
    elif len(sys.argv) > 1:
        file_name = DIR + sys.argv[1]
    f = open(file_name, "r")
    print(f.read())
