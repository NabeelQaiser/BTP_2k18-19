import sys
import datetime
from subprocess import call

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyRawCfgToGraph import MyRawCfgToGraph
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from WpcGenerator import WpcGenerator
from WpcStringConverter import WpcStringConverter
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser


def main(argv):
    name = "wpc/data/" + argv[1]
    file = open(name, "r")
    content = file.read().upper()
    file.close()
    file = open('wpc/upper_input.sql', "w")
    file.write(content)
    file.close()

    input = FileStream('wpc/upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()

    cfg = MyCFG()
    helper = MyHelper(parser)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)

    print(v.rawCFG, "\n")

    for key in v.cfg.nodes:
        if v.cfg.nodes[key].ctx != None:
            print(key, " --> ", v.cfg.nodes[key].ctx.getText())
    print("\n")

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    print("\n")

    cfg.dotToPng(cfg.dotGraph, "wpc/raw_graph")
    utility.generateVariableSet(cfg)

    # all properties of each node
    for nodeId in cfg.nodes:
        cfg.nodes[nodeId].printPretty()


    ssaString = MySsaStringGenerator(cfg, parser)
    # ssaString.execute()


    algo = WpcGenerator(cfg, helper, ssaString)
    algo.execute()
    algo.finalWpcString = algo.finalWpcString.replace("  ", " ")
    # done: replace " = " with " == " in algo.finalWpcString
    algo.finalWpcString = algo.finalWpcString.replace(" = ", " == ")

    print("\n**** Final WPC String:\n", algo.finalWpcString, "\n")

    # print(algo.variablesForZ3)

    # algo.finalWpcString = "( ( z ) ^ ( ( ! ( y ) ) ==> ( ( ( 2 ) v ( x ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( ( ( true ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( true ) ) ^ ( ( a ) ==> ( b ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ==> ( true ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ^ ( true ) v ( g ) ) )"       # for testing! Don't UNCOMMENT...
    z3StringConvertor = WpcStringConverter(algo.finalWpcString)
    z3StringConvertor.execute()
    print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")

    z3FileString = "# This file was generated at runtime on " + str(datetime.datetime.now()) + "\n"
    z3FileString = z3FileString + "from z3 import *\n\n"
    for i in algo.variablesForZ3:
        z3FileString = z3FileString + i + " = Real(\'" + i + "\')\n"
    z3FileString = z3FileString + "\ns = Solver()\n"

    if len(z3StringConvertor.implies_p) > 0:
        for i in range(len(z3StringConvertor.implies_p)):
            z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p[i] + ")\n"
            if not z3StringConvertor.convertedWpc == z3StringConvertor.implies_p_q[i]:
                z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p_q[i] + ")\n"
    #     if z3StringConvertor.convertedWpc not in z3StringConvertor.implies_p_q:
    #         z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    # else:
    #     z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    z3FileString = z3FileString + "s.add( Not( " + z3StringConvertor.convertedWpc + " ) )\n"

    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "\nprint(\"------------------------------------------------------------------\\nRunning script in /wpc/z3FormatWpcFile.py ....\\n\")\n"
    z3FileString = z3FileString + "\nprint(\"%%%%%%%%%% Aggregate Formula %%%%%%%%%%\\n\", s)\n"
    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiability %%%%%%%%%%\\n\", s.check())\n"
    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiable Model %%%%%%%%%%\\n\", s.model())\n"
    z3FileString = z3FileString + "\nprint()\n"

    file = open('wpc/z3FormatWpcFile.py', "w")
    file.write(z3FileString)
    file.close()

    # call(["python3", "wpc/z3FormatWpcFile.py"])




if __name__ == '__main__':
    main(sys.argv)


# TODO notes:
