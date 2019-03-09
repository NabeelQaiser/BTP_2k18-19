# This file was generated at runtime on 2019-03-09 19:10:06.088481
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		B0 = Real('B0')
		N_O_VISITS0 = Real('N_O_VISITS0')
		M0 = Real('M0')
		X1 = Real('X1')
		C30 = Real('C30')
		D20 = Real('D20')
		B20 = Real('B20')
		G1 = Real('G1')
		C20 = Real('C20')
		D30 = Real('D30')
		C0 = Real('C0')
		A30 = Real('A30')
		D0 = Real('D0')
		NOTHING1 = Real('NOTHING1')
		B30 = Real('B30')
		Y1 = Real('Y1')
		A0 = Real('A0')
		A20 = Real('A20')

		s = Solver()
		s.add(True)
		s.add(Implies( True, And( ( G1 ) == ( A0 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ))
		s.add(True)
		s.add(Implies( True, A0 > 0 ))
		s.add(True)
		s.add(Implies( True, And( ( X1 ) == ( A0 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ))
		s.add(True)
		s.add(Implies( True, And( ( Y1 ) == ( B30 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ))
		s.add(True)
		s.add(Implies( True, ( NOTHING1 ) == ( ( 6 ) ) ))
		s.add( Not( And( Implies( True, And( ( G1 ) == ( A0 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ), And( Implies( True, A0 > 0 ), And( Implies( True, And( ( X1 ) == ( A0 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ), And( Implies( True, And( ( Y1 ) == ( B30 ), And( And( A20 >= M0 + 5, C0 < 99 ), And( B0 == B20, C20 == C30 ) ) ) ), And( Implies( True, ( NOTHING1 ) == ( ( 6 ) ) ), A0 > 0 ) ) ) ) ) ) )

		self.finalFormula = str(s)
		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			self.satisfiability = "Unsatisfiable"
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			self.satisfiability = "Satisfiable"