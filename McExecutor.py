from z3 import *

from McSsaForBooleanVc import McSsaForBooleanVc
from WpcStringConverter import WpcStringConverter


class McExecutor():

    def __init__(self):
        pass

    def getAllPaths(self, cfg, nodeId, currPath, allPaths):
        if not cfg.nodes[nodeId].visited:
            # print("--", nodeId)
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


    def unvisitCfg(self, mcUtility):
        for nodeId in mcUtility.cfg.nodes:
            mcUtility.cfg.nodes[nodeId].visited = False
    
    
    def setParentBranching(self, cfg, nodeId, stk_):
        stk = list(stk_)
        if not cfg.nodes[nodeId].visited:
            cfg.nodes[nodeId].visited = True
            if (len(cfg.nodes[nodeId].parent) > 1):
                stk.pop()
            for i in range(len(stk)):
                cfg.nodes[nodeId].parentBranching[stk[i][0]] = stk[i][1]
            if len(cfg.nodes[nodeId].next) > 1:
                stk.append((nodeId, 'true'))
                self.setParentBranching(cfg, cfg.nodes[nodeId].branching['true'], stk)
                stk.append((nodeId, 'false'))
                self.setParentBranching(cfg, cfg.nodes[nodeId].branching['false'], stk)
            elif len(cfg.nodes[nodeId].next) == 1:
                self.setParentBranching(cfg, list(cfg.nodes[nodeId].next)[0], stk)


    def initRawPredicateContent(self, predicateList, rawPredicateContentList, rawPredicateContentDict):
        for i in range(len(predicateList)):
            rawPredicateContentDict[i] = [rawPredicateContentList[i], 'cond']

    def execute(self, mcUtility, predicateList, rawPredicateContentList, sePathList, seSatInfoList, tableInfo):
        self.setParentBranching(mcUtility.cfg, 0, [])
        self.unvisitCfg(mcUtility)

        rawPredicateContentDict = dict()        # format : {'index of predicate' : ['rawPredicate', 'ass / cond'], ...}
        self.initRawPredicateContent(predicateList, rawPredicateContentList, rawPredicateContentDict)
        updatedPredList = list(predicateList)
        paths = []
        self.getAllPaths(mcUtility.cfg, 0, [], paths)
        self.unvisitCfg(mcUtility)
        # print("mcPathsList", paths)
        mcUtility.execute(predicateList)      # important, as we need all variables

        spuriousCoount = 0
        refinementCount = 0

        pathIndex = 0
        while pathIndex < len(paths):
            # rawPredicateContentList --> for generating consequents
            print("\n\n\n__________VAVAVAVAVAVAVA__________ Working for path : ", paths[pathIndex], "_________VAVAVAVAVAVAVA__________")
            tempSpurious, tempRefinement = self.executeForAPath(mcUtility, rawPredicateContentList, updatedPredList, rawPredicateContentDict, paths[pathIndex], self.getSeSatisfiability(sePathList, seSatInfoList, paths[pathIndex]), tableInfo)
            spuriousCoount = spuriousCoount + tempSpurious
            refinementCount = refinementCount + tempRefinement
            # result is printed in the above function
            self.cleanForNextPath(mcUtility, predicateList)     #remove additional predicates, ie, apart from initial predicates
            pathIndex = pathIndex + 1
        return spuriousCoount, refinementCount






        # for predicateIndex in range(len(predicateList)):
        #     print("----------------- Working for PREDICATE : \t", predicateList[predicateIndex])
        #     index = 0
        #     isFirstRefined = False
        #     isFaultyPredicate = False
        #     probNodeIdSet = set()
        #     while index < len(paths):       #index for conventional loop
        #         looksGood = True
        #         probNodeId = -1
        #         for nodeId in paths[index]:
        #             looksGood = self.observeNode(mcUtility, nodeId, predicateIndex)
        #             if not looksGood:
        #                 probNodeId = nodeId
        #                 break   #todo : mention something worthy here
        #         if not looksGood:           #todo : check for spurious path here and also update the 'isRefined' variable
        #             seSatisfiability = self.getSeSatisfiability(sePathList, seSatInfoList, paths[index])
        #             if seSatisfiability == "ProblemInSeApi":
        #                 print("!!!!!!!!!    This path dosen't exists in SE API paths !!!!!", "\nAnd that path is : \t", paths[index])
        #             elif seSatisfiability == "cannotsay":
        #                 isFaultyPredicate = True
        #                 print("Problem in execution of path (here showing only node IDs) : \n\t",
        #                       paths[index], "\nAnd the node ID which is causing problem is :\t", probNodeId, "\n")
        #             elif seSatisfiability == "looksgood":     # se looks good where as mc doesn't
        #                 if not isFirstRefined:
        #                     isFirstRefined = True
        #                     tempPred = self.firstRefine(mcUtility, paths[index], updatedPredList[predicateIndex], predicateIndex)  # we are adding all the 'if' conditions of this particular path
        #                     updatedPredList[predicateIndex] = tempPred
        #                     index = index - 1
        #                 else:
        #                     if probNodeId not in probNodeIdSet:
        #                         tempPred = self.furtherRefine(mcUtility, paths[index], updatedPredList[predicateIndex], predicateIndex, probNodeId)  # we are adding assignment eq. as condition
        #                         updatedPredList[predicateIndex] = tempPred
        #                         probNodeIdSet.add(probNodeId)
        #                         index = index - 1
        #                     else:
        #                         isFaultyPredicate = True
        #                         print("Problem in execution of path (even after adding assignment equivalent condition) : \n\t",
        #                               paths[index], "\nAnd the node ID for which equivalent condition is already added :\t", probNodeId,
        #                               "\n")
        #             # if not isRefined:
        #             #     isRefined = True
        #
        #             # else:       #todo: mention the error here
        #             #     isFaultyPredicate = True
        #             #     print("Problem for PREDICATE : \t", predicateList[predicateIndex])
        #             #     print("There is a problem in the execution of path (here showing only node IDs) : \n\t", paths[index], "\nAnd the node ID which is causing problem is :\t", probNodeId, "\n")
        #             #     break
        #         index = index + 1
        #     if not isFaultyPredicate:
        #         print("\nSUCCESSFUL FOR PREDICATE :\t", predicateList[predicateIndex], "\n")


    def cleanForNextPath(self, mcUtility, predicateList):     #todo : remove additional predicates, ie, apart from initial predicates
        notToRemove = []
        for i in range(len(predicateList)):
            notToRemove.append(i)
        for nodeId in mcUtility.cfg.nodes:
            wpcStringKeys = list(mcUtility.cfg.nodes[nodeId].wpcString.keys())
            booleansKeys = list(mcUtility.cfg.nodes[nodeId].booleans.keys())
            for index in wpcStringKeys:
                if not index in notToRemove:
                    mcUtility.cfg.nodes[nodeId].wpcString.pop(index, None)
            for index in booleansKeys:
                if not index in notToRemove:
                    mcUtility.cfg.nodes[nodeId].booleans.pop(index, None)


    def executeForAPath(self, mcUtility, rawPredicateContentList, updatedPredList, rawPredicateContentDict, mcPath, seZ3Output, tableInfo):     # seZ3Output : 'ProblemInSeApi' / 'looksgood' / 'cannotsay'
        mcPredList = list(updatedPredList)
        isSpurious = 0
        refinementCount = 0
        mcRawPredicateContentDict = dict(rawPredicateContentDict)
        if seZ3Output == 'ProblemInSeApi':
            print("\n!!!! NO PATH MATCHED CORRESPONDING TO : ", mcPath, " in SE provided paths !!!!\n")
            # pass
        elif seZ3Output == "NoZ3OutputGivenForThisPath":
            print("\n!!!! SE did'd GENERATED OUTPUT FOR PATH : ", mcPath, " in SE API module !!!!\n")
            # pass
        else:
            mcOutput = ""
            while mcOutput != seZ3Output:       # assuming it never happen that mcOutput == looksgood and seZ3Output == cannotsay
                mcUtility.generateBooleanVariableForAPath(mcPredList, mcPath)
                eqBooleanProg = self.generateEqBooleanProg(mcUtility, mcPredList, mcPath)
                antecedent, consequent, versionisedVarSet = self.generateVcForBooleanProg(mcUtility, rawPredicateContentList, eqBooleanProg, mcPredList, mcRawPredicateContentDict, mcPath, tableInfo)


                if len(antecedent) == 0:
                    print("\n\nSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS Output for a PATH......................................................................................")
                    print("%%%%%%%% All booleans are SKIP for path :  ", mcPath, ", And seZ3Output : ", seZ3Output)
                    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    break
                mcOutput = self.checkSatisfiability(mcUtility, antecedent, consequent, versionisedVarSet)      # here refinement may be needed
                print("///////////////////////// Checking Spurious-ness:\n", "mcOutput = ", mcOutput, ",\t seZ3Output = ", seZ3Output)
                if mcOutput == seZ3Output:
                    if mcOutput == "looksgood":
                        # pass
                        print("\n\nSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS Output for a PATH......................................................................................")
                        print("%%%%%%%% No violation in path :  ", mcPath)
                        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    elif mcOutput == "cannotsay":
                        culprits = self.findCulprits(mcUtility, eqBooleanProg, mcPath)
                        print("\n\nSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS Output for a PATH......................................................................................")
                        print("%%%%%%%% Violation in path :  ", mcPath, "\tCulprit nodes are : ", culprits)
                        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    break
                else:           # also consider for the situation where, after saturation of refining, mcOutput and seZ3Output do not match
                    culprits = self.findCulprits(mcUtility, eqBooleanProg, mcPath)
                    if len(culprits) == 0:  # saturation attained, no culprits
                        print("\n\nSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS Output for a PATH......................................................................................")
                        print("!!!! NO CULPRIT FOUND, BUT STILL SE AND MC ARE NOT CONSISTENT, FOR THE PATH : ", mcPath)     # todo : handle the situation where no culprit found
                        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                        break
                    else:
                        isSpurious = 1
                        refinementCount = refinementCount + 1
                        self.refine(mcUtility, mcPredList, mcRawPredicateContentDict, mcPath, culprits)
        return isSpurious, refinementCount



    def findCulprits(self, mcUtility, eqBooleanProg, mcPath):        # returns -1 in case of NO culprit found
        i = len(mcPath) - 1
        res = []        # list of all the culprits
        while i >= 0:       # traversing in the reverse direction
            predicateIndex = eqBooleanProg[mcPath[i]]
            boolean = mcUtility.cfg.nodes[mcPath[i]].booleans[predicateIndex]
            if len(boolean) == 3:
                res.append(mcPath[i])
            elif len(boolean) == 1 and boolean[0] == "*":
                res.append(mcPath[i])
            i = i - 1
        return res

    def refine(self, mcUtility, mcPredList, mcRawPredicateContentDict, mcPath, culprits):
        print("------------- Entered Refine(...) fn.")
        for nodeId in culprits:    # culprit ~ nodeId
            rawContent, assCond = self.getRawContentOfANode(nodeId, mcUtility)
            newPredicate = self.getNewBrackettedPredicate(mcUtility, nodeId)
            if not rawContent == "" and not newPredicate == "":
                if not rawContent in [i[0] for  i in mcRawPredicateContentDict.values()]:
                    mcPredList.append(newPredicate)
                    predIndex = len(mcPredList) - 1
                    mcRawPredicateContentDict[predIndex] = [rawContent, assCond]
                    mcUtility.cfg.nodes[nodeId].booleans[predIndex] = ["True"]
            controlNodeIds = []
            for key in mcUtility.cfg.nodes[nodeId].parentBranching:
                controlNodeIds.append(key)
            for nodeId in controlNodeIds:
                rawContent, assCond = self.getRawContentOfANode(nodeId, mcUtility)
                newPredicate = self.getNewBrackettedPredicate(mcUtility, nodeId)
                if not rawContent == "" and not newPredicate == "":
                    if not rawContent in [i[0] for i in mcRawPredicateContentDict.values()]:        #todo: someone may consider the implications of the new predicates to old predicates
                        mcPredList.append(newPredicate)
                        predIndex = len(mcPredList) - 1
                        mcRawPredicateContentDict[predIndex] = [rawContent, assCond]
                        mcUtility.cfg.nodes[nodeId].booleans[predIndex] = ["True"]



    def checkSatisfiability(self, mcUtility, antecedent, consequent, versionisedVarSet):
        rawWpcStr = "( ( " + antecedent + " ) ==> ( " + consequent + " ) )"
        rawWpcStr = rawWpcStr.replace("  ", " ")
        rawWpcStr = rawWpcStr.replace(" = ", " == ")
        z3StringConvertorObj = WpcStringConverter(rawWpcStr)
        z3StringConvertorObj.execute()
        tempRes =  self.getZ3SolverResult(z3StringConvertorObj, versionisedVarSet, "JUST_IGNORE_IT_NOTHING_MUCH")
        if tempRes:
            return "looksgood"
        else:
            return "cannotsay"


    def printBooleans(self, mcUtility, mcPath):
        print("\n&&&&&&&&&&&&&&&&&&&&&& BOOLEANS and WPCs")
        for nodeId in mcPath:
            print(nodeId, ": ", mcUtility.cfg.nodes[nodeId].booleans)
            print(nodeId, ": ", mcUtility.cfg.nodes[nodeId].wpcString)
            print("--")


    def generateVcForBooleanProg(self, mcUtility, rawPredicateContentList, eqBooleanProg, mcPredList, rawPredicateContentDict, mcPath, tableInfo):
        toVersionizeList = list()   # list of predicateIndex
        toVersionizeContentDict = dict()

        print("\n&&&&&&&&&&&&&&&&&&&&&& mcPredList,", len(mcPredList), " (Updated pred-list for further working)")
        for i in mcPredList:
            print(i)
        self.printBooleans(mcUtility, mcPath)

        for nodeId in mcPath:
            predicateIndex = eqBooleanProg[nodeId]
            if len(mcUtility.cfg.nodes[nodeId].booleans[predicateIndex]) == 1:       # "True" / "*" / "skip" only
                if mcUtility.cfg.nodes[nodeId].booleans[predicateIndex][0] == "True":
                    toVersionizeList.append(predicateIndex)
                    toVersionizeContentDict[predicateIndex] = [rawPredicateContentDict[predicateIndex][0], rawPredicateContentDict[predicateIndex][1]]
                elif mcUtility.cfg.nodes[nodeId].booleans[predicateIndex][0] == "*":
                    # temp = "( " + rawPredicateContentDict[predicateIndex][0] + " ) OR ( NOT ( " + rawPredicateContentDict[predicateIndex][0] + " ) )"
                    toVersionizeList.append(predicateIndex)
                    toVersionizeContentDict[predicateIndex] = [rawPredicateContentDict[predicateIndex][0], rawPredicateContentDict[predicateIndex][1]]
            elif len(mcUtility.cfg.nodes[nodeId].booleans[predicateIndex]) == 3:  # "phi, *, True"
                phi = mcUtility.cfg.nodes[nodeId].booleans[predicateIndex][0]
                # temp = "( ( " + phi + " ) AND ( " + rawPredicateContentDict[predicateIndex][0] + " ) ) OR ( ( " + phi + " ) AND NOT ( " + rawPredicateContentDict[predicateIndex][0] + " ) ) OR ( NOT ( " + phi + " ) AND ( " + rawPredicateContentDict[predicateIndex][0] + " ) )"
                toVersionizeList.append(predicateIndex)
                toVersionizeContentDict[predicateIndex] = [rawPredicateContentDict[predicateIndex][0], rawPredicateContentDict[predicateIndex][1], phi]
        mcSsaForBooleanVc = McSsaForBooleanVc()
        versionizedPredicateList, versionisedVarSet, versionizedConsequentList = mcSsaForBooleanVc.execute(toVersionizeList, toVersionizeContentDict, tableInfo, rawPredicateContentList)
        # print("versionizedPredicateList, versionisedVarSet, versionizedConsequentList---\n", versionizedPredicateList,"\n", versionisedVarSet, "\n", versionizedConsequentList)

        # print("&&&&&&&&&&&&&&&&&&&&&& toVersionizeList :", toVersionizeList, " (List of pred-index need to versionize)")
        #
        print("&&&&&&&&&&&&&&&&&&&&&& versionizedPredicateList,", len(versionizedPredicateList), " (List of eq. predicates after versionization)")
        for i in versionizedPredicateList:
            print(i)
        # print("&&&&&&&&&&&&&&&&&&&&&& versionizedConsequentList", " (Versionized ORIGINAL predicates for Consequent in VC)")
        for i in versionizedConsequentList:
            print(i)
        print()

        finalVc = ""
        finalConsequent = ""
        isFirst = True
        currIndex = 0
        for i in range(len(mcPath)):
            temp = ""
            predicateIndex = eqBooleanProg[mcPath[i]]
            if len(mcUtility.cfg.nodes[mcPath[i]].booleans[predicateIndex]) == 1:  # "True" / "*" / "skip" only
                if mcUtility.cfg.nodes[mcPath[i]].booleans[predicateIndex][0] == "True":
                    if len(mcUtility.cfg.nodes[mcPath[i]].next) > 1:
                        if mcUtility.cfg.nodes[mcPath[i]].branching['true'] == mcPath[i + 1]:
                            temp = "( ( " + versionizedPredicateList[currIndex] + " ) == True )"
                            currIndex = currIndex + 1
                        elif mcUtility.cfg.nodes[mcPath[i]].branching['false'] == mcPath[i + 1]:
                            temp = "( ( " + versionizedPredicateList[currIndex] + " ) == False )"
                            currIndex = currIndex + 1
                        else:
                            # pass
                            print("!!!! some problem occured !!!!")
                    else:       # considering last node will have 0 child
                        temp = "( ( " + versionizedPredicateList[currIndex] + " ) == True )"
                        currIndex = currIndex + 1
                elif mcUtility.cfg.nodes[mcPath[i]].booleans[predicateIndex][0] == "*":
                    temp = versionizedPredicateList[currIndex]
                    temp = "( ( " + temp + " ) v ( ! ( " + temp + " ) ) )"
                    currIndex = currIndex + 1
            elif len(mcUtility.cfg.nodes[mcPath[i]].booleans[predicateIndex]) == 3:  # "phi, *, True"
                temp = versionizedPredicateList[currIndex]
                currIndex = currIndex + 1
            if not temp == "":
                if isFirst:
                    isFirst = False
                    finalVc = temp
                else:
                    finalVc = "( ( " + finalVc + " ) ^ ( " + temp + " ) )"
                # print("-------------temp = ", temp)
        isFirst = True
        for consequent in versionizedConsequentList:
            if isFirst:
                isFirst = False
                finalConsequent = "( ( " + consequent + " ) == True )"
            else:
                finalConsequent = "( ( " + finalConsequent + " ) ^ ( ( " + consequent + " ) == True ) )"
        return finalVc, finalConsequent, versionisedVarSet



    def generateEqBooleanProg(self, mcUtility, mcPredList, mcPath):
        result = dict()         # format :: { nodeId : correspondingPredicateIndex, ...}
        for nodeId in mcPath:
            temp = -1   # it signifies predicateIndex
            for i in range(len(mcPredList)):
                if len(mcUtility.cfg.nodes[nodeId].booleans[i]) == 1:       # "True" / "*" / "skip" only
                    if mcUtility.cfg.nodes[nodeId].booleans[i][0] == "True":
                        temp = i
                        break
                    elif mcUtility.cfg.nodes[nodeId].booleans[i][0] == "*":
                        temp = i
                        # continue
                elif len(mcUtility.cfg.nodes[nodeId].booleans[i]) == 3:     # "phi, *, True"
                    temp = i
            if temp == -1:       # temp=-1 means "skip" at this point
                temp = 0
            result[nodeId] = temp
        return result


    def getRawContentOfANode(self, nodeId, mcUtility):
        currentNode = mcUtility.cfg.nodes[nodeId]
        ruleName = mcUtility.helper.getRuleName(currentNode.ctx).strip()
        rawContent = ""
        assCond = ""
        if len(currentNode.next) > 1:
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "cond"
            if mcUtility.wpcGenerator.nullInCondition(currentNode.ctx):
                rawContent = ""
                assCond = ""
        elif ruleName == "assignment_statement":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        elif ruleName == "update_statement":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        elif ruleName == "insert_statement":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        elif ruleName == "select_statement":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        elif ruleName == "cursor_declaration":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        elif ruleName == "fetch_statement":
            rawContent = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx).strip()
            assCond = "ass"
        return rawContent, assCond

    # def firstRefine(self, mcUtility, path, oldPredicate, predicateIndex):
    #     newPredicateStr = oldPredicate
    #     for i in range(len(path)):
    #         if len(mcUtility.cfg.nodes[path[i]].next) > 1:
    #             if not mcUtility.wpcGenerator.nullInCondition(mcUtility.cfg.nodes[path[i]].ctx):
    #                 singleCondition = mcUtility.wpcGenerator.getConditionalString(mcUtility.cfg.nodes[path[i]].ctx)
    #                 if path[i + 1] == mcUtility.cfg.nodes[path[i]].branching['true']:
    #                     newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + singleCondition + " ) )"
    #                 elif path[i + 1] == mcUtility.cfg.nodes[path[i]].branching['true']:
    #                     newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( ! ( " + singleCondition + " ) ) )"
    #
    #     mcUtility.generateWpcStringForAPredicate(newPredicateStr, predicateIndex)
    #     mcUtility.generateBooleanVariableForAPredicate(newPredicateStr, predicateIndex)
    #     # print("%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$4 firstRefine", newPredicateStr)
    #     return newPredicateStr

    def getNewBrackettedPredicate(self, mcUtility, nodeId):
        currentNode = mcUtility.cfg.nodes[nodeId]
        ruleName = mcUtility.helper.getRuleName(currentNode.ctx).strip()
        newPredicateStr = ""
        if len(currentNode.next) > 1:
            newPredicateStr = mcUtility.wpcGenerator.getConditionalString(currentNode.ctx).strip()
            if mcUtility.wpcGenerator.nullInCondition(currentNode.ctx):
                newPredicateStr = ""
        elif ruleName == "assignment_statement":
            lhsVar = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[0]).strip()
            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
            # DON'T expect more...
            varString = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[2]).strip()
            varString = varString.replace("( )", "")
            varString = varString.replace("  ", " ").strip()
            rhsVar = "( " + varString + " )"
            if not lhsVar == "" and not varString == "":
                newPredicateStr = "( " + lhsVar + " == " + rhsVar + " )"
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
                                if not newPredicateStr == "":
                                    newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                                else:
                                    newPredicateStr = "( " + lhsVar + " == " + rhsVar + " )"
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
                        if not newPredicateStr == "":
                            newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + myLHS[i] + " == " + rhsVar + " ) )"
                        else:
                            newPredicateStr = "( " + myLHS[i] + " == " + rhsVar + " )"
        elif ruleName == "select_statement":
            tempNode = currentNode.ctx.children[0].children[0]
            myRHS = []
            myLHS = []
            conditionInFromClause = ""
            # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
            into_flag = -1
            whereHandled_flag = False
            for i in range(tempNode.getChildCount()):
                if tempNode.children[i].getChildCount() > 0:
                    if mcUtility.helper.getRuleName(tempNode.children[i]) == "selected_element":
                        varString = mcUtility.wpcGenerator.ssaString.getTerminal(tempNode.children[i]).strip()
                        myRHS.append(mcUtility.wpcGenerator.getVariableForAggregateFunctionInSelect(varString))  # <--- RHS
                    elif mcUtility.helper.getRuleName(tempNode.children[i]) == "into_clause":
                        into_flag = i
                        intoNode = tempNode.children[i]
                        for x in range(intoNode.getChildCount()):
                            if intoNode.children[x].getChildCount() > 0 and mcUtility.helper.getRuleName(intoNode.children[x]) == "variable_name":
                                myLHS.append(mcUtility.wpcGenerator.ssaString.getTerminal(intoNode.children[x]).strip())  # <--- LHS
                    elif mcUtility.helper.getRuleName(tempNode.children[i]) == "from_clause":
                        conditionInFromClause = mcUtility.wpcGenerator.extractConditionsInFromClause(tempNode.children[i].children[1]).strip()
                        # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                    elif mcUtility.helper.getRuleName(tempNode.children[i]) == "where_clause":
                        # myLHS & myRHS & conditionInFromClause will be already filled here if they should be
                        whereCondition = mcUtility.wpcGenerator.getConditionalString(tempNode.children[i].children[1])
                        # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                        if not conditionInFromClause == "":  # merging condition from WHERE and FROM_CLAUSE
                            whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                        whereHandled_flag = True
                        if into_flag > -1:
                            for j in range(len(myLHS)):
                                if newPredicateStr == "":
                                    newPredicateStr = "( " + myLHS[j] + " == " + myRHS[j] + " )"
                                else:
                                    newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + myLHS[j] + " == " + myRHS[j] + " ) )"
                            if mcUtility.wpcGenerator.nullInCondition(tempNode.children[i].children[1]):  # NULL +nt in where_condition
                                if not conditionInFromClause == "":
                                    newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + conditionInFromClause + " ) )"
                            else:  # NULL not +nt in where_condition
                                newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + whereCondition + " ) )"
            if whereHandled_flag is False and into_flag > -1:
                # whereCondition do not exist in SELECT
                for i in range(len(myLHS)):
                    if newPredicateStr == "":
                        newPredicateStr = "( " + myLHS[i] + " == " + myRHS[i] + " )"
                    else:
                        newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + myLHS[i] + " == " + myRHS[i] + " ) )"
                # BUT, don't relax, condition from FROM_CLAUSE may not be empty!!!
                if not conditionInFromClause == "":
                    newPredicateStr = "( ( " + newPredicateStr + " ) ^ ( " + conditionInFromClause + " ) )"
        elif ruleName == "cursor_declaration":
            lhsVar = ""
            rhsVar = ""
            whereCondition = ""
            conditionInFromClause = ""
            isWherePresent = False
            isNullPresentInWhere = False
            for i in range(currentNode.ctx.getChildCount()):
                if mcUtility.helper.getRuleName(currentNode.ctx.children[i]) == "cursor_name":
                    lhsVar = mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[i]).strip()
                elif mcUtility.helper.getRuleName(currentNode.ctx.children[i]) == "select_statement":
                    tempCtx = currentNode.ctx.children[i].children[0].children[0]
                    for j in range(tempCtx.getChildCount()):
                        if mcUtility.helper.getRuleName(tempCtx.children[j]) == "from_clause":
                            conditionInFromClause = mcUtility.wpcGenerator.extractConditionsInFromClause(tempCtx.children[j].children[1]).strip()
                            # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                        elif mcUtility.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                            isWherePresent = True
                            if mcUtility.wpcGenerator.nullInCondition(tempCtx.children[j].children[1]):
                                isNullPresentInWhere = True
                            else:
                                whereCondition = mcUtility.wpcGenerator.getConditionalString(tempCtx.children[j].children[1])
                                # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                    # BUT what to do if there are multiple SELECTION attributes here???...as per datasets assuming single attribute...
                    varString = mcUtility.wpcGenerator.ssaString.getTerminal(tempCtx.children[1]).strip()
                    rhsVar = mcUtility.wpcGenerator.getVariableForAggregateFunctionInSelect(varString)
            if not (lhsVar == "") and not (rhsVar == ""):
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            newPredicateStr = "( " + lhsVar + " == " + rhsVar + " )"
                        else:
                            newPredicateStr = "( ( " + conditionInFromClause + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = "( ( " + conditionInFromClause + " ) ^ ( " + whereCondition + " ) )"
                        newPredicateStr = "( ( " + whereCondition + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                else:
                    if not conditionInFromClause == "":
                        newPredicateStr = "( ( " + conditionInFromClause + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                    else:
                        newPredicateStr = "( " + lhsVar + " == " + rhsVar + " )"
        elif ruleName == "fetch_statement":
            newPredicateStr = "( ( " + mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[3]).strip() + " ) == ( " + mcUtility.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[1]).strip() + " ) )"

        newPredicateStr = newPredicateStr.replace("  ", " ")
        newPredicateStr = newPredicateStr.replace(" = ", " == ").strip()
        return newPredicateStr

    #
    #
    #
    # def observeNode(self, mcUtility, nodeId, predicateIndex):
    #     boolean = mcUtility.cfg.nodes[nodeId].booleans[predicateIndex]
    #     result = True
    #     if len(boolean) == 3:
    #         result = self.ternaryOperation(mcUtility, nodeId, predicateIndex)
    #     elif len(boolean) == 1:
    #         if boolean[0] == "True" or boolean[0] == "skip":
    #             result = True
    #         elif boolean[0] == "False":
    #             result = False
    #         elif boolean[0] == "*":         # since it is always satisfiable !(((b==true) v (b==false)) --> (b==true))
    #             result = False
    #
    #     else:
    #         print("**************     !!! SOMETHING UNEXPECTED HAPPENED !!!      ************")
    #     return result
    #
    # def ternaryOperation(self, mcUtility, nodeId, predicateIndex):
    #     boolVarStr = "b" + str(predicateIndex)
    #     phi = mcUtility.cfg.nodes[nodeId].booleans[predicateIndex][0]
    #     rawWpcStr = "( ( ( ( " + boolVarStr + " ) ^ " + phi + " ) v ( ( " + boolVarStr + " ) ^ ( ! ( " + phi + " ) ) ) v ( ( ! ( " + boolVarStr + " ) ) ^ " + phi + " ) ) ==> ( ( " + boolVarStr + " ) = " + " ( True ) ) )"
    #     rawWpcStr = rawWpcStr.replace("  ", " ")
    #     rawWpcStr = rawWpcStr.replace(" = ", " == ")
    #     z3StringConvertorObj = WpcStringConverter(rawWpcStr)
    #     z3StringConvertorObj.execute()
    #     return self.getZ3SolverResult(z3StringConvertorObj, mcUtility.allVar, boolVarStr)


    def getZ3SolverResult(self, z3StringConvertorObj, allVar, boolVarStr):
        for i in allVar:
            exec("%s=%s" % (i, "Real(\'" + i + "\')"))
        exec("%s=%s" % (boolVarStr, "Bool(\'" + boolVarStr + "\')"))
        z3SolverObj = Solver()
        # print("z3StringConvertorObj.wpcString---\n", z3StringConvertorObj.wpcString)
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


