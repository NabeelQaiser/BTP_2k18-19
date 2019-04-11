from z3 import *
from WpcStringConverter import WpcStringConverter


class McExecutor():

    def __init__(self):
        pass

    def getAllPaths(self, cfg, nodeId, currPath, allPaths):
        if not cfg.nodes[nodeId].visited:
            cfg.nodes[nodeId].visited = True
            currPath.append(nodeId)
            children = list(cfg.nodes[nodeId].next)
            if len(cfg.nodes[nodeId].next) == 0:
                tempPath = list(currPath)
                allPaths.append(tempPath)
            for child in children:
                self.getAllPaths(cfg, child, currPath, allPaths)
            currPath.pop()
            cfg.nodes[nodeId].visited = False

    def execute(self, mcUtility, predicateList):
        paths = []
        self.getAllPaths(mcUtility.cfg, 0, [], paths)
        mcUtility.execute(predicateList)
        for predicateIndex in range(len(predicateList)):
            # currPredicate = predicateList[predicateIndex]
            index = 0
            isRepeated = False
            isFaultyPredicate = False
            while index < len(paths):
                looksGood = True
                for nodeId in paths[index]:
                    looksGood = self.observeNode(mcUtility, nodeId, predicateIndex)
                    if not looksGood:
                        break   #todo : mention something worthy here
                if not looksGood:
                    if not isRepeated:
                        isRepeated = True
                        self.refine(mcUtility, paths[index], predicateList[predicateIndex], predicateIndex)       # we are adding all the 'if' conditions of this particular path
                        index = index - 1
                    else:       #todo: mention the error here
                        isFaultyPredicate = True
                        print("Problem for PREDICATE : \t", predicateList[predicateIndex])
                        print("There is a problem in the execution of path (here showing only node IDs) : \n\t", paths[index], "\nAnd the node ID which is causing problem is :\t", nodeId, "\n")
                        break
                index = index + 1
            if not isFaultyPredicate:
                print("SUCCESSFUL FOR PREDICATE :\t", predicateList[predicateIndex], "\n")


    def refine(self, mcUtility, path, oldPredicate, predicateIndex):
        newPredicateStr = oldPredicate
        for i in range(len(path)):
            if len(mcUtility.cfg.nodes[path[i]].next) > 1:
                if not mcUtility.wpcGenerator.nullInCondition(mcUtility.cfg.nodes[path[i]].ctx):
                    singleCondition = mcUtility.wpcGenerator.getConditionalString(mcUtility.cfg.nodes[path[i]].ctx)
                    if path[i + 1] == mcUtility.cfg.nodes[path[i]].branching['true']:
                        newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + singleCondition + " ) )"
                    elif path[i + 1] == mcUtility.cfg.nodes[path[i]].branching['true']:
                        newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( ! ( " + singleCondition + " ) ) )"

        mcUtility.generateWpcStringForAPredicate(newPredicateStr, predicateIndex)
        mcUtility.generateBooleanVariableForAPredicate(newPredicateStr, predicateIndex)





    def observeNode(self, mcUtility, nodeId, predicateIndex):
        boolean = mcUtility.cfg.nodes[nodeId].booleans[predicateIndex]
        result = True
        if len(boolean) == 3:
            result = self.ternaryOperation(mcUtility, nodeId, predicateIndex)
        elif len(boolean) == 1:
            if boolean[0] == "True" or boolean[0] == "skip":
                result = True
            elif boolean[0] == "False":
                result = False
            elif boolean[0] == "*":         # since it is always satisfiable !(((b==true) v (b==false)) --> (b==true))
                result = False

        else:
            print("**************     !!! SOMETHING UNEXPECTED HAPPENED !!!      ************")
        return result

    def ternaryOperation(self, mcUtility, nodeId, predicateIndex):
        boolVarStr = "b" + str(predicateIndex)
        phi = mcUtility.cfg.nodes[nodeId].booleans[predicateIndex][0]
        rawWpcStr = "( ( ( ( " + boolVarStr + " ) ^ " + phi + " ) v ( ( " + boolVarStr + " ) ^ ( ! ( " + phi + " ) ) ) v ( ( ! ( " + boolVarStr + " ) ) ^ " + phi + " ) ) ==> ( ( " + boolVarStr + " ) = " + " ( True ) ) )"
        rawWpcStr = rawWpcStr.replace("  ", " ")
        rawWpcStr = rawWpcStr.replace(" = ", " == ")
        z3StringConvertorObj = WpcStringConverter(rawWpcStr)
        z3StringConvertorObj.execute()
        return self.getZ3SolverResult(z3StringConvertorObj, mcUtility.allVar, boolVarStr)

    def getZ3SolverResult(self, z3StringConvertorObj, allVar, boolVarStr):
        for i in allVar:
            exec("%s=%s" % (i, "Real(\'" + i + "\')"))
        exec("%s=%s" % (boolVarStr, "Bool(\'" + boolVarStr + "\')"))
        z3SolverObj = Solver()
        if len(z3StringConvertorObj.implies_p) > 0:
            for i in range(len(z3StringConvertorObj.implies_p)):
                exec("%s" % ("z3SolverObj.add(" + z3StringConvertorObj.implies_p[i] + ")"))
                if not z3StringConvertorObj.convertedWpc == z3StringConvertorObj.implies_p_q[i]:
                    exec("%s" % ("z3SolverObj.add(" + z3StringConvertorObj.implies_p_q[i] + ")"))
        exec("%s" % ("z3SolverObj.add( Not(" + z3StringConvertorObj.convertedWpc + ") )"))
        satisfiability = str(z3SolverObj.check())
        if satisfiability == "unsat":
            return True
        elif satisfiability == "sat":
            return False
