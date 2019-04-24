# This file was generated at runtime on 2019-04-24 21:04:09.937886
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		PRICE = Real('PRICE')
		NUM_ITEM = Real('NUM_ITEM')
		ITEM_ID = Real('ITEM_ID')
		ITEM_COUNT = Real('ITEM_COUNT')
		NO_OF_ITEM = Real('NO_OF_ITEM')
		ITEM_PRICE = Real('ITEM_PRICE')
		ID = Real('ID')

		s = Solver()
		s.add(And( NO_OF_ITEM > 0, ITEM_PRICE > 0 ))
		s.add( Not( Implies( And( NO_OF_ITEM > 0, ITEM_PRICE > 0 ), Or( And( ITEM_ID == ID, Or( And( NUM_ITEM >= 1000, ( ITEM_PRICE - 0.1 * NUM_ITEM ) > 0 ), And( Not( NUM_ITEM >= 1000 ), Or( And( NUM_ITEM >= 500, ( ITEM_PRICE - 0.2 * NUM_ITEM ) > 0 ), And( Not( NUM_ITEM >= 500 ), Or( And( And( NUM_ITEM > 99, ITEM_PRICE > 5000 ), ( ITEM_PRICE - 0.2 * NUM_ITEM ) > 0 ), And( Not( And( NUM_ITEM > 99, ITEM_PRICE > 5000 ) ), ( ITEM_PRICE + 0.05 * NUM_ITEM ) > 0 ) ) ) ) ) ) ), And( Not( ITEM_ID == ID ), Or( And( NUM_ITEM >= 1000, ( PRICE - 0.1 * NUM_ITEM ) > 0 ), And( Not( NUM_ITEM >= 1000 ), Or( And( NUM_ITEM >= 500, ( PRICE - 0.2 * NUM_ITEM ) > 0 ), And( Not( NUM_ITEM >= 500 ), Or( And( And( NUM_ITEM > 99, PRICE > 5000 ), ( PRICE - 0.2 * NUM_ITEM ) > 0 ), And( Not( And( NUM_ITEM > 99, PRICE > 5000 ) ), ( PRICE + 0.05 * NUM_ITEM ) > 0 ) ) ) ) ) ) ) ) ) ) )

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