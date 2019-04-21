# This file was generated at runtime on 2019-04-15 19:15:06.569068
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		ACC_NO = Real('ACC_NO')
		BALANCE = Real('BALANCE')
		AMT = Real('AMT')
		ACCNO = Real('ACCNO')
		BAL = Real('BAL')
		MIN_BAL = Real('MIN_BAL')

		s = Solver()
		s.add(BALANCE > 0)
		s.add( Not( Implies( BALANCE > 0, Or( And( ACCNO == ACC_NO, Or( And( And( AMT < 10000, ( BALANCE - AMT ) > 0 ), Or( And( ACCNO == ACC_NO, ( BALANCE - AMT ) > 0 ), And( Not( ACCNO == ACC_NO ), BALANCE > 0 ) ) ), And( Not( And( AMT < 10000, ( BALANCE - AMT ) > 0 ) ), BALANCE > 0 ) ) ), And( Not( ACCNO == ACC_NO ), Or( And( And( AMT < 10000, ( BAL - AMT ) > 0 ), Or( And( ACCNO == ACC_NO, ( BALANCE - AMT ) > 0 ), And( Not( ACCNO == ACC_NO ), BALANCE > 0 ) ) ), And( Not( And( AMT < 10000, ( BAL - AMT ) > 0 ) ), BALANCE > 0 ) ) ) ) ) ) )

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