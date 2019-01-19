from subprocess import call

class MyCFG():

    def __init__(self):
        self.nodes = dict()
        self.dotGraph = ""

    def addNode(self, node):
        self.nodes[node.id] = node

    def connect(self, a, b):
        self.nodes[a].addChild(b)
        self.nodes[b].setParent(a)

    def printPretty(self):
        for nodeId in self.nodes:
            print(nodeId, " --> ", end='')
            for i in self.nodes[nodeId].next:
                print(i, "\t", end='')
            print("parents : ", end='')
            for i in self.nodes[nodeId].parent:
                print(i, "\t", end='')
            print("")


    def dotToPng(self, dotString, filename):
        file = open(filename, 'w')
        file.write(dotString)
        file.close()

        call(["dot", "-Tpng", "-o", filename + ".png", filename])
        call(["eog", filename + ".png"])