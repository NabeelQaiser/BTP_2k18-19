# This file was generated at runtime on 2019-03-09 01:58:10.153169
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		X0 = Real('X0')
		WEIGHT0 = Real('WEIGHT0')
		NOTHING1 = Real('NOTHING1')
		N_O_VISITS0 = Real('N_O_VISITS0')
		MY_WEIGHT1 = Real('MY_WEIGHT1')
		START_TIME0 = Real('START_TIME0')
		Y0 = Real('Y0')
		SUM_WEIGHT0 = Real('SUM_WEIGHT0')
		CUSTOMER_ID0 = Real('CUSTOMER_ID0')
		CUSTOMER0 = Real('CUSTOMER0')
		SYSDATE0 = Real('SYSDATE0')
		LOAD_ID0 = Real('LOAD_ID0')
		PRICE0 = Real('PRICE0')
		P_RESERVATION_ID0 = Real('P_RESERVATION_ID0')
		LOADS0 = Real('LOADS0')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( PRICE0 > 0, SYSDATE0 > 0 ) ))
		s.add(True)
		s.add(Implies( True, And( ( MY_WEIGHT1 ) == ( SUM_WEIGHT0 ), Or( X0 == Y0, And( And( And( LOAD_ID0 == LOAD_ID0, CUSTOMER_ID0 == CUSTOMER0 ), START_TIME0 >= SYSDATE0 ), START_TIME0 <= SYSDATE0 + 7 ) ) ) ))
		s.add(True)
		s.add(Implies( True, ( NOTHING1 ) == ( ( 6 ) ) ))
		s.add( Not( And( Implies( True, And( PRICE0 > 0, SYSDATE0 > 0 ) ), And( Implies( True, And( ( MY_WEIGHT1 ) == ( SUM_WEIGHT0 ), Or( X0 == Y0, And( And( And( LOAD_ID0 == LOAD_ID0, CUSTOMER_ID0 == CUSTOMER0 ), START_TIME0 >= SYSDATE0 ), START_TIME0 <= SYSDATE0 + 7 ) ) ) ), And( Implies( True, ( NOTHING1 ) == ( ( 6 ) ) ), And( PRICE0 > 0, SYSDATE0 > 0 ) ) ) ) ) )

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
