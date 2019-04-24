# This file was generated at runtime on 2019-04-24 13:52:07.503019
from z3 import *

class Z3RuntimeCnfFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		RESERVATION_ID0 = Real('RESERVATION_ID0')
		FIRST_NAME0 = Real('FIRST_NAME0')
		N_O_VISITS0 = Real('N_O_VISITS0')
		LAST_NAME0 = Real('LAST_NAME0')
		COMPLETED0 = Real('COMPLETED0')
		CAPACITY0 = Real('CAPACITY0')
		TELEPHONE0 = Real('TELEPHONE0')
		COUNT_STAR = Real('COUNT_STAR')
		ROOM_ID_R0 = Real('ROOM_ID_R0')
		TO_PAY1 = Real('TO_PAY1')
		SUM_PRICE_PER_DAY0 = Real('SUM_PRICE_PER_DAY0')
		FINAL_COST1 = Real('FINAL_COST1')
		DISCOUNT1 = Real('DISCOUNT1')
		ENDING0 = Real('ENDING0')
		P_RESERVATION_ID0 = Real('P_RESERVATION_ID0')
		BEGINNING0 = Real('BEGINNING0')
		DISCOUNT2 = Real('DISCOUNT2')
		ROOM_ID0 = Real('ROOM_ID0')
		N_O_VISITS1 = Real('N_O_VISITS1')
		PESEL_C0 = Real('PESEL_C0')
		PESEL0 = Real('PESEL0')
		DISCOUNT0 = Real('DISCOUNT0')
		STATUS0 = Real('STATUS0')
		PRICE_PER_DAY0 = Real('PRICE_PER_DAY0')
		DATE_OF_PURCHASE0 = Real('DATE_OF_PURCHASE0')
		DISCOUNT3 = Real('DISCOUNT3')
		RESERVATION_ID_R0 = Real('RESERVATION_ID_R0')
		DATE_OF_RESERVATION0 = Real('DATE_OF_RESERVATION0')
		TO_PAY0 = Real('TO_PAY0')
		FINAL_COST0 = Real('FINAL_COST0')

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