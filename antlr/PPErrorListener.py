from antlr4.error.ErrorListener import ErrorListener

class PPErrorListener(ErrorListener):

    def __init__(self):
        super(PPErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error at line " + str(line) + ":" + str(column) + ": " + msg)

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     raise Exception("Ambiguity error at line " + str(startIndex) + ":" + str(stopIndex) + ": " + str(ambigAlts))
    #
    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise Exception("Full context error at line " + str(startIndex) + ":" + str(stopIndex) + ": " + str(conflictingAlts))
    #
    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     raise Exception("Context sensitivity error at line " + str(startIndex) + ":" + str(stopIndex) + ": " + str(prediction))