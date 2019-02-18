# This file was generated at runtime on 2019-02-18 23:59:42.600761
from z3 import *

Y = Real('Y')
Z = Real('Z')
B = Real('B')
X = Real('X')
C = Real('C')
A = Real('A')

s = Solver()
s.add(Z + Y > 10)
s.add( Not( Implies( Z + Y > 10, Or( And( And( A == X + 3, IS ), A - B + C > 0 ), And( Not( And( A == X + 3, IS ) ), X - Y + Z > 0 ) ) ) ) )

print()

print("------------------------------------------------------------------\nRunning script in /wpc/z3FormatWpcFile.py ....\n")

print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)

print()
print("%%%%%%%%%% Satisfiability %%%%%%%%%%\n", s.check())

print()
print("%%%%%%%%%% Satisfiable Model %%%%%%%%%%\n", s.model())

print()
