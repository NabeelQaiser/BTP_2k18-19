# This file was generated at runtime on 2019-05-03 06:06:45.351959
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		ID0 = Real('ID0')
		PRICE2 = Real('PRICE2')
		PRICE1 = Real('PRICE1')
		PRICE0 = Real('PRICE0')
		PRICE4 = Real('PRICE4')
		T_PRICE0 = Real('T_PRICE0')
		T_AMOUNT1 = Real('T_AMOUNT1')
		PRICE5 = Real('PRICE5')
		T_ID0 = Real('T_ID0')
		T_PRICE1 = Real('T_PRICE1')
		PRICE3 = Real('PRICE3')
		AMOUNT0 = Real('AMOUNT0')
		T_ID1 = Real('T_ID1')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( And( AMOUNT0 > 0, T_PRICE0 > 0 ), PRICE0 > 0 ) ))
		s.add(True)
		s.add(Implies( True, And( ( PRICE1 ) == ( T_PRICE0 ), T_ID0 == ID0 ) ))
		s.add(AMOUNT0 >= 1000)
		s.add(Implies( AMOUNT0 >= 1000, ( PRICE5 ) == ( ( PRICE1 - 0.1 * AMOUNT0 ) ) ))
		s.add(AMOUNT0 >= 1000)
		s.add(Implies( AMOUNT0 >= 1000, PRICE3 == PRICE5 ))
		s.add(And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ))
		s.add(Implies( And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ), ( PRICE2 ) == ( ( PRICE1 - 0.2 * AMOUNT0 ) ) ))
		s.add(And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ))
		s.add(Implies( And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ), PRICE3 == PRICE2 ))
		s.add(And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ))
		s.add(Implies( And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ), ( PRICE4 ) == ( ( PRICE1 + 0.05 * AMOUNT0 ) ) ))
		s.add(And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ))
		s.add(Implies( And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ), PRICE3 == PRICE4 ))
		s.add(True)
		s.add(Implies( True, ( T_ID1 ) == ( ID0 ) ))
		s.add(True)
		s.add(Implies( True, ( T_PRICE1 ) == ( PRICE3 ) ))
		s.add(True)
		s.add(Implies( True, ( T_AMOUNT1 ) == ( AMOUNT0 ) ))
		s.add( Not( And( Implies( True, And( And( AMOUNT0 > 0, T_PRICE0 > 0 ), PRICE0 > 0 ) ), And( Implies( True, And( ( PRICE1 ) == ( T_PRICE0 ), T_ID0 == ID0 ) ), And( Implies( AMOUNT0 >= 1000, ( PRICE5 ) == ( ( PRICE1 - 0.1 * AMOUNT0 ) ) ), And( Implies( AMOUNT0 >= 1000, PRICE3 == PRICE5 ), And( Implies( And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ), ( PRICE2 ) == ( ( PRICE1 - 0.2 * AMOUNT0 ) ) ), And( Implies( And( Not( AMOUNT0 >= 1000 ), And( AMOUNT0 >= 200, PRICE1 > 5000 ) ), PRICE3 == PRICE2 ), And( Implies( And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ), ( PRICE4 ) == ( ( PRICE1 + 0.05 * AMOUNT0 ) ) ), And( Implies( And( Not( AMOUNT0 >= 1000 ), Not( And( AMOUNT0 >= 200, PRICE1 > 5000 ) ) ), PRICE3 == PRICE4 ), And( Implies( True, ( T_ID1 ) == ( ID0 ) ), And( Implies( True, ( T_PRICE1 ) == ( PRICE3 ) ), And( Implies( True, ( T_AMOUNT1 ) == ( AMOUNT0 ) ), PRICE3 > 0 ) ) ) ) ) ) ) ) ) ) ) ) )

		self.finalFormula = str(s)
		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			self.satisfiability = "violation"
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			self.satisfiability = "sat"