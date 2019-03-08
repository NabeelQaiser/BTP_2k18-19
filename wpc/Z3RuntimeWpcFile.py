# This file was generated at runtime on 2019-03-09 01:31:06.937520
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		PRICE = Real('PRICE')
		Y = Real('Y')
		BIG_DISCOUNT = Real('BIG_DISCOUNT')
		CUSTOMER_ID = Real('CUSTOMER_ID')
		SYSDATE = Real('SYSDATE')
		LOW_DISCOUNT = Real('LOW_DISCOUNT')
		START_TIME = Real('START_TIME')
		WRONG_DISCOUNT = Real('WRONG_DISCOUNT')
		SUM_WEIGHT = Real('SUM_WEIGHT')
		X = Real('X')
		WEIGHT = Real('WEIGHT')
		LOAD_ID = Real('LOAD_ID')

		s = Solver()
		s.add(And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ))
		s.add( Not( Implies( And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ), Or( And( Or( X == Y, And( And( LOAD_ID == 5, START_TIME >= SYSDATE ), START_TIME <= SYSDATE + 7 ) ), And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ) ), And( Not( Or( X == Y, And( And( LOAD_ID == 5, START_TIME >= SYSDATE ), START_TIME <= SYSDATE + 7 ) ) ), And( And( And( And( BIG_DISCOUNT >= 0, LOW_DISCOUNT >= 0 ), WRONG_DISCOUNT >= 0 ), PRICE > 0 ), SYSDATE > 0 ) ) ) ) ) )

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
