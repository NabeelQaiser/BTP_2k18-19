import sys
from inspect import signature
from antlr4 import *
from SeAPI.gen.PlSqlLexer import PlSqlLexer
from SeAPI.gen.PlSqlParser import PlSqlParser
from SeAPI.gen.PlSqlVisitor import PlSqlVisitor

class MyPlSqlVisitor(PlSqlVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.varDict = {}

    def visitSql_script(self, ctx):
        #print(ctx, "\n\n\n\n")
        for i in range(ctx.getChildCount()-1):
            if(ctx.children[i].getChildCount()>0):
                self.visit(ctx.children[i])
            else:
                self.getTerminal(ctx.children[i])
                print()

    def visitCreate_procedure_body(self, ctx):
        #print(ctx, "\n\n\n\n")
        for i in range(ctx.getChildCount()):
            if(ctx.children[i].getChildCount()>0):
                self.visit(ctx.children[i])
            else:
                self.getTerminal(ctx.children[i])

    def visitBody(self, ctx):
        for i in range(ctx.getChildCount()):
            if(ctx.children[i].getChildCount()>0):
                print()
                self.visit(ctx.children[i])
            else:
                print()
                self.getTerminal(ctx.children[i])

    def visitSeq_of_statements(self, ctx):
        for i in range(ctx.getChildCount()):
            if(ctx.children[i].getChildCount()>0):
                self.visit(ctx.children[i])
            else:
                self.getTerminal(ctx.children[i])

    def visitProcedure_name(self, ctx):
        #print(ctx.getText(), "\n\n\n\n")
        self.getTerminal(ctx)
        #print()

    def visitParameter(self, ctx):
        #print(ctx.getText(), "\n\n\n\n")
        self.getTerminal(ctx.children[0], True, False)
        self.getTerminal(ctx.children[1], False, False)
        self.getTerminal(ctx.children[2], False, False)
        #print()

    def visitDeclare_spec(self, ctx):
        self.visit(ctx.children[0])
        #print()
        #self.getTerminal(ctx)

    def visitVariable_declaration(self, ctx):
        print()
        self.getTerminal(ctx.children[0], True, False)
        self.getTerminal(ctx.children[1], False, False)
        self.getTerminal(ctx.children[2], False, False)

    def visitCursor_declaration(self, ctx):
        print()
        self.getTerminal(ctx.children[0], False, False)
        self.getTerminal(ctx.children[1], False, False)
        self.getTerminal(ctx.children[2], False, False)
        self.getTerminal(ctx.children[3], False, False)      # <--- change it
        self.getTerminal(ctx.children[4], False, False)

    def visitSql_statement(self, ctx):
        print()
        #self.getTerminal(ctx)
        self.visit(ctx.children[0])

    def visitOpen_statement(self, ctx):
        self.getTerminal(ctx.children[0], False, False)
        self.getTerminal(ctx.children[1], True, False)

    def visitFetch_statement(self, ctx):
        self.getTerminal(ctx.children[0], False, False)
        self.getTerminal(ctx.children[1], True, False)
        self.getTerminal(ctx.children[2], False, False)
        self.getTerminal(ctx.children[3], True, True)

    def visitClose_statement(self, ctx):
        self.getTerminal(ctx.children[0], False, False)
        self.getTerminal(ctx.children[1], True, False)

    def visitInsert_statement(self, ctx):
        self.getTerminal(ctx.children[0], False, False)
        self.getTerminal(ctx.children[1], False, False)      # <--- change it

    def visitIf_statement(self, ctx):
        #print(ctx.getText(), "\n\n")
        #self.getTerminal(ctx)
        print()
        self.getTerminal(ctx.children[0])
        self.getTerminal(ctx.children[1], False, False)
        self.getTerminal(ctx.children[2])
        print("\n\t", end="")
        self.getTerminal(ctx.children[3], False, True)
        print("\n", end="")
        self.getTerminal(ctx.children[4])
        self.getTerminal(ctx.children[5])



    def getTerminal(self, ctx, displayCount=False, incrCount=True):
        c = ctx.getChildCount()
        if(c==0):
            if(displayCount):
                if(self.varDict.get(str(ctx))==None):
                    self.varDict[str(ctx)] = 0
                elif (incrCount):
                    self.varDict[str(ctx)] = self.varDict[str(ctx)] + 1
                print(str(ctx)+"_#"+str(self.varDict[str(ctx)]), end=" ")
            else:
                print(str(ctx), end=" ")
        else:
            for i in range(c):

                if(self.getRuleName(ctx)=="regular_id" and displayCount==False):
                    self.getTerminal(ctx.children[i], True, incrCount)
                else:
                    self.getTerminal(ctx.children[i], displayCount, incrCount)

                # replacing comment by...
                #self.getTerminal(ctx.children[i], displayCount, incrCount)

    def getRuleName(self, ctx):
        s = str(ctx.toStringTree(recog=self.parser))
        n = len(s)
        i = 0
        while not(s[i]=='('):
            i = i+1
        j = i+1
        while not(s[j]==' '):
            j = j+1
        return s[i+1:j]





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
    #print(str(MyPlSqlVisitor(parser).getRuleName(tree)))
    #print("\n\n", signature(tree.toStringTree), "\n")

    v = MyPlSqlVisitor(parser)
    v.visit(tree)

    # file = open('ggg.md', 'w')
    # file.write(ast)
    # file.close()


if __name__ == '__main__':
    main(sys.argv)