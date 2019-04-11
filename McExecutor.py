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

    def execute(self, mcUtility, predicateList, sePathList, seSatInfoList):
        paths = []
        self.getAllPaths(mcUtility.cfg, 0, [], paths)
        mcUtility.execute(predicateList)
        for predicateIndex in range(len(predicateList)):
            print("----------------- Working for PREDICATE : \t", predicateList[predicateIndex])
            index = 0
            isFirstRefined = False
            isFaultyPredicate = False
            while index < len(paths):       #index for conventional loop
                looksGood = True
                probNodeId = -1
                for nodeId in paths[index]:
                    looksGood = self.observeNode(mcUtility, nodeId, predicateIndex)
                    if not looksGood:
                        probNodeId = nodeId
                        break   #todo : mention something worthy here
                if not looksGood:           #todo : check for spurious path here and also update the 'isRefined' variable
                    seSatisfiability = self.getSeSatisfiability(sePathList, seSatInfoList, paths[index])
                    if seSatisfiability == "ProblemInSeApi":
                        print("!!!!!!!!!    This path dosen't exists in SE API paths !!!!!", "\nAnd that path is : \t", paths[index])
                    elif seSatisfiability == "cannotsay":
                        isFaultyPredicate = True
                        print("Problem in execution of path (here showing only node IDs) : \n\t",
                              paths[index], "\nAnd the node ID which is causing problem is :\t", probNodeId, "\n")
                    elif seSatisfiability == "looksgood":     # se looks good where as mc doesn't
                        if not isFirstRefined:
                            isFirstRefined = True
                            self.firstRefine(mcUtility, paths[index], predicateList[predicateIndex], predicateIndex)  # we are adding all the 'if' conditions of this particular path
                            index = index - 1
                        else:
                            self.furtherRefine(mcUtility, paths[index], predicateList[predicateIndex], predicateIndex, probNodeId)  # we are adding assignment eq. as condition
                            index = index - 1
                    # if not isRefined:
                    #     isRefined = True

                    # else:       #todo: mention the error here
                    #     isFaultyPredicate = True
                    #     print("Problem for PREDICATE : \t", predicateList[predicateIndex])
                    #     print("There is a problem in the execution of path (here showing only node IDs) : \n\t", paths[index], "\nAnd the node ID which is causing problem is :\t", probNodeId, "\n")
                    #     break
                index = index + 1
            if not isFaultyPredicate:
                print("\nSUCCESSFUL FOR PREDICATE :\t", predicateList[predicateIndex], "\n")


    def firstRefine(self, mcUtility, path, oldPredicate, predicateIndex):
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

    def furtherRefine(self, mcUtility, path, oldPredicate, predicateIndex, probNodeId):
        newPredicateStr = oldPredicate
        currentNode = mcUtility.cfg.nodes[probNodeId]
        ruleName = mcUtility.helper.getRuleName(currentNode.ctx).strip()
        if ruleName == "assignment_statement":
            lhsVar = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[0]).strip()
            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
            # DON'T expect more...
            varString = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[2]).strip()
            varString = varString.replace("( )", "")
            varString = varString.replace("  ", " ").strip()
            rhsVar = "( " + varString + " )"
            if not lhsVar == "" and not varString == "":
                newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
        elif ruleName == "update_statement":
            for i in range(currentNode.ctx.getChildCount()):
                # finding "update_set_clause"...
                if currentNode.ctx.children[i].getChildCount() > 1 and mcUtility.helper.getRuleName(currentNode.ctx.children[i]) == "update_set_clause":
                    updateSetCtx = currentNode.ctx.children[i]
                    for j in range(updateSetCtx.getChildCount()):
                        # finding "column_based_update_set_clause"...
                        if updateSetCtx.children[j].getChildCount() > 1 and mcUtility.helper.getRuleName(updateSetCtx.children[j]) == "column_based_update_set_clause":
                            lhsVar = mcUtility.wpcGenerator.ssaString.getTerminal(updateSetCtx.children[j].children[0]).strip()
                            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                            # DON'T expect more...
                            varString = mcUtility.wpcGenerator.ssaString.getTerminal(updateSetCtx.children[j].children[2]).strip()
                            varString = varString.replace("( )", "")
                            varString = varString.replace("  ", " ").strip()
                            rhsVar = " ( " + varString + " ) "
                            if not lhsVar == "" and not varString == "":
                                newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                # finding "where_clause"...
                elif currentNode.ctx.children[i].getChildCount() > 1 and mcUtility.helper.getRuleName(currentNode.ctx.children[i]) == "where_clause":
                    if not mcUtility.wpcGenerator.nullInCondition(currentNode.ctx.children[i].children[1]):
                        whereCondition = mcUtility.wpcGenerator.getConditionalString(currentNode.ctx.children[i].children[1])
                        newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + whereCondition + " ) )"
        elif ruleName == "insert_statement":    # assuming Attributes in which data is to be inserted is mentioned with Tablename
            tempNode = currentNode.ctx.children[1]  # single_table_insert
            myLHS = []
            myRHS = []
            count = tempNode.children[0].getChildCount()  # inset_into_clause
            if count > 2:
                i = 2
                while i < count:
                    if tempNode.children[0].children[i].getChildCount() > 0:
                        myLHS.append(tempNode.children[0].children[i].getText().strip())
                    i = i + 1
            count = tempNode.children[1].children[1].getChildCount()  # expression_list
            i = 0
            while i < count:
                node = tempNode.children[1].children[1].children[i]
                if node.getChildCount() > 0:
                    myRHS.append(mcUtility.wpcGenerator.ssaString.getTerminal(node).strip())
                i = i + 1
            # do replacing in wpcString now...
            if len(myLHS) > 0:
                for i in range(len(myLHS)):
                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                    # DON'T expect more...
                    varString = myRHS[i]
                    varString = varString.replace("( )", "")
                    varString = varString.replace("  ", " ").strip()
                    rhsVar = "( " + varString + " )"
                    if not myLHS[i] == "" and not varString == "":
                        newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + myLHS[i] + " == " + rhsVar + " ) )"

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

    def getSeSatisfiability(self, sePathList, seSatInfoList, mcPath):
        target = -1
        for i in range(len(sePathList)):
            if mcPath == sePathList[i]:
                target = i
                break
        if target != -1:
            return seSatInfoList[target]
        else:
            return "ProblemInSeApi"
