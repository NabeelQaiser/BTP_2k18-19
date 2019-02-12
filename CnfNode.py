from MyNode import MyNode

class CnfNode(MyNode):


    def __init__(self, id, ctx=None):
        super().__init__(id, ctx)
        self.parentBranching = dict()       # format : {'ancestor branching node id': "whether this node lies in the true part or the false part of that ancestor branching node"}
        self.visited = False
        self.color = 'white'
        self.pre = 0
        self.post = 0
        self.antecedent = []
        self.consequent = []
        self.isAssertion = False

    def printPretty(self):
        super().printPretty()
        print("parent branching info : ", self.parentBranching)
        print("antecedent : ", self.antecedent)
        print("consequent : ", self.consequent)
