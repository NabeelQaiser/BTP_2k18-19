# This file was generated at runtime on 2019-03-08 01:53:31.525148
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		A_PHONE_NUMBER = Real('A_PHONE_NUMBER')
		CURRENT_DATE = Real('CURRENT_DATE')
		A_CITY = Real('A_CITY')
		A_PROVINCE = Real('A_PROVINCE')
		A_SALARY = Real('A_SALARY')
		V_CONTRACT_TYPE_ID = Real('V_CONTRACT_TYPE_ID')
		A_NAME = Real('A_NAME')
		A_POSTAL_CODE = Real('A_POSTAL_CODE')
		ID = Real('ID')
		A_APARTMENT_NUMBER = Real('A_APARTMENT_NUMBER')
		A_PESEL = Real('A_PESEL')
		V_COUNTRY_ID = Real('V_COUNTRY_ID')
		A_CAR_LICENSE_NUMBER = Real('A_CAR_LICENSE_NUMBER')
		A_STREET = Real('A_STREET')
		V_DRIVING_LICENSE_CATEGORY_ID = Real('V_DRIVING_LICENSE_CATEGORY_ID')
		A_SURNAME = Real('A_SURNAME')
		A_HOUSE_NUMBER = Real('A_HOUSE_NUMBER')
		V_COURIER_ID = Real('V_COURIER_ID')
		MAX_ID = Real('MAX_ID')
		A_WAREHOUSE_ID = Real('A_WAREHOUSE_ID')
		GET_MAX_COURIER_ID = Real('GET_MAX_COURIER_ID')
		V_CONTRACT_START = Real('V_CONTRACT_START')

		s = Solver()
		s.add(And( MAX_ID > 0, ID > 0 ))
		s.add( Not( Implies( And( MAX_ID > 0, ID > 0 ), Or( And( MAX_ID > 0, ( ( 1 ) ) > 0 ), And( MAX_ID > 0, ( ( ( MAX_ID ) + 1 ) ) > 0 ) ) ) ) )

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
