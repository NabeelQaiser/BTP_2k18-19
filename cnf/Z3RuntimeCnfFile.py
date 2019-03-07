# This file was generated at runtime on 2019-03-08 02:57:49.126623
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		A_PARCEL_ID0 = Real('A_PARCEL_ID0')
		A_NEW_WAREHOUSE_ID0 = Real('A_NEW_WAREHOUSE_ID0')
		ENTERED_WAREHOUSE1 = Real('ENTERED_WAREHOUSE1')
		WAREHOUSE_ID0 = Real('WAREHOUSE_ID0')
		ENTERED_WAREHOUSE2 = Real('ENTERED_WAREHOUSE2')
		PARCEL_ID0 = Real('PARCEL_ID0')
		PARCEL_ID1 = Real('PARCEL_ID1')
		ENTERED_WAREHOUSE3 = Real('ENTERED_WAREHOUSE3')
		V_TIME0 = Real('V_TIME0')
		WAREHOUSE_ID1 = Real('WAREHOUSE_ID1')
		V_TIME1 = Real('V_TIME1')
		WAREHOUSE_ID2 = Real('WAREHOUSE_ID2')
		A_OLD_WAREHOUSE_ID0 = Real('A_OLD_WAREHOUSE_ID0')
		PARCEL_ID2 = Real('PARCEL_ID2')
		ENTERED_WAREHOUSE0 = Real('ENTERED_WAREHOUSE0')
		CURRENT_DATE0 = Real('CURRENT_DATE0')
		PARCEL_ID3 = Real('PARCEL_ID3')
		WAREHOUSE_ID3 = Real('WAREHOUSE_ID3')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( And( PARCEL_ID0 > 0, WAREHOUSE_ID0 > 0 ), ENTERED_WAREHOUSE0 > 0 ) ))
		s.add(True)
		s.add(Implies( True, ( V_TIME1 ) == ( CURRENT_DATE0 ( ) ) ))
		s.add(True)
		s.add(Implies( True, Or( And( ( LEFT_WAREHOUSE ) == ( V_TIME1 ), WAREHOUSE_ID0 == A_OLD_WAREHOUSE_ID0 ), And( Not( WAREHOUSE_ID0 == A_OLD_WAREHOUSE_ID0 ), ( LEFT_WAREHOUSE ) == ( LEFT_WAREHOUSE ) ) ) ))
		s.add(True)
		s.add(Implies( True, ( PARCEL_ID2 ) == ( A_PARCEL_ID0 ) ))
		s.add(True)
		s.add(Implies( True, ( WAREHOUSE_ID2 ) == ( A_NEW_WAREHOUSE_ID0 ) ))
		s.add(True)
		s.add(Implies( True, ( ENTERED_WAREHOUSE2 ) == ( V_TIME1 ) ))
		s.add(True)
		s.add(Implies( True, PARCEL_ID3 == PARCEL_ID2 ))
		s.add(True)
		s.add(Implies( True, WAREHOUSE_ID3 == WAREHOUSE_ID2 ))
		s.add(True)
		s.add(Implies( True, ENTERED_WAREHOUSE3 == ENTERED_WAREHOUSE2 ))
		s.add(True)
		s.add(Implies( True, PARCEL_ID3 == PARCEL_ID1 ))
		s.add(True)
		s.add(Implies( True, WAREHOUSE_ID3 == WAREHOUSE_ID1 ))
		s.add(True)
		s.add(Implies( True, ENTERED_WAREHOUSE3 == ENTERED_WAREHOUSE1 ))
		s.add( Not( And( Implies( True, And( And( PARCEL_ID0 > 0, WAREHOUSE_ID0 > 0 ), ENTERED_WAREHOUSE0 > 0 ) ), And( Implies( True, ( V_TIME1 ) == ( CURRENT_DATE0 ( ) ) ), And( Implies( True, Or( And( ( LEFT_WAREHOUSE ) == ( V_TIME1 ), WAREHOUSE_ID0 == A_OLD_WAREHOUSE_ID0 ), And( Not( WAREHOUSE_ID0 == A_OLD_WAREHOUSE_ID0 ), ( LEFT_WAREHOUSE ) == ( LEFT_WAREHOUSE ) ) ) ), And( Implies( True, ( PARCEL_ID2 ) == ( A_PARCEL_ID0 ) ), And( Implies( True, ( WAREHOUSE_ID2 ) == ( A_NEW_WAREHOUSE_ID0 ) ), And( Implies( True, ( ENTERED_WAREHOUSE2 ) == ( V_TIME1 ) ), And( Implies( True, PARCEL_ID3 == PARCEL_ID2 ), And( Implies( True, WAREHOUSE_ID3 == WAREHOUSE_ID2 ), And( Implies( True, ENTERED_WAREHOUSE3 == ENTERED_WAREHOUSE2 ), And( Implies( True, PARCEL_ID3 == PARCEL_ID1 ), And( Implies( True, WAREHOUSE_ID3 == WAREHOUSE_ID1 ), And( Implies( True, ENTERED_WAREHOUSE3 == ENTERED_WAREHOUSE1 ), And( And( PARCEL_ID3 > 0, WAREHOUSE_ID3 > 0 ), ENTERED_WAREHOUSE3 > 0 ) ) ) ) ) ) ) ) ) ) ) ) ) ) )

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
