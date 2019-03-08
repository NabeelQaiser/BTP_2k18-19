# This file was generated at runtime on 2019-03-09 05:07:58.473715
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		D = Real('D')
		B3 = Real('B3')
		A2 = Real('A2')
		C = Real('C')
		B = Real('B')
		A = Real('A')
		M = Real('M')

		s = Solver()
		s.add(A > 0)
		s.add(Implies( A > 0, A > 0 ))
		s.add(A > 0)
		s.add(Implies( A > 0, A > 0 ))
		s.add( Not( Or( And( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ), Implies( A > 0, A > 0 ) ), And( Not( And( And( B == B2, C2 == C3 ), And( A2 >= M + 5, C < 99 ) ) ), Implies( A > 0, A > 0 ) ) ) ) )

		print()
		print("%%%%%%%%%% Aggregate Formula %%%%%%%%%%\n", s)
		self.finalFormula = str(s)
		print()
		print("%%%%%%%%%% Satisfiability %%%%%%%%%%")

		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			print()
			print("-------->> Violation Occurred...")
			self.satisfiability = "Unsatisfiable"
			print()
			print("%%%%%%%%%% An Instance for which Violation Occurred %%%%%%%%%%\n", s.model())
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			print()
			print("-------->> NO Violation Detected so far...")
			self.satisfiability = "Satisfiable"
			print()
		print()
