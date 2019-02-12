# This file was generated at runtime on 2019-02-12 16:21:09.531502
from z3 import *

Y = Real('Y')
ID = Real('ID')
C = Real('C')
Z = Real('Z')
A = Real('A')
B = Real('B')
X = Real('X')

s = Solver()
s.add(Z + Y > 10)
s.add(Implies( Z + Y > 10, Or( And( ( B ) > A, ( ( B ) + 5 ) - ( ( B ) - 5 ) + ( A * ( Z - 2 ) ) > 0 ), And( Not( ( B ) > A ), Or( And( ( B ) < A, ( ( B ) + 5 ) - ( ( B ) - 5 ) + ( A * ( Z - 2 ) ) > 0 ), And( Not( ( B ) < A ), Or( And( And( ( ( B ) + 5 ) > 10, ( ( B ) - 5 ) <= ( ( ( B ) + 40 ) + A ) - 50 ), ( ( ( B ) + 5 ) * ( ( ( B ) + 40 ) - 9 * ( A - 3 ) ) ) - ( A - 9 ) + ( A * ( Z - 2 ) ) > 0 ), And( Not( And( ( ( B ) + 5 ) > 10, ( ( B ) - 5 ) <= ( ( ( B ) + 40 ) + A ) - 50 ) ), ( ( B ) + 5 ) - ( ( B ) - 5 ) + ( A * ( Z - 2 ) ) > 0 ) ) ) ) ) ) ))

print()

print("------------------------------------------------------------------\nRunning script in /wpc/z3FormatWpcFile.py ....\n")

print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)

print()
print("%%%%%%%%%% Satisfiability %%%%%%%%%%\n", s.check())

print()
print("%%%%%%%%%% Satisfiable Model %%%%%%%%%%\n", s.model())

print()
