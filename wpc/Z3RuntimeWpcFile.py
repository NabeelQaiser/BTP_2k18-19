# This file was generated at runtime on 2019-03-05 19:52:44.186194
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		EMP_NUMBER = Real('EMP_NUMBER')
		MGR = Real('MGR')
		JOB = Real('JOB')
		SAL = Real('SAL')
		EMP_RET = Real('EMP_RET')
		HIREDATE = Real('HIREDATE')
		COMM = Real('COMM')
		ENAME = Real('ENAME')
		DEPTNO = Real('DEPTNO')
		EMPNO = Real('EMPNO')

		s = Solver()
		s.add(EMP_RET > 0)
		s.add( Not( Implies( EMP_RET > 0, Or( And( EMPNO == EMP_NUMBER, EMPNO > 0 ), And( Not( EMPNO == EMP_NUMBER ), EMP_RET > 0 ) ) ) ) )

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
