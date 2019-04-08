from z3 import *

allVar = {"A", "B", "C", "D"}
# exec("%s" % ("print('mkc bkl')"))
# print(a)
for i in allVar:
    exec("%s=%s" % (i, "Real(\'" + i + "\')"))
# print(C)
#
# A = Real('A')
# B = Real('B')
z3SolverObj = Solver()
#
s1 = "A>10"
s2 = "Implies(A>10, A>20)"
#
exec("%s" % ("z3SolverObj.add(" + s1 + ")"))
exec("%s" % ("z3SolverObj.add(" + s2 + ")"))
# z3SolverObj.add(s1)
# z3SolverObj.add(s2)
#

# z3SolverObj.add(A>10)
# z3SolverObj.add(Implies(A>10, A>20))
print(z3SolverObj)
print(z3SolverObj.check())