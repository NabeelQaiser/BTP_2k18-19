# This file was generated at runtime on 2019-03-09 19:50:06.236541
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		CAPACITY0 = Real('CAPACITY0')
		ROOM_ID0 = Real('ROOM_ID0')
		LAST_NAME0 = Real('LAST_NAME0')
		ENDING0 = Real('ENDING0')
		PESEL_C0 = Real('PESEL_C0')
		N_O_VISITS0 = Real('N_O_VISITS0')
		BEGINNING0 = Real('BEGINNING0')
		DISCOUNT0 = Real('DISCOUNT0')
		DATE_OF_PURCHASE0 = Real('DATE_OF_PURCHASE0')
		FINAL_COST1 = Real('FINAL_COST1')
		FIRST_NAME0 = Real('FIRST_NAME0')
		TELEPHONE0 = Real('TELEPHONE0')
		PRICE_PER_DAY0 = Real('PRICE_PER_DAY0')
		DATE_OF_RESERVATION0 = Real('DATE_OF_RESERVATION0')
		DISCOUNT2 = Real('DISCOUNT2')
		SUM_PRICE_PER_DAY0 = Real('SUM_PRICE_PER_DAY0')
		TO_PAY0 = Real('TO_PAY0')
		FINAL_COST0 = Real('FINAL_COST0')
		COUNT_STAR = Real('COUNT_STAR')
		DISCOUNT1 = Real('DISCOUNT1')
		N_O_VISITS1 = Real('N_O_VISITS1')
		TO_PAY1 = Real('TO_PAY1')
		STATUS0 = Real('STATUS0')
		ROOM_ID_R0 = Real('ROOM_ID_R0')
		RESERVATION_ID_R0 = Real('RESERVATION_ID_R0')
		P_RESERVATION_ID0 = Real('P_RESERVATION_ID0')
		DISCOUNT3 = Real('DISCOUNT3')
		PESEL0 = Real('PESEL0')
		COMPLETED0 = Real('COMPLETED0')
		RESERVATION_ID0 = Real('RESERVATION_ID0')

		s = Solver()
		s.add(True)
		s.add(Implies( True, TO_PAY0 > 0 ))
		s.add(True)
		s.add(Implies( True, And( ( N_O_VISITS1 ) == ( COUNT_STAR ), And( STATUS0 == COMPLETED0, And( PESEL_C0 == PESEL0, RESERVATION_ID0 == RESERVATION_ID_R0 ) ) ) ))
		s.add(N_O_VISITS1 > 10)
		s.add(Implies( N_O_VISITS1 > 10, ( DISCOUNT1 ) == ( ( 10 ) ) ))
		s.add(N_O_VISITS1 > 10)
		s.add(Implies( N_O_VISITS1 > 10, DISCOUNT2 == DISCOUNT1 ))
		s.add(Not( N_O_VISITS1 > 10 ))
		s.add(Implies( Not( N_O_VISITS1 > 10 ), ( DISCOUNT3 ) == ( ( 0 ) ) ))
		s.add(Not( N_O_VISITS1 > 10 ))
		s.add(Implies( Not( N_O_VISITS1 > 10 ), DISCOUNT2 == DISCOUNT3 ))
		s.add(True)
		s.add(Implies( True, And( ( FINAL_COST1 ) == ( SUM_PRICE_PER_DAY0 ), And( RESERVATION_ID_R0 == P_RESERVATION_ID0, ROOM_ID0 == ROOM_ID_R0 ) ) ))
		s.add(True)
		s.add(Implies( True, ( TO_PAY1 ) == ( ( FINAL_COST1 - FINAL_COST1 * ( DISCOUNT2 / 100 ) ) ) ))
		s.add( Not( And( Implies( True, TO_PAY0 > 0 ), And( Implies( True, And( ( N_O_VISITS1 ) == ( COUNT_STAR ), And( STATUS0 == COMPLETED0, And( PESEL_C0 == PESEL0, RESERVATION_ID0 == RESERVATION_ID_R0 ) ) ) ), And( Implies( N_O_VISITS1 > 10, ( DISCOUNT1 ) == ( ( 10 ) ) ), And( Implies( N_O_VISITS1 > 10, DISCOUNT2 == DISCOUNT1 ), And( Implies( Not( N_O_VISITS1 > 10 ), ( DISCOUNT3 ) == ( ( 0 ) ) ), And( Implies( Not( N_O_VISITS1 > 10 ), DISCOUNT2 == DISCOUNT3 ), And( Implies( True, And( ( FINAL_COST1 ) == ( SUM_PRICE_PER_DAY0 ), And( RESERVATION_ID_R0 == P_RESERVATION_ID0, ROOM_ID0 == ROOM_ID_R0 ) ) ), And( Implies( True, ( TO_PAY1 ) == ( ( FINAL_COST1 - FINAL_COST1 * ( DISCOUNT2 / 100 ) ) ) ), TO_PAY1 > 0 ) ) ) ) ) ) ) ) ) )

		self.finalFormula = str(s)
		self.satisfiability = str(s.check())
		if self.satisfiability == "sat":
			self.satisfiability = "Unsatisfiable"
			self.modelForViolation = str(s.model())
		elif self.satisfiability == "unsat":
			self.satisfiability = "Satisfiable"