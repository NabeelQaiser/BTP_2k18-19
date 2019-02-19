# This file was generated at runtime 
from z3 import *

Y0 = Real('Y0')
A2 = Real('A2')
C0 = Real('C0')
X1 = Real('X1')
B0 = Real('B0')
A0 = Real('A0')
B2 = Real('B2')
C1 = Real('C1')
D3 = Real('D3')
A3 = Real('A3')
X0 = Real('X0')
C2 = Real('C2')
D1 = Real('D1')
K1 = Real('K1')
B1 = Real('B1')
A1 = Real('A1')
D2 = Real('D2')
C3 = Real('C3')
B3 = Real('B3')
D0 = Real('D0')

s = Solver()
s.add(True)
s.add(Implies( True, And( And( And( And( C0 + D0 < 0, A0 > 0 ), B0 > 0 ), C0 > 0 ), D0 > 0 ) ))
s.add(True)
s.add(Implies( True, ( X1 ) == ( X0 - 50 ) ))
s.add(True)
s.add(Implies( True, And( ( A0 ) == ( K1 ), And( A0 == X1 + 3, B0 == X1 - 3 ) ) ))
s.add(True)
s.add(Implies( True, ( A1 ) == ( X1 + 5 ) ))
s.add(True)
s.add(Implies( True, ( B1 ) == ( Y0 - 5 ) ))
s.add(True)
s.add(Implies( True, Or( And( ( A3 ) == ( X1 - 9 ), A2 > 10 ), And( Not( A2 > 10 ), ( A3 ) == ( A2 ) ) ) ))
s.add( Not( And( Implies( True, And( And( And( And( C0 + D0 < 0, A0 > 0 ), B0 > 0 ), C0 > 0 ), D0 > 0 ) ), And( Implies( True, ( X1 ) == ( X0 - 50 ) ), And( Implies( True, And( ( A0 ) == ( K1 ), And( A0 == X1 + 3, B0 == X1 - 3 ) ) ), And( Implies( True, ( A1 ) == ( X1 + 5 ) ), And( Implies( True, ( B1 ) == ( Y0 - 5 ) ), And( Implies( True, Or( And( ( A3 ) == ( X1 - 9 ), A2 > 10 ), And( Not( A2 > 10 ), ( A3 ) == ( A2 ) ) ) ), And( And( And( And( C3 + D3 < 0, A3 > 0 ), B3 > 0 ), C3 > 0 ), D3 > 0 ) ) ) ) ) ) ) ) )

print()

print("------------------------------------------------------------------\nRunning script in /wpc/z3FormatWpcFile.py ....\n")

print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)

print()
print("%%%%%%%%%% Satisfiability %%%%%%%%%%\n", s.check())

print()
print("%%%%%%%%%% Satisfiable Model %%%%%%%%%%\n", s.model())

print()
