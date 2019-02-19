# This file was generated at runtime on 2019-02-19 14:02:04.770129
from z3 import *

X = Real('X')
P = Real('P')
Y = Real('Y')
A = Real('A')
D = Real('D')
B = Real('B')
Q = Real('Q')
C = Real('C')
R = Real('R')

s = Solver()
s.add(And( And( A + P >= 50, C + D == 100 ), Q + R < 54 ))
s.add( Not( Implies( And( And( A + P >= 50, C + D == 100 ), Q + R < 54 ), Or( And( And( A == ( X - 50 ) + 3, B == ( X - 50 ) - 3 ), Or( And( ( ( X - 50 ) + 5 ) > 10, And( And( ( ( X - 50 ) - 9 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ), And( Not( ( ( X - 50 ) + 5 ) > 10 ), And( And( ( ( X - 50 ) + 5 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ) ) ), And( Not( And( A == ( X - 50 ) + 3, B == ( X - 50 ) - 3 ) ), Or( And( ( ( X - 50 ) + 5 ) > 10, And( And( ( ( X - 50 ) - 9 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ), And( Not( ( ( X - 50 ) + 5 ) > 10 ), And( And( ( ( X - 50 ) + 5 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ) ) ) ) ) ) )

print()

print("------------------------------------------------------------------\nRunning script in /wpc/z3FormatWpcFile.py ....\n")

print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)

print()
print("%%%%%%%%%% Satisfiability %%%%%%%%%%\n", s.check())

print()
print("%%%%%%%%%% Satisfiable Model %%%%%%%%%%\n", s.model())

print()
