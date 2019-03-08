# This file was generated at runtime on 2019-03-08 19:03:11.757207
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		B = Real('B')
		A = Real('A')
		Z = Real('Z')
		Y = Real('Y')
		X = Real('X')
		C = Real('C')
		D = Real('D')

		s = Solver()
		s.add(C > 0)
		s.add( Not( Implies( C > 0, Or( And( B == 50, ( A * ( Z - 2 ) ) > 0 ), And( Not( B == 50 ), ( Y * ( Z - 2 ) ) > 0 ) ) ) ) )

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
