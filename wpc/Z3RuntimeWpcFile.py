# This file was generated at runtime on 2019-05-03 06:07:36.148378
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		PRICE = Real('PRICE')
		AMOUNT = Real('AMOUNT')
		ID = Real('ID')
		T_PRICE = Real('T_PRICE')
		T_ID = Real('T_ID')

		s = Solver()
		s.add(And( And( AMOUNT > 0, T_PRICE > 0 ), PRICE > 0 ))
		s.add( Not( Implies( And( And( AMOUNT > 0, T_PRICE > 0 ), PRICE > 0 ), Or( And( T_ID == ID, Or( And( AMOUNT >= 1000, ( T_PRICE - 0.1 * AMOUNT ) > 0 ), And( Not( AMOUNT >= 1000 ), Or( And( And( AMOUNT >= 200, T_PRICE > 5000 ), ( T_PRICE - 0.2 * AMOUNT ) > 0 ), And( Not( And( AMOUNT >= 200, T_PRICE > 5000 ) ), ( T_PRICE + 0.05 * AMOUNT ) > 0 ) ) ) ) ), And( Not( T_ID == ID ), Or( And( AMOUNT >= 1000, ( PRICE - 0.1 * AMOUNT ) > 0 ), And( Not( AMOUNT >= 1000 ), Or( And( And( AMOUNT >= 200, PRICE > 5000 ), ( PRICE - 0.2 * AMOUNT ) > 0 ), And( Not( And( AMOUNT >= 200, PRICE > 5000 ) ), ( PRICE + 0.05 * AMOUNT ) > 0 ) ) ) ) ) ) ) ) )

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