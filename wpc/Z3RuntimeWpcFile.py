# This file was generated at runtime on 2019-03-09 19:20:25.096248
from z3 import *

class Z3RuntimeWpcFile():
	def __init__(self):
		self.finalFormula = ""
		self.satisfiability = ""
		self.modelForViolation = ""

	def execute(self):
		COMPLETED = Real('COMPLETED')
		TO_PAY = Real('TO_PAY')
		DATE_OF_PURCHASE = Real('DATE_OF_PURCHASE')
		N_O_VISITS = Real('N_O_VISITS')
		ROOM_ID = Real('ROOM_ID')
		P_RESERVATION_ID = Real('P_RESERVATION_ID')
		COUNT_STAR = Real('COUNT_STAR')
		STATUS = Real('STATUS')
		ENDING = Real('ENDING')
		FIRST_NAME = Real('FIRST_NAME')
		FINAL_COST = Real('FINAL_COST')
		CAPACITY = Real('CAPACITY')
		SUM_PRICE_PER_DAY = Real('SUM_PRICE_PER_DAY')
		LAST_NAME = Real('LAST_NAME')
		PRICE_PER_DAY = Real('PRICE_PER_DAY')
		BEGINNING = Real('BEGINNING')
		PESEL = Real('PESEL')
		PESEL_C = Real('PESEL_C')
		RESERVATION_ID = Real('RESERVATION_ID')
		ROOM_ID_R = Real('ROOM_ID_R')
		RESERVATION_ID_R = Real('RESERVATION_ID_R')
		DISCOUNT = Real('DISCOUNT')
		DATE_OF_RESERVATION = Real('DATE_OF_RESERVATION')
		TELEPHONE = Real('TELEPHONE')

		s = Solver()
		s.add(TO_PAY > 0)
		s.add( Not( Implies( TO_PAY > 0, Or( And( And( And( PESEL_C == PESEL, RESERVATION_ID == RESERVATION_ID_R ), STATUS == COMPLETED ), Or( And( COUNT_STAR > 10, Or( And( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ), ( SUM_PRICE_PER_DAY - SUM_PRICE_PER_DAY * ( ( 10 ) / 100 ) ) > 0 ), And( Not( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ) ), ( FINAL_COST - FINAL_COST * ( ( 10 ) / 100 ) ) > 0 ) ) ), And( Not( COUNT_STAR > 10 ), Or( And( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ), ( SUM_PRICE_PER_DAY - SUM_PRICE_PER_DAY * ( ( 0 ) / 100 ) ) > 0 ), And( Not( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ) ), ( FINAL_COST - FINAL_COST * ( ( 0 ) / 100 ) ) > 0 ) ) ) ) ), And( Not( And( And( PESEL_C == PESEL, RESERVATION_ID == RESERVATION_ID_R ), STATUS == COMPLETED ) ), Or( And( N_O_VISITS > 10, Or( And( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ), ( SUM_PRICE_PER_DAY - SUM_PRICE_PER_DAY * ( ( 10 ) / 100 ) ) > 0 ), And( Not( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ) ), ( FINAL_COST - FINAL_COST * ( ( 10 ) / 100 ) ) > 0 ) ) ), And( Not( N_O_VISITS > 10 ), Or( And( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ), ( SUM_PRICE_PER_DAY - SUM_PRICE_PER_DAY * ( ( 0 ) / 100 ) ) > 0 ), And( Not( And( ROOM_ID == ROOM_ID_R, RESERVATION_ID_R == P_RESERVATION_ID ) ), ( FINAL_COST - FINAL_COST * ( ( 0 ) / 100 ) ) > 0 ) ) ) ) ) ) ) ) )

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