# This file was generated at runtime on 2019-03-07 13:57:36.694218
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		EMPLOYEE_ID = Real('EMPLOYEE_ID')
		SALARY = Real('SALARY')
		COMMISSION = Real('COMMISSION')
		COMMISSION_PCT = Real('COMMISSION_PCT')
		SALES_AMT = Real('SALES_AMT')
		EMP_ID = Real('EMP_ID')

		s = Solver()
		s.add(And( SALARY > 0, SALARY < 90000 ))
		s.add( Not( Implies( And( SALARY > 0, SALARY < 90000 ), Or( And( EMPLOYEE_ID == EMP_ID, Or( And( SALARY > 0, SALARY < 90000 ), Or( And( EMPLOYEE_ID == EMP_ID, And( ( SALARY + SALES_AMT * COMMISSION_PCT ) > 0, ( SALARY + SALES_AMT * COMMISSION_PCT ) < 90000 ) ), And( Not( EMPLOYEE_ID == EMP_ID ), And( SALARY > 0, SALARY < 90000 ) ) ) ) ), And( Not( EMPLOYEE_ID == EMP_ID ), Or( And( SALARY > 0, SALARY < 90000 ), Or( And( EMPLOYEE_ID == EMP_ID, And( ( SALARY + SALES_AMT * COMMISSION ) > 0, ( SALARY + SALES_AMT * COMMISSION ) < 90000 ) ), And( Not( EMPLOYEE_ID == EMP_ID ), And( SALARY > 0, SALARY < 90000 ) ) ) ) ) ) ) ) )

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
