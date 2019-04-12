import sys
from MyHelper import MyHelper
from gen.PlSqlVisitor import PlSqlVisitor

global varSet
varSet = list()

class z3formulaofvcs(PlSqlVisitor):
    def __init__(self, cfg, parser):
        self.cfg = cfg
        self.parser = parser
        self.helper = MyHelper(self.parser)


    def z3VariableDeclarationSet(self, path):
        global varSet
        for i in range(len(path)):
            node = path[i]
            if self.cfg.nodes[node].versionedRHS:
                for element in self.cfg.nodes[node].versionedRHS:
                    values = self.cfg.nodes[node].versionedRHS[element]
                    if values not in varSet:
                        varSet.append(values)



            if self.cfg.nodes[node].versionedLHS:
                for element in self.cfg.nodes[node].versionedLHS:
                    values = self.cfg.nodes[node].versionedLHS[element]
                    if values not in varSet:
                        varSet.append(values)


            if  self.cfg.nodes[node].destructedPhi:
                    #print(context)
                    for element in self.cfg.nodes[node].destructedPhi:
                        values = self.cfg.nodes[node].destructedPhi[element]
                        for i in range(len(values)):
                            if values[i] not in varSet:
                                varSet.append(values[i])




        return varSet

    @staticmethod
    def anticedent_position(x):
        l = []
        for index,bracket in enumerate(x):
            if bracket == '(':
                l.append(bracket)
            else:
                if bracket == ')':
                    l.pop();
                    if(len(l)==0):
                        return index+1


    
    def z3FormulaForEachPath(self, vc, pwd):
        global varSet
        y = list(map(lambda k: k+" = Real('"+k+"')\n", varSet))
        position = self.anticedent_position(vc[8:]);
        with open(pwd + 'SeAPI/z3formula.py', 'w') as outfile:
            outfile.writelines("from z3 import *\n")
            outfile.writelines(y)
            outfile.writelines("s = Solver()\n")
            outfile.writelines("s.add("+vc[8:position+8]+")\n")
            outfile.writelines("s.add(Not("+vc+"))\n")
            outfile.writelines("r = s.check()\n")
            outfile.writelines("if str(r) == \"unsat\":\n")
            outfile.writelines("    print(\"looksgood\")\n")
            outfile.writelines("else:\n")
            outfile.writelines("    print(\"cannotsay\")\n")
            

    

