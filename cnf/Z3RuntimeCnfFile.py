# This file was generated at runtime on 2019-04-15 19:13:15.085083
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		ACC_NO0 = Real('ACC_NO0')
		BALANCE0 = Real('BALANCE0')
		BALANCE1 = Real('BALANCE1')
		AMT0 = Real('AMT0')
		MIN_BAL0 = Real('MIN_BAL0')
		BAL1 = Real('BAL1')
		ACCNO2 = Real('ACCNO2')
		ACCNO0 = Real('ACCNO0')
		BAL0 = Real('BAL0')
		MIN_BAL1 = Real('MIN_BAL1')
		BALANCE2 = Real('BALANCE2')
		ACCNO1 = Real('ACCNO1')

		s = Solver()
		s.add(True)
		s.add(Implies( True, BALANCE0 > 0 ))
		s.add(True)
		s.add(Implies( True, And( ( BAL1 ) == ( BALANCE0 ), ACCNO0 == ACC_NO0 ) ))
		s.add(True)
		s.add(Implies( True, ( MIN_BAL1 ) == ( ( BAL1 - AMT0 ) ) ))
		s.add(And( AMT0 < 10000, MIN_BAL1 > 0 ))
		s.add(Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), Or( And( ( BALANCE1 ) == ( BALANCE0 - AMT0 ), ACCNO0 == ACC_NO0 ), And( Not( ACCNO0 == ACC_NO0 ), ( BALANCE1 ) == ( BALANCE0 ) ) ) ))
		s.add(And( AMT0 < 10000, MIN_BAL1 > 0 ))
		s.add(Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), ACCNO2 == ACCNO1 ))
		s.add(And( AMT0 < 10000, MIN_BAL1 > 0 ))
		s.add(Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), BALANCE2 == BALANCE1 ))
		s.add(Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ))
		s.add(Implies( Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ), ACCNO2 == ACCNO0 ))
		s.add(Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ))
		s.add(Implies( Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ), BALANCE2 == BALANCE0 ))
		s.add( Not( And( Implies( True, BALANCE0 > 0 ), And( Implies( True, And( ( BAL1 ) == ( BALANCE0 ), ACCNO0 == ACC_NO0 ) ), And( Implies( True, ( MIN_BAL1 ) == ( ( BAL1 - AMT0 ) ) ), And( Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), Or( And( ( BALANCE1 ) == ( BALANCE0 - AMT0 ), ACCNO0 == ACC_NO0 ), And( Not( ACCNO0 == ACC_NO0 ), ( BALANCE1 ) == ( BALANCE0 ) ) ) ), And( Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), ACCNO2 == ACCNO1 ), And( Implies( And( AMT0 < 10000, MIN_BAL1 > 0 ), BALANCE2 == BALANCE1 ), And( Implies( Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ), ACCNO2 == ACCNO0 ), And( Implies( Not( And( AMT0 < 10000, MIN_BAL1 > 0 ) ), BALANCE2 == BALANCE0 ), BALANCE2 > 0 ) ) ) ) ) ) ) ) ) )

		self.finalFormula = str(s)
		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			self.satisfiability = "Unsatisfiable"
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			self.satisfiability = "Satisfiable"