import sys
from antlr.PPVisitor import *
from antlr.PPListener import *
from antlr.PPLexer import *
from antlr.PPParser import *
from antlr.PPErrorListener import *

def interprateInput(data):
    # lexer
    lexer = PPLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = PPParser(stream)
    # parser.addErrorListener(PPErrorListener())  # add error listener
    try:
        tree = parser.program()
    except Exception as e:
        print(e)
        return

    # evaluator
    visitor = PPVisitor()
    output = visitor.visit(tree)
    

DIR = "examples/"

if __name__ == "__main__":

    if len(sys.argv) == 1: # no arguments
        while True:
            data = InputStream(input(">>> "))
            interprateInput(data)
    elif len(sys.argv) > 1:
        file = DIR + sys.argv[1]
        data = FileStream(file, encoding='utf-8')
        interprateInput(data)
