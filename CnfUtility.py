from MyCFG import MyCFG
from MyUtility import MyUtility
from CnfNode import CnfNode

class CnfUtility(MyUtility):


    def __init__(self, helper):
        super().__init__(helper)

    def copyNode(self, node):
        res = CnfNode(node.id, node.ctx)
        res.next = node.next
        res.parent = node.parent
        res.domSet = node.domSet
        res.sDomSet = node.sDomSet
        res.iDom = node.iDom
        res.DFSet = node.DFSet
        res.levelFromEntryNode = node.levelFromEntryNode
        res.phiNode = node.phiNode
        res.variableSet = node.variableSet
        res.variableLHS = node.variableLHS
        res.variableRHS = node.variableRHS
        res.versionedPhiNode = node.versionedPhiNode
        res.versionedLHS = node.versionedLHS
        res.versionedRHS = node.versionedRHS
        res.destructedPhi = node.destructedPhi
        res.stringSsa = node.stringSsa
        res.oldString = node.oldString
        res.branching = node.branching
        return res

    def copyCfg(self, cfg):
        res = MyCFG()
        for nodeId in cfg.nodes:
            res.addNode(self.copyNode(cfg.nodes[nodeId]))
        return res

    # def explore(self, iCnfCfg, nodeId, branchingAncestor, res):
    #     if not iCnfCfg.nodes[nodeId].visited:
    #         if len(iCnfCfg.nodes[nodeId].next) <= 1 and len(iCnfCfg.nodes[nodeId].parent) <= 1:
    #             iCnfCfg.nodes[nodeId].visited = True
    #             temp = self.copyNode(iCnfCfg.nodes[nodeId])
    #             for i in range(len(branchingAncestor)):
    #                 temp.parentBranching[branchingAncestor[i][0]] = branchingAncestor[i][1]
    #             res.addNode(temp)
    #             if len(res) == 1:
    #                 temp.parent = set()
    #             else:
    #                 temp.parent = set(list(res.items())[-1][0])
    #             if len(iCnfCfg.nodes[nodeId].next) == 1:
    #                 next = self.explore(iCnfCfg, iCnfCfg.nodes[nodeId].next[0],
    #                                 branchingAncestor, res)
    #                 temp.next = {next}
    #             else:
    #                 temp.next = set()
    #             return nodeId
    #         elif len(iCnfCfg.nodes[nodeId].next) > 1 and len(iCnfCfg.nodes[nodeId].parent) <= 1:
    #             if not(nodeId in res.nodes.keys()):
    #                 temp = self.copyNode(iCnfCfg.nodes[nodeId])
    #                 temp.parent = set()
    #                 temp.next = set()
    #                 res.addNode(temp)
    #                 branchingAncestor.append((nodeId, True))
    #                 self.explore(iCnfCfg, iCnfCfg.nodes[nodeId].branching['true'], branchingAncestor, res)
    #                 return iCnfCfg.nodes[nodeId].branching['true']
    #             else:
    #                 branchingAncestor.append((nodeId, False))
    #                 iCnfCfg.nodes[nodeId].visited = True
    #                 self.explore(iCnfCfg, iCnfCfg.nodes[nodeId].branching['false'], branchingAncestor, res)
    #                 return iCnfCfg.nodes[nodeId].branching['false']
    #         elif len(iCnfCfg.nodes[nodeId].next) <= 1 and len(iCnfCfg.nodes[nodeId].parent) > 1:
    #             temp = self.copyNode(iCnfCfg.nodes[nodeId])
    #             for i in temp.parent:
    #                 next = branchingAncestor.pop()
    #
    #
    #     else:
    #         return nodeId   #todo: rectify this


    def explore(self, iCnfCfg, nodeId, branchingAncestor, res):
        if iCnfCfg.nodes[nodeId].color != 'black':
            if len(iCnfCfg.nodes[nodeId].next) <= 1 and len(iCnfCfg.nodes[nodeId].parent) <= 1:
                iCnfCfg.nodes[nodeId].color = 'grey'
                temp = self.copyNode(iCnfCfg.nodes[nodeId])
                if len(temp.parent) == 1:
                    temp.parent = {list(res.nodes.keys())[-1]}
                else:
                    temp.parent = set()
                for i in range(len(branchingAncestor)):
                    temp.parentBranching[branchingAncestor[i][0]] = branchingAncestor[i][1]
                res.addNode(temp)
                if len(temp.next) == 1:
                    nxt = self.explore(iCnfCfg, list(temp.next)[0], branchingAncestor, res)
                    temp.next = {nxt}
                else:
                    temp.next = set()
                iCnfCfg.nodes[nodeId].color = 'black'
                return nodeId
            else:
                if len(iCnfCfg.nodes[nodeId].parent) > 1:
                    iCnfCfg.nodes[nodeId].color = 'grey'
                    temp = self.copyNode(iCnfCfg.nodes[nodeId])
                    for parent in iCnfCfg.nodes[nodeId].parent:
                        if iCnfCfg.nodes[parent].color != 'black':
                            iCnfCfg.nodes[parent].color = 'black'
                            next = branchingAncestor.pop()
                            return self.explore(iCnfCfg, next[0], branchingAncestor, res)
                    temp.parent = {list(res.nodes.keys())[-1]}
                    for i in range(len(branchingAncestor)):
                        temp.parentBranching[branchingAncestor[i][0]] = branchingAncestor[i][1]
                    res.addNode(temp)
                    if len(temp.next) == 1:
                        next = self.explore(iCnfCfg, list(temp.next)[0], branchingAncestor, res)
                        temp.next = next
                        iCnfCfg.nodes[nodeId].color = 'black'
                        return nodeId
                if len(iCnfCfg.nodes[nodeId].next) > 1:
                    iCnfCfg.nodes[nodeId].color = 'grey'
                    temp = self.copyNode(iCnfCfg.nodes[nodeId])
                    if not nodeId in res.nodes.keys():
                        res.addNode(temp)
                        temp.parent = {list(res.nodes.keys())[-1]}
                    temp = res.nodes[nodeId]
                    trueNode = iCnfCfg.nodes[nodeId].branching['true']
                    if iCnfCfg.nodes[trueNode].color == 'white':
                        temp.next = {trueNode}
                        branchingAncestor.append((nodeId, 'true'))
                        return self.explore(iCnfCfg, trueNode, branchingAncestor, res)
                    falseNode = iCnfCfg.nodes[nodeId].branching['false']
                    if iCnfCfg.nodes[falseNode].color == 'white':
                        branchingAncestor.append((nodeId, 'false'))
                        return self.explore(iCnfCfg, falseNode, branchingAncestor, res)
                    iCnfCfg.nodes[nodeId].color = 'black'
                    return nodeId

    def traverse(self, iCnfCfg, nodeId, res):
        if not iCnfCfg.nodes[nodeId].visited:
            iCnfCfg.nodes[nodeId].visited = True
            temp = self.copyNode(iCnfCfg.nodes[nodeId])
            temp.next = set()
            temp.parent = set()
            temp.pre = self.counter
            iCnfCfg.nodes[nodeId].pre = self.counter
            self.counter = self.counter + 1
            if len(iCnfCfg.nodes[nodeId].next) > 1:
                self.traverse(iCnfCfg, iCnfCfg.nodes[nodeId].branching['false'], res)
                self.traverse(iCnfCfg, iCnfCfg.nodes[nodeId].branching['true'], res)
            elif len(iCnfCfg.nodes[nodeId].next) == 1:
                self.traverse(iCnfCfg, list(iCnfCfg.nodes[nodeId].next)[0], res)
            temp.post = self.counter
            iCnfCfg.nodes[nodeId].post = self.counter
            self.counter = self.counter + 1
            res.addNode(temp)

    def topologicalSort(self, iCnfCfg):
        res = MyCFG()
        self.counter = 1
        self.traverse(iCnfCfg, iCnfCfg.nodes[0].id, res)
        return res


    def unvisit(self, cfg):
        for nodeId in cfg.nodes:
            cfg.nodes[nodeId].visited = False

    def tour(self, iCnfCfg, nodeId, stk_):
        stk = list(stk_)
        if not iCnfCfg.nodes[nodeId].visited:
            iCnfCfg.nodes[nodeId].visited = True
            if (len(iCnfCfg.nodes[nodeId].parent) > 1):
                stk.pop()
            for i in range(len(stk)):
                iCnfCfg.nodes[nodeId].parentBranching[stk[i][0]] = stk[i][1]
            if len(iCnfCfg.nodes[nodeId].next) > 1:
                stk.append((nodeId, 'true'))
                self.tour(iCnfCfg, iCnfCfg.nodes[nodeId].branching['true'], stk)
                stk.append((nodeId, 'false'))
                self.tour(iCnfCfg, iCnfCfg.nodes[nodeId].branching['false'], stk)
            elif len(iCnfCfg.nodes[nodeId].next) == 1:
                self.tour(iCnfCfg, list(iCnfCfg.nodes[nodeId].next)[0], stk)


    def setParentBranching(self, iCnfCfg):
        stk = []
        self.tour(iCnfCfg, iCnfCfg.nodes[0].id, stk)

    def ssaToCnf(self, iCnfCfg):        # iCnfCfg -> intermediate cnfCfg
        branchingAncestor = []
        res = MyCFG()
        self.explore(iCnfCfg, iCnfCfg.nodes[0].id, branchingAncestor, res)
        return res

    def reverseDictOrder(self, reverseCnfCfg):
        temp = list(reverseCnfCfg.nodes.keys())
        res = MyCFG()
        for i in range(len(temp)-1, -1, -1):
            res.addNode(reverseCnfCfg.nodes[temp[i]])
        return res

    def copyParentBranching(self, cnfCfg, iCnfCfg):
        for nodeId in cnfCfg.nodes:
            cnfCfg.nodes[nodeId].parentBranching = iCnfCfg.nodes[nodeId].parentBranching

    def cnfVc(self, cnfCfg):
        res = []
        for nodeId in cnfCfg.nodes:
            antecedentStr = cnfCfg.nodes[nodeId].antecedent[0]
            isFirst = True
            for str in cnfCfg.nodes[nodeId].antecedent:
                if isFirst:
                    isFirst = False
                    continue
                antecedentStr = "AND( " + antecedentStr + ", " + str + " )"
            # print("\n]t&&&&&&&&&&&&&&&\n\n")
            # print(len(cnfCfg.nodes[nodeId].antecedent))
            # print("\n\n)))))))))))))\n\n")
            for i in range(len(cnfCfg.nodes[nodeId].consequent)):
                if cnfCfg.nodes[nodeId].isAssertion:
                    res.append("ASSERTION: " + cnfCfg.nodes[nodeId].consequent[i])
                else:
                    res.append("IMPLIES( " + antecedentStr + ", " + cnfCfg.nodes[nodeId].consequent[i] + " )")
        return res

    def iZ3format(self, cnfCfg):
        varSet = set()
        implies = []
        for nodeId in cnfCfg.nodes:
            antecedentStr = ""
            isFirst = True
            for str in cnfCfg.nodes[nodeId].antecedent:
                str = str.replace("  ", " ")
                str = str.strip()
                if isFirst:
                    isFirst = False
                    antecedentStr = "( " + str + " )"
                    continue
                antecedentStr = antecedentStr + " ^ ( " + str + " )"
            antecedentStr = "( " + antecedentStr + " )"
            for i in range(len(cnfCfg.nodes[nodeId].consequent)):
                if cnfCfg.nodes[nodeId].isAssertion:
                    implies.append("( " + cnfCfg.nodes[nodeId].consequent[i] + " )")
                else:
                    implies.append("( ( " + antecedentStr + " ) ==> ( " + cnfCfg.nodes[nodeId].consequent[i] + " ) )")
            for x in cnfCfg.nodes[nodeId].versionedLHS:
                varSet = varSet.union({cnfCfg.nodes[nodeId].versionedLHS[x]})
            for x in cnfCfg.nodes[nodeId].versionedRHS:
                varSet = varSet.union({cnfCfg.nodes[nodeId].versionedRHS[x]})
            for x in cnfCfg.nodes[nodeId].destructedPhi:
                varSet = varSet.union({cnfCfg.nodes[nodeId].destructedPhi[x][0], cnfCfg.nodes[nodeId].destructedPhi[x][1]})
        res = ""
        isFirst = True
        for x in implies:
            x = x.replace("  ", " ")
            x = x.strip()
            if isFirst:
                res = "( " + x + " )"
                isFirst = False
                continue
            res = res + " ^ ( " + x + " )"
        res = "( " + res + " )"
        return varSet, res
