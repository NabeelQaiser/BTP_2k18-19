
class WpcGenerator():

    def __init__(self, cfg):
        self.cfg = cfg

        self.totalNodeCount = -1


    def execute(self):
        self.totalNodeCount = len(self.cfg.nodes.keys())
        currentNodeId = self.totalNodeCount - 1
        self.runner(currentNodeId)


    def runner(self, currentNodeId):
        print(currentNodeId, end=" ")
        if len(self.cfg.nodes[currentNodeId].parent) < 1:
            return
        else:
            setOfParents = set(self.cfg.nodes[currentNodeId].parent)
            while len(setOfParents) >= 1:
                tempNodeId = setOfParents.pop()
                self.runner(tempNodeId)