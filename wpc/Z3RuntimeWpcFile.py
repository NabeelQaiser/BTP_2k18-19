# This file was generated at runtime on 2019-04-01 21:19:35.773198
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		BIG_DISCOUNT = Real('BIG_DISCOUNT')
		LOW_DISCOUNT = Real('LOW_DISCOUNT')
		PERCENT = Real('PERCENT')
		PRICE = Real('PRICE')
		WRONG_DISCOUNT = Real('WRONG_DISCOUNT')
		SYSDATE = Real('SYSDATE')

		s = Solver()
		s.add(And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ))
		s.add( Not( Implies( And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ), Or( And( Or( PERCENT < 0, PERCENT > 100 ), And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ) ), And( Not( Or( PERCENT < 0, PERCENT > 100 ) ), Or( And( PERCENT > 200, And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ) ), And( Not( PERCENT > 200 ), And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ) ) ) ) ) ) ) )

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