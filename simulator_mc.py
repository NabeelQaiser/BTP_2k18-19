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
    tableInfo, predicates, predicateVarSet, resultString = processor.start()
    execute(tableInfo, predicates, predicateVarSet, resultString, dataFileName, specFileName)

def preprocessSinglePlSqlFile(dataFileName, specFileName):
    f = open("mc/data/" + dataFileName, 'r')
    linesOfCode = len(f.readlines())
    f.close()
    processor = McPreProcessor("mc/spec/" + specFileName, "mc/data/" + dataFileName)
    tableInfo, predicates, predicateVarSet, resultString = processor.start()
    execute(tableInfo, predicates, predicateVarSet, resultString, dataFileName, specFileName)

def execute(tableInfo, predicates, predicateVarSet, resultString, dataFileName, specFileName):
    file = open('mc/upper_input.sql', "w")
    file.write(resultString)
    file.close()

    # recording startTime
    startTime = datetime.datetime.now()

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

    print("\n++++++++++++++++++++++\tPredicates\n")
    for i in predicates:
        print(i)

    # for i in mcCfg.nodes:
    #     if mcCfg.nodes[i].ctx is not None:
    #         print(mcCfg.nodes[i].ctx.getText(), "\twpcs -->\t", mcCfg.nodes[i].wpcString, "\n")

    # mcUtility.execute(predicates)

    mcExecutor = McExecutor()

    pwd = os.getcwd()
    pwd = pwd + "/"
    sePathsInfoForMc = SePathsInfoForMc()
    sePathList, seSatInfoList = sePathsInfoForMc.execute(dataFileName, specFileName, pwd)
    print("sePathList", sePathList)
    print("seSatInfoList", seSatInfoList)
    # paths = []
    # mcExecutor.getAllPaths(mcCfg, 0, [], paths)
    # print(paths)

    print("********************************")
    mcExecutor.execute(mcUtility, predicates, sePathList, seSatInfoList)
    print("********************************\n")

    print("\n-------  booleans and wpcs  ------\n")
    for i in mcCfg.nodes:
        if mcCfg.nodes[i].ctx is not None:
            print(str(i)+".", mcCfg.nodes[i].ctx.getText(), "\nbooleans -->\t", mcCfg.nodes[i].booleans, ",\twpcs -->\t", mcCfg.nodes[i].wpcString, "\n")

    mcCfg.dotToPng(cfg.dotGraph, "mc/raw_graph")






def main(argv):
    if len(argv) < 3:
        print("Not Enough Arguments. Exiting...")
    elif len(argv) == 3:        # python3 simulator_mc.py <data-file-name> <spec-file-name>
        dataFileName = argv[1]    # given data-file must be +nt in "mc/data/"
        specFileName = argv[2]    # given spec-file must be +nt in "mc/spec/"
        preprocessSinglePlSqlFile(dataFileName, specFileName)
    elif len(argv) == 6:        # see dataset_runner_mc.py
        if argv[3] == "-data_spec_filepaths":
            print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Running for filename :", argv[1], "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            preprocessSinglePlSqlFileForDatasetRunning(argv[1], argv[2], argv[4], argv[5])


if __name__ == '__main__':
    main(sys.argv)

