import os
import sys
import datetime
import time
from importlib import reload
from subprocess import call

from antlr4 import *

from McExecutor import McExecutor
from McNode import McNode
from McPreProcessor import McPreProcessor
from McUtility import McUtility
from MyCFG import MyCFG
from MyHelper import MyHelper
from MyRawCfgToGraph import MyRawCfgToGraph
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from PreProcessor import PreProcessor
from SeAPI.SePathsInfoForMc import SePathsInfoForMc
from WpcGenerator import WpcGenerator
from WpcStringConverter import WpcStringConverter
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser


def copyNode(node):
    res = McNode(node.id, node.ctx)
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

def preprocessSinglePlSqlFileForDatasetRunning(dataFileName, specFileName, dataFilePath, specFilePath):
    f = open(dataFilePath, 'r')
    linesOfCode = len(f.readlines())
    f.close()
    processor = McPreProcessor(specFilePath, dataFilePath)
    tableInfo, predicates, rawPredicateContent, predicateVarSet, resultString = processor.start()
    timeTaken = execute(tableInfo, predicates, rawPredicateContent, predicateVarSet, resultString, dataFileName, specFileName)
    return linesOfCode, timeTaken

def preprocessSinglePlSqlFile(dataFileName, specFileName):
    f = open("mc/data/" + dataFileName, 'r')
    linesOfCode = len(f.readlines())
    f.close()
    processor = McPreProcessor("mc/spec/" + specFileName, "mc/data/" + dataFileName)
    tableInfo, predicates, rawPredicateContent, predicateVarSet, resultString = processor.start()
    timeTaken = execute(tableInfo, predicates, rawPredicateContent, predicateVarSet, resultString, dataFileName, specFileName)
    return linesOfCode, timeTaken

def execute(tableInfo, predicates, rawPredicateContent, predicateVarSet, resultString, dataFileName, specFileName):
    file = open('mc/upper_input.sql', "w")
    file.write(resultString)
    file.close()

    # recording startTime1
    startTime1 = datetime.datetime.now()

    input = FileStream('mc/upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()

    cfg = MyCFG()
    helper = MyHelper(parser)
    helper.updateTableDict(tableInfo)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)

    # print("\n--- Raw CFG >>>\t", v.rawCFG, "\n")

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()


    mcCfg = MyCFG()
    for nodeId in cfg.nodes:
        tempNode = copyNode(cfg.nodes[nodeId])
        mcCfg.nodes[nodeId] = tempNode

    utility.generateVariableSet(mcCfg)
    ssaString = MySsaStringGenerator(mcCfg, parser)
    wpcObj = WpcGenerator(mcCfg, helper, ssaString)
    mcUtility = McUtility(mcCfg, wpcObj, predicateVarSet)
    # print("mc graph------------->")
    # for nodeId in mcCfg.nodes:
    #     mcCfg.nodes[nodeId].printPretty()

    for i in mcCfg.nodes:
        if mcCfg.nodes[i].ctx is not None:
            print(i, mcCfg.nodes[i].ctx.getText())
        else:
            print(i, "ctx = None")
    print("\n++++++++++++++++++++++\tPredicates Given in SPEC file:")
    for i in predicates:
        print(i)
    print("++++++++++++++++++++++\n")
    # mcCfg.dotToPng(cfg.dotGraph, "mc/raw_graph")

    mcExecutor = McExecutor()

    # recording endTime1
    endTime1 = datetime.datetime.now()

    pwd = os.getcwd()
    pwd = pwd + "/"
    sePathsInfoForMc = SePathsInfoForMc()
    sePathList, seSatInfoList = sePathsInfoForMc.execute(dataFileName, specFileName, pwd)
    print("sePathList", sePathList)
    print("seSatInfoList", seSatInfoList)
    # paths = []
    # mcExecutor.getAllPaths(mcCfg, 0, [], paths)
    # print(paths)

    # recording startTime2
    startTime2 = datetime.datetime.now()
    print("********CDCDCDCDCDCDCDCD******** Entered into McExcuter ********CDCDCDCDCDCDCDCD********")
    mcExecutor.execute(mcUtility, predicates, rawPredicateContent, sePathList, seSatInfoList, tableInfo)
    print("********CDCDCDCDCDCDCDCD******** Exited from McExcuter ********CDCDCDCDCDCDCDCD********\n")
    # recording endTime2
    endTime2 = datetime.datetime.now()

    timeForMcExcludingSe = ((endTime1 - startTime1) + (endTime2 - startTime2)).total_seconds()

    return timeForMcExcludingSe






def main(argv):
    if len(argv) < 3:
        print("Not Enough Arguments. Exiting...")
    elif len(argv) == 3:        # python3 simulator_mc.py <data-file-name> <spec-file-name>
        dataFileName = argv[1]    # given data-file must be +nt in "mc/data/"
        specFileName = argv[2]    # given spec-file must be +nt in "mc/spec/"
        linesOfCode, timeTaken = preprocessSinglePlSqlFile(dataFileName, specFileName)
        print("XXXXXXXXXXXXXXXXXXXXXXX Completed Execution for...")
        print(" Filename:", dataFileName)
        print(" Lines of Code:", linesOfCode)
        print(" Execution Time:", timeTaken)
    elif len(argv) == 6:        # see dataset_runner_mc.py
        if argv[3] == "-data_spec_filepaths":
            print("\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Running for filename :", argv[1], "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TLTLTLTLTLTL@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
            linesOfCode, timeTaken = preprocessSinglePlSqlFileForDatasetRunning(argv[1], argv[2], argv[4], argv[5])
            print("XXXXXXXXXXXXXXXXXXXXXXX Completed Execution for...")
            print(" Filename:", argv[1])
            print(" Lines of Code:", linesOfCode)
            print(" Execution Time:", timeTaken)


if __name__ == '__main__':
    main(sys.argv)

