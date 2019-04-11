import sys
from inspect import signature
from antlr4 import *
from SeAPI.gen.PlSqlLexer import PlSqlLexer
from SeAPI.gen.PlSqlParser import PlSqlParser


def main(argv):
    name = "gen/data/"+argv[1]
    file = open(name, "r")
    content = file.read().upper()
    file.close()
    file = open('upper_input.sql', "w")
    file.write(content)
    file.close()

    input = FileStream('upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()
    ast = tree.toStringTree(recog=parser)
    #print("\n\n", signature(tree.toStringTree), "\n")
    print(ast, "\n\n")


    # file = open('ggg.md', 'w')
    # file.write(ast)
    # file.close()


if __name__ == '__main__':
    main(sys.argv)
