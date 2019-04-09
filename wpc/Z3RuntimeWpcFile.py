# This file was generated at runtime on 2019-04-09 22:32:16.945494
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		MY_MAX = Real('MY_MAX')
		M = Real('M')
		B3 = Real('B3')
		MAX_B3 = Real('MAX_B3')
		D = Real('D')
		MAX_A = Real('MAX_A')
		D3 = Real('D3')
		G = Real('G')
		B = Real('B')
		A = Real('A')
		C = Real('C')
		T2 = Real('T2')
		A2 = Real('A2')
		A3 = Real('A3')
		C2 = Real('C2')
		C3 = Real('C3')
		AVG_A2 = Real('AVG_A2')
		Y = Real('Y')
		D2 = Real('D2')
		B2 = Real('B2')
		X = Real('X')

		s = Solver()
		s.add(And( A > 15, A3 > 15 ))
		s.add(Implies( And( A > 15, A3 > 15 ), Or( And( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ), Or( And( ( MAX_A ) > MAX_B3, Or( And( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ), And( A > 0, ( A3 * ( AVG_A2 - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) > MAX_B3 ), Or( And( ( MAX_A ) < MAX_B3, Or( And( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ), And( ( A * ( AVG_A2 - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) < MAX_B3 ), And( ( ( MAX_A ) - AVG_A2 ) > 0, A3 > 10 ) ) ) ) ) ), And( Not( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ) ), Or( And( ( MAX_A ) > Y, Or( And( And( A3 > 10, B3 <= ( X + Y ) ), And( A > 0, ( A3 * ( X - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) > Y ), Or( And( ( MAX_A ) < Y, Or( And( And( A > 10, B <= ( X + Y ) ), And( ( A * ( X - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) < Y ), And( ( ( MAX_A ) - X ) > 0, A3 > 10 ) ) ) ) ) ) ) ))
		s.add(And( A > 15, A3 > 15 ))
		s.add(Implies( And( A > 15, A3 > 15 ), Or( And( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ), Or( And( ( G ) > MAX_B3, Or( And( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ), And( A > 0, ( A3 * ( AVG_A2 - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) > MAX_B3 ), Or( And( ( G ) < MAX_B3, Or( And( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ), And( ( A * ( AVG_A2 - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) < MAX_B3 ), And( ( ( G ) - AVG_A2 ) > 0, A3 > 10 ) ) ) ) ) ), And( Not( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ) ), Or( And( ( G ) > Y, Or( And( And( A3 > 10, B3 <= ( X + Y ) ), And( A > 0, ( A3 * ( X - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) > Y ), Or( And( ( G ) < Y, Or( And( And( A > 10, B <= ( X + Y ) ), And( ( A * ( X - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) < Y ), And( ( ( G ) - X ) > 0, A3 > 10 ) ) ) ) ) ) ) ))
		s.add( Not( Or( And( And( A >= M + 5, And( C == C2, B2 >= 50 ) ), Implies( And( A > 15, A3 > 15 ), Or( And( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ), Or( And( ( MAX_A ) > MAX_B3, Or( And( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ), And( A > 0, ( A3 * ( AVG_A2 - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) > MAX_B3 ), Or( And( ( MAX_A ) < MAX_B3, Or( And( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ), And( ( A * ( AVG_A2 - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) < MAX_B3 ), And( ( ( MAX_A ) - AVG_A2 ) > 0, A3 > 10 ) ) ) ) ) ), And( Not( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ) ), Or( And( ( MAX_A ) > Y, Or( And( And( A3 > 10, B3 <= ( X + Y ) ), And( A > 0, ( A3 * ( X - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) > Y ), Or( And( ( MAX_A ) < Y, Or( And( And( A > 10, B <= ( X + Y ) ), And( ( A * ( X - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( MAX_A ) < Y ), And( ( ( MAX_A ) - X ) > 0, A3 > 10 ) ) ) ) ) ) ) ) ), And( Not( And( A >= M + 5, And( C == C2, B2 >= 50 ) ) ), Implies( And( A > 15, A3 > 15 ), Or( And( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ), Or( And( ( G ) > MAX_B3, Or( And( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ), And( A > 0, ( A3 * ( AVG_A2 - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) > MAX_B3 ), Or( And( ( G ) < MAX_B3, Or( And( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ), And( ( A * ( AVG_A2 - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( AVG_A2 + MAX_B3 ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) < MAX_B3 ), And( ( ( G ) - AVG_A2 ) > 0, A3 > 10 ) ) ) ) ) ), And( Not( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ) ), Or( And( ( G ) > Y, Or( And( And( A3 > 10, B3 <= ( X + Y ) ), And( A > 0, ( A3 * ( X - 9 ) ) > 10 ) ), And( Not( And( A3 > 10, B3 <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) > Y ), Or( And( ( G ) < Y, Or( And( And( A > 10, B <= ( X + Y ) ), And( ( A * ( X - 9 ) ) > 0, A3 > 10 ) ), And( Not( And( A > 10, B <= ( X + Y ) ) ), And( A > 0, A3 > 10 ) ) ) ), And( Not( ( G ) < Y ), And( ( ( G ) - X ) > 0, A3 > 10 ) ) ) ) ) ) ) ) ) ) ) )

		#print("\n%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)
		self.finalFormula = str(s)
		#print("\n%%%%%%%%%% Satisfiability %%%%%%%%%%")

		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			#print("\n-------->> Violation Occurred...")
			self.satisfiability = "violation"
			#print("\n%%%%%%%%%% An Instance for which Violation Occurred %%%%%%%%%%\n", s.model())
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			#print("\n-------->> NO Violation Detected so far...\n")
			self.satisfiability = "sat"