# This file was generated at runtime on 2019-04-21 22:05:23.521207
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		R = Real('R')
		B = Real('B')
		Y = Real('Y')
		Q = Real('Q')
		D = Real('D')
		X = Real('X')
		A = Real('A')
		C = Real('C')
		P = Real('P')

		s = Solver()
		s.add(And( And( A + P >= 50, C + D == 100 ), Q + R < 54 ))
		s.add( Not( Implies( And( And( A + P >= 50, C + D == 100 ), Q + R < 54 ), Or( And( And( A == ( X - 50 ) + 3, B == ( X - 50 ) - 3 ), Or( And( ( ( X - 50 ) + 5 ) > 10, And( And( ( ( X - 50 ) - 9 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ), And( Not( ( ( X - 50 ) + 5 ) > 10 ), And( And( ( ( X - 50 ) + 5 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ) ) ), And( Not( And( A == ( X - 50 ) + 3, B == ( X - 50 ) - 3 ) ), Or( And( ( ( X - 50 ) + 5 ) > 10, And( And( ( ( X - 50 ) - 9 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ), And( Not( ( ( X - 50 ) + 5 ) > 10 ), And( And( ( ( X - 50 ) + 5 ) + P >= 50, C + D == 100 ), Q + R < 54 ) ) ) ) ) ) ) )

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