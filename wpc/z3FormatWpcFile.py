# This file was generated at runtime on 2019-02-08 06:45:35.763038
from z3 import *

B = Real('B')
A = Real('A')
X = Real('X')
Y = Real('Y')
HELLO = Real('HELLO')

s = Solver()
s.add(A + X > 12)
s.add(Implies( A + X > 12, Or( And( And( Not( A > 10 ), ( HELLO ) <= ( X + Y ) - 50 ), ( A * ( X - 9 * ( Y - 3 ) ) ) > 0 ), And( Not( And( Not( A > 10 ), ( HELLO ) <= ( X + Y ) - 50 ) ), A > 0 ) ) ))

print()

print("------------------------------------------------------------------\nRunning script in /wpc/z3FormatWpcFile.py ....\n")

print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)

print()
print("%%%%%%%%%% Satisfiability %%%%%%%%%%\n", s.check())

print()
print("%%%%%%%%%% Satisfiable Model %%%%%%%%%%\n", s.model())

print()
