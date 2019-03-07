# This file was generated at runtime on 2019-03-08 01:46:58.417944
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		B0 = Real('B0')
		Y0 = Real('Y0')
		A1 = Real('A1')
		B1 = Real('B1')
		A0 = Real('A0')
		A2 = Real('A2')
		B2 = Real('B2')
		X0 = Real('X0')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( A0 > 10, B0 > 10 ) ))
		s.add(X0 >= 3)
		s.add(Implies( X0 >= 3, Or( And( ( B1 ) == ( B0 - 10 ), A0 == Y0 ), And( Not( A0 == Y0 ), ( B1 ) == ( B0 ) ) ) ))
		s.add(X0 >= 3)
		s.add(Implies( X0 >= 3, A2 == A1 ))
		s.add(X0 >= 3)
		s.add(Implies( X0 >= 3, B2 == B1 ))
		s.add(Not( X0 >= 3 ))
		s.add(Implies( Not( X0 >= 3 ), A2 == A0 ))
		s.add(Not( X0 >= 3 ))
		s.add(Implies( Not( X0 >= 3 ), B2 == B0 ))
		s.add( Not( And( Implies( True, And( A0 > 10, B0 > 10 ) ), And( Implies( X0 >= 3, Or( And( ( B1 ) == ( B0 - 10 ), A0 == Y0 ), And( Not( A0 == Y0 ), ( B1 ) == ( B0 ) ) ) ), And( Implies( X0 >= 3, A2 == A1 ), And( Implies( X0 >= 3, B2 == B1 ), And( Implies( Not( X0 >= 3 ), A2 == A0 ), And( Implies( Not( X0 >= 3 ), B2 == B0 ), And( A2 > 10, B2 > 10 ) ) ) ) ) ) ) ) )

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
