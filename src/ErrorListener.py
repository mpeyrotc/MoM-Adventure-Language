from antlr4.error.ErrorListener import ErrorListener


class MoMErrorListener(ErrorListener):
    def __init__(self):
        super(MoMErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        e
        raise Exception("Oh no! " + str(offendingSymbol) + " ++++++ " + msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!! " + str(dfa))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!!!")
