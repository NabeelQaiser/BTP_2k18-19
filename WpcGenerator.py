
class WpcGenerator():

    def __init__(self, cfg):
        self.cfg = cfg
        self.finalWpcString = ""
        self.totalNodeCount = -1
        self.cfgVisited = []


    def execute(self):
        self.totalNodeCount = len(self.cfg.nodes.keys())
        self.cfgVisited = [0] * self.totalNodeCount
        currentNodeId = self.totalNodeCount - 1
        # self.runner(currentNodeId)        # 1st approach
        self.goodAlgo(currentNodeId, "")    # 2nd approach




    ### 2nd approach... better complexity than 1st one

    def goodAlgo(self, currentNodeId, wpcString):
        if self.cfgVisited[currentNodeId] == 1:
            return

        currentNode = self.cfg.nodes[currentNodeId]
        if len(currentNode.next) > 1:       # it's a condition! Yo!!!
            listOfNext = list(currentNode.next)
            if self.cfgVisited[listOfNext[0]]==1 and self.cfgVisited[listOfNext[1]]==1:
                # Beware! first enrich wpcMakerHelper dict()
                self.enrich_wpcMakerHelper(currentNodeId, wpcString)
                # if len(currentNode.wpcMakerHelper) < 2:
                #     if currentNode.wpcMakerHelper.get('true') == None:
                #         self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
                #     elif currentNode.wpcMakerHelper.get('false') == None:
                #         self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString

                # merge true and false part
                print(listOfNext)
                print("-------", currentNode.wpcMakerHelper)
                wpcString = "( ( " + str(currentNodeId) + " ^ " + currentNode.wpcMakerHelper['true'] + " ) v ( !" + str(currentNodeId) + " ^ " + currentNode.wpcMakerHelper['false'] + " ) )"
            elif self.cfgVisited[listOfNext[0]]==1:
                print("first")
                self.addWpcString(currentNodeId, listOfNext[0], wpcString)
                # if currentNode.branching['true']==listOfNext[0]:
                #     self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString    # fool! don't just edit the copy!
                # elif currentNode.branching['false']==listOfNext[0]:
                #     self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
                return
            elif self.cfgVisited[listOfNext[1]]==1:
                print("second")
                self.addWpcString(currentNodeId, listOfNext[1], wpcString)
                # if currentNode.branching['true']==listOfNext[1]:
                #     self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
                # elif currentNode.branching['false']==listOfNext[1]:
                #     self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
                return

        self.cfgVisited[currentNodeId] = 1
        print(">>>", currentNodeId, "= 1")
        if len(currentNode.next) <= 1:      # avoid conditional node for wpcString
            wpcString = wpcString + "." + str(currentNodeId)

        #..........
        if len(currentNode.parent) < 1:
            self.finalWpcString = wpcString
            return
        elif len(currentNode.parent) == 1:
            parent = set(currentNode.parent)
            self.goodAlgo(parent.pop(), wpcString)
        elif len(currentNode.parent) > 1:
            setOfParents = set(currentNode.parent)
            while len(setOfParents) >= 1:
                tempNodeId = setOfParents.pop()
                self.goodAlgo(tempNodeId, wpcString)

    def addWpcString(self, currentNodeId, myVisitedChildId, wpcString):
        if self.cfg.nodes[currentNodeId].branching['true'] == myVisitedChildId:
            self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString    # fool! don't just edit the copy!
        elif self.cfg.nodes[currentNodeId].branching['false'] == myVisitedChildId:
            self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString

    def enrich_wpcMakerHelper(self, currentNodeId, wpcString):
        if len(self.cfg.nodes[currentNodeId].wpcMakerHelper) < 2:
            if self.cfg.nodes[currentNodeId].wpcMakerHelper.get('true') == None:
                self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
            elif self.cfg.nodes[currentNodeId].wpcMakerHelper.get('false') == None:
                self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString


    ### 1st approach...

    # def runner(self, currentNodeId):
    #     print(currentNodeId, end=" ")
    #     if len(self.cfg.nodes[currentNodeId].parent) < 1:
    #         return
    #     else:
    #         setOfParents = set(self.cfg.nodes[currentNodeId].parent)
    #         while len(setOfParents) >= 1:
    #             tempNodeId = setOfParents.pop()
    #             self.runner(tempNodeId)