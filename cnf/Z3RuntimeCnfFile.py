# This file was generated at runtime on 2019-03-07 01:22:50.122979
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		D1 = Real('D1')
		D2 = Real('D2')
		A0 = Real('A0')
		A3 = Real('A3')
		B0 = Real('B0')
		X1 = Real('X1')
		C3 = Real('C3')
		D0 = Real('D0')
		A2 = Real('A2')
		X0 = Real('X0')
		Z1 = Real('Z1')
		B2 = Real('B2')
		X2 = Real('X2')
		C2 = Real('C2')
		B1 = Real('B1')
		D3 = Real('D3')
		B3 = Real('B3')
		C0 = Real('C0')
		C1 = Real('C1')
		Y0 = Real('Y0')
		A1 = Real('A1')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( And( And( And( C0 + D0 < 0, A0 > 0 ), B0 > 0 ), C0 > 0 ), D0 > 0 ) ))
		s.add(True)
		s.add(Implies( True, ( X1 ) == ( X0 - 36 ) ))
		s.add(True)
		s.add(Implies( True, And( ( X2 ) == ( A0 ), A0 == X1 + 3 ) ))
		s.add(True)
		s.add(Implies( True, And( ( Z1 ) == ( B0 ), A0 == X1 + 3 ) ))
		s.add(True)
		s.add(Implies( True, ( A1 ) == ( X2 + 5 ) ))
		s.add(True)
		s.add(Implies( True, ( B1 ) == ( Y0 - 5 ) ))
		s.add(True)
		s.add(Implies( True, Or( And( And( ( A3 ) == ( A2 * ( X2 - 9 * ( Y0 - 3 ) ) ), ( B3 ) == ( Y0 - 9 ) ), And( A2 > 10, B2 <= ( X2 + Y0 ) - 50 ) ), And( Not( And( A2 > 10, B2 <= ( X2 + Y0 ) - 50 ) ), And( ( A3 ) == ( A2 ), ( B3 ) == ( B2 ) ) ) ) ))
		s.add( Not( And( Implies( True, And( And( And( And( C0 + D0 < 0, A0 > 0 ), B0 > 0 ), C0 > 0 ), D0 > 0 ) ), And( Implies( True, ( X1 ) == ( X0 - 36 ) ), And( Implies( True, And( ( X2 ) == ( A0 ), A0 == X1 + 3 ) ), And( Implies( True, And( ( Z1 ) == ( B0 ), A0 == X1 + 3 ) ), And( Implies( True, ( A1 ) == ( X2 + 5 ) ), And( Implies( True, ( B1 ) == ( Y0 - 5 ) ), And( Implies( True, Or( And( And( ( A3 ) == ( A2 * ( X2 - 9 * ( Y0 - 3 ) ) ), ( B3 ) == ( Y0 - 9 ) ), And( A2 > 10, B2 <= ( X2 + Y0 ) - 50 ) ), And( Not( And( A2 > 10, B2 <= ( X2 + Y0 ) - 50 ) ), And( ( A3 ) == ( A2 ), ( B3 ) == ( B2 ) ) ) ) ), And( And( And( C3 + D3 < 0, A3 > 0 ), B3 > 0 ), D3 > 0 ) ) ) ) ) ) ) ) ) )

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
