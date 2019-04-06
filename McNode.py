from MyNode import MyNode

class McNode(MyNode):


    def __init__(self, id, ctx=None):
        super().__init__(id, ctx)
        self.booleans = dict()          #format { 1 : [True], 2 : [False / * / skip], b : [phi, first ternary, second ternary] ... }
        self.wpcString = dict()         #format  { 1 : "---corresponding to first predicate---", ......}


    def printPretty(self):
        super().printPretty()
        print("booleans", self.booleans)
        print("wpcString", self.wpcString)

