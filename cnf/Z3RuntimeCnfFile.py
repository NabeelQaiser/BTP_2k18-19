# This file was generated at runtime on 2019-05-03 17:35:30.216386
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		X0 = Real('X0')
		X1 = Real('X1')
		X2 = Real('X2')

		s = Solver()
		s.add(True)
		s.add(Implies( True, X0 > - 50 ))
		s.add(X0 < 0)
		s.add(Implies( X0 < 0, ( X1 ) == ( ( - X0 ) ) ))
		s.add(X0 < 0)
		s.add(Implies( X0 < 0, X2 == X1 ))
		s.add(Not( X0 < 0 ))
		s.add(Implies( Not( X0 < 0 ), X2 == X0 ))
		s.add( Not( And( Implies( True, X0 > - 50 ), And( Implies( X0 < 0, ( X1 ) == ( ( - X0 ) ) ), And( Implies( X0 < 0, X2 == X1 ), And( Implies( Not( X0 < 0 ), X2 == X0 ), X2 > 0 ) ) ) ) ) )

		self.finalFormula = str(s)
		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			self.satisfiability = "violation"
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			self.satisfiability = "sat"