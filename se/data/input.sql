

CREATE or replace PACKAGE STATIC_DATA IS
PROJECT_NAME CONSTANT VARCHAR2(20) := 'DRONES';
BLACK_FRIDAY_DISCOUNT INTEGER := 40;
OMG_SMTH EXCEPTION;
iter1 INTEGER := 1;
iter2 INTEGER := 1;
END STATIC_DATA;




CREATE TABLE MY_AUDIT (
	AUDIT_ID NUMBER(5) NOT NULL PRIMARY KEY, 
	USER_NAME VARCHAR2(20), 
	DATE_IN VARCHAR2(20),
	TABLE_NAME VARCHAR2(20)) 
PCTFREE 10 
PCTUSED 80 
STORAGE(INITIAL 50K NEXT 50K MAXEXTENTS 5 PCTINCREASE 0);




CREATE OR REPLACE PROCEDURE ADD_DRONE (model VARCHAR2, weight NUMBER, add_weight NUMBER, speed NUMBER) AS
	not_user EXCEPTION;
BEGIN
	IF USER<> 'SYST' THEN
		RAISE not_user;
	END IF;
	INSERT INTO DRONES VALUES(MY_SEQ.NEXTVAL, model, weight, add_weight, speed);
	COMMIT;
	EXCEPTION when not_user then
		insert into my_audit values (my_seq.nextval, USER, to_char(sysdate), 'Drones');
		commit;
END add_drone;




CREATE OR REPLACE PROCEDURE TEMPORARY_WEEK_DISCOUNT(CUSTOMER IN CUSTOMERS.CUSTOMER_ID%TYPE, PERCENT INTEGER)
IS
	big_discount EXCEPTION;
	low_discount EXCEPTION;
	wrong_discount EXCEPTION;
	sum_weight NUMBER(5,3);
BEGIN
	SELECT SUM(LOADS.WEIGHT) INTO sum_weight from LOADS, ROUTES 
	WHERE LOADS.LOAD_ID IN (SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	if percent < 0 or percent > 100 then
		raise wrong_discount;
	elsif sum_weight < 10 and percent > 50 then
		raise big_discount;
	elsif sum_weight > 30 and percent < 10 then
		raise low_discount;
	end if;
	UPDATE ROUTES
	SET PRICE = PRICE*((100 - PERCENT)/100)
	WHERE LOAD_ID IN (
		SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	COMMIT;
	EXCEPTION
	when low_discount then
		raise_application_error(-20001, 'You wrote too low discount');
	when big_discount then
		raise_application_error(-20002, 'You wrote too big discount');
	when wrong_discount then
		raise_application_error(-20003, 'You wrote wrong discount');
END TEMPORARY_WEEK_DISCOUNT;



create or replace procedure exc is
numb NUMBER(5,2);
begin
numb := 4/0;
exception
when zero_divide then
raise_application_error(-20090, 'U R LOSER');
end exc;






create or replace package mypack is
FUNCTION LESS_THAN_AVG_DISTANCE RETURN INTEGER;
FUNCTION EFFECTIVE_CUSTOMERS_PERCENT(ROUTES_COUNT INTEGER) RETURN NUMBER;
FUNCTION EFFECTIVE_ADDWEIGHT_PERCENT(DRONE IN DRONES.DRONE_ID%TYPE) RETURN NUMBER;
FUNCTION GET_DRONE_TO_TRANSPORT(MY_WEIGHT IN DRONES.ADD_WEIGHT%TYPE) RETURN NUMBER;
PROCEDURE TEMPORARY_WEEK_DISCOUNT(CUSTOMER IN CUSTOMERS.CUSTOMER_ID%TYPE, PERCENT INTEGER);
FUNCTION CUT_STRING(MY_STR VARCHAR2, N INTEGER, M INTEGER) RETURN VARCHAR2;
FUNCTION PUSH_STARS(STR1 VARCHAR2, STR2 VARCHAR2) RETURN VARCHAR2;
FUNCTION SHUFFLE_STRINGS(STR1 VARCHAR2, STR2 VARCHAR2) RETURN VARCHAR2;
FUNCTION COMMON_LETTERS(STR1 VARCHAR2, STR2 VARCHAR2) RETURN VARCHAR2;
FUNCTION DIFF_LETTERS(STR1 VARCHAR2, STR2 VARCHAR2) RETURN VARCHAR2;
FUNCTION Display_Customers(cust varchar2) RETURN VARCHAR2;
PROCEDURE DISCOUNT(wei IN LOADS.WEIGHT%TYPE);
PROCEDURE fill_five_table(numb number);
FUNCTION get_drones(min number, max number) RETURN VARCHAR2;
end mypack;



create or replace package body mypack is
FUNCTION LESS_THAN_AVG_DISTANCE 
RETURN INTEGER AS COUNT_ROWS INTEGER;
BEGIN
	SELECT COUNT(*) INTO COUNT_ROWS 
	FROM ROUTES 
	WHERE DISTANCE < (SELECT AVG(DISTANCE) FROM ROUTES);
	RETURN COUNT_ROWS;
END LESS_THAN_AVG_DISTANCE;

FUNCTION EFFECTIVE_CUSTOMERS_PERCENT(ROUTES_COUNT INTEGER)
RETURN NUMBER
AS PERCENT NUMBER(6,2);
NEEDED_CUSTOMERS NUMBER(6,2);
ALL_CUSTOMERS NUMBER(6,2);
BEGIN 
	SELECT COUNT(*) INTO NEEDED_CUSTOMERS FROM (
		SELECT LOADS.CUSTOMER_ID, COUNT(ROUTES.ROUTE_ID) 
		FROM LOADS, ROUTES 
		WHERE LOADS.LOAD_ID = ROUTES.LOAD_ID 
		GROUP BY LOADS.CUSTOMER_ID 
		HAVING COUNT(ROUTES.ROUTE_ID) >= ROUTES_COUNT);
	SELECT COUNT(*) INTO ALL_CUSTOMERS FROM CUSTOMERS;
	PERCENT :=(NEEDED_CUSTOMERS/ALL_CUSTOMERS)*100;
	RETURN(PERCENT);
END EFFECTIVE_CUSTOMERS_PERCENT;

FUNCTION EFFECTIVE_ADDWEIGHT_PERCENT(DRONE IN DRONES.DRONE_ID%TYPE)
RETURN NUMBER
AS PERCENT NUMBER(6,2);
AVGWEIGHT NUMBER(6,2);
ADDWEIGHT NUMBER(6,2);
BEGIN
SELECT AVG(LOADS.WEIGHT) INTO AVGWEIGHT 
	FROM LOADS, ROUTES 
	WHERE LOADS.LOAD_ID = ROUTES.LOAD_ID AND ROUTES.DRONE_ID = DRONE;
SELECT ADD_WEIGHT INTO ADDWEIGHT FROM DRONES WHERE DRONE_ID = DRONE;
PERCENT :=(AVGWEIGHT/ADDWEIGHT)*100;
RETURN(PERCENT);
END EFFECTIVE_ADDWEIGHT_PERCENT;

FUNCTION GET_DRONE_TO_TRANSPORT(MY_WEIGHT IN DRONES.ADD_WEIGHT%TYPE)
RETURN NUMBER
AS DRONE NUMBER(3);
NUM NUMBER(3);
BEGIN
SELECT DRONE_ID INTO NUM FROM DRONES 
	WHERE ADD_WEIGHT >= MY_WEIGHT AND ROWNUM = 1
	ORDER BY ADD_WEIGHT;
DRONE := NUM;
RETURN(DRONE);
END GET_DRONE_TO_TRANSPORT;

PROCEDURE TEMPORARY_WEEK_DISCOUNT(CUSTOMER IN CUSTOMERS.CUSTOMER_ID%TYPE, PERCENT INTEGER)
IS
	big_discount EXCEPTION;
	low_discount EXCEPTION;
	wrong_discount EXCEPTION;
	sum_weight NUMBER(5,3);
BEGIN
	SELECT SUM(LOADS.WEIGHT) INTO sum_weight from LOADS, ROUTES 
	WHERE LOADS.LOAD_ID IN (SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	if percent < 0 or percent > 100 then
		raise wrong_discount;
	elsif sum_weight < 10 and percent > 50 then
		raise big_discount;
	elsif sum_weight > 30 and percent < 10 then
		raise low_discount;
	end if;
	UPDATE ROUTES
	SET PRICE = PRICE*((100 - PERCENT)/100)
	WHERE LOAD_ID IN (
		SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	COMMIT;
	EXCEPTION
	when low_discount then
		raise_application_error(-20001, 'You wrote too low discount');
	when big_discount then
		raise_application_error(-20002, 'You wrote too big discount');
	when wrong_discount then
		raise_application_error(-20003, 'You wrote wrong discount');
END TEMPORARY_WEEK_DISCOUNT;

FUNCTION CUT_STRING(MY_STR VARCHAR2, N INTEGER, M INTEGER)
RETURN VARCHAR2
AS RES VARCHAR2(20);
BEGIN
	SELECT SUBSTR(MY_STR, 1, M - 1) || SUBSTR(MY_STR, N + M) INTO RES FROM DUAL;
RETURN(RES);
END CUT_STRING;

FUNCTION PUSH_STARS(STR1 VARCHAR2, STR2 VARCHAR2)
RETURN VARCHAR2
AS RES VARCHAR2(30);
BEGIN
	IF (LENGTH(STR1) < LENGTH(STR2)) THEN
		SELECT LPAD(STR1, LENGTH(STR2), '*') INTO RES FROM DUAL;
	ELSIF (LENGTH(STR2) < LENGTH(STR1)) THEN
		SELECT LPAD(STR2, LENGTH(STR1), '*') INTO RES FROM DUAL;
	END IF;
RETURN(RES);
END PUSH_STARS;


FUNCTION SHUFFLE_STRINGS(STR1 VARCHAR2, STR2 VARCHAR2)
RETURN VARCHAR2
AS RES VARCHAR2(30);
LEN INTEGER := 0;
ENDING VARCHAR2(20);
BEGIN
	IF (LENGTH(STR1) < LENGTH(STR2)) THEN
		LEN := LENGTH(STR1);
		SELECT SUBSTR(STR2, LEN + 1) INTO ENDING FROM DUAL;
	ELSE
		LEN := LENGTH(STR2);
		SELECT SUBSTR(STR1, LEN + 1) INTO ENDING FROM DUAL;
	END IF;
	FOR I IN 1..LEN LOOP
		SELECT RES || SUBSTR(STR1, I, 1) || SUBSTR(STR2, I, 1) INTO RES FROM DUAL;
	END LOOP;
	RES := RES || ENDING;
RETURN(RES);
END SHUFFLE_STRINGS;

FUNCTION COMMON_LETTERS(STR1 VARCHAR2, STR2 VARCHAR2)
RETURN VARCHAR2
AS RES VARCHAR2(30);
LETTER VARCHAR2(1);
BEGIN
	FOR I IN 1..LENGTH(STR1) LOOP
		SELECT SUBSTR(STR1, I, 1) INTO LETTER FROM DUAL;
		IF INSTR(STR2, LETTER) > 0 THEN
			RES := RES || LETTER;
		END IF;
	END LOOP;
RETURN(RES);
END COMMON_LETTERS;

FUNCTION DIFF_LETTERS(STR1 VARCHAR2, STR2 VARCHAR2)
RETURN VARCHAR2
AS RES VARCHAR2(30);
LETTER VARCHAR2(1);
BEGIN
	FOR I IN 1..LENGTH(STR1) LOOP
		SELECT SUBSTR(STR1, I, 1) INTO LETTER FROM DUAL;
		IF INSTR(STR2, LETTER) = 0 THEN
			RES := RES || LETTER;
		END IF;
	END LOOP;
	FOR I IN 1..LENGTH(STR2) LOOP
		SELECT SUBSTR(STR2, I, 1) INTO LETTER FROM DUAL;
		IF INSTR(STR1, LETTER) = 0 THEN
			RES := RES || LETTER;
		END IF;
	END LOOP;
RETURN(RES);
END DIFF_LETTERS;

FUNCTION Display_Customers(cust varchar2)
RETURN VARCHAR2
is
RES VARCHAR2(400);
CUST_NAME VARCHAR2(30);
CURSOR c1 IS SELECT title from customers, loads where loads.Customer_Id = customers.customer_id and name = cust;
BEGIN
	open c1;
	fetch c1 into res;
	if c1%notfound = false then
		
	loop
		fetch c1 into cust_name;
		res := res || ', ' || cust_name;
	exit when c1%notfound;
	end loop;
	end if;
	
RETURN(RES);
END Display_Customers;

PROCEDURE DISCOUNT(wei IN LOADS.WEIGHT%TYPE)
IS
PR NUMBER(5,3);
cursor load_ids is select load_id from loads where weight > wei;
cursor route_price(load number) is select route_id, price from routes where load_id = load for update;
BEGIN
	FOR I IN LOAD_ids loop
		for j in route_price(i.load_id) loop
			pr := j.price * 0.8;
			update routes set routes.price = pr where current of route_price;
		end loop;
	end loop;
END DISCOUNT;

PROCEDURE fill_five_table(numb number)
IS
minspeed number(5,2);
maxspeed1 number(5,2);
step number(5,2);

drones_str varchar2(300);
maxspeed_drone varchar2(100) := '';
cursor max_speed_drones(maxsp number) is select model from drones where speed = maxsp;

BEGIN
	delete from want_my_five;
	select max(speed), min(speed) into maxspeed1, minspeed from drones;
	step := (maxspeed1 - minspeed)/numb;
	
	for i in 1..numb loop
		drones_str := mypack.get_drones(minspeed + (i-1)* step, minspeed + i * step);
		if i = numb then			
			for rec in max_speed_drones(maxspeed1) loop
				maxspeed_drone := maxspeed_drone || ',' || rec.model;
			end loop;
			drones_str := drones_str || maxspeed_drone;			
			insert into want_my_five values (my_seq.nextval, minspeed + (i-1)* step, maxspeed1, ltrim(drones_str, ','));
		else
			insert into want_my_five values (my_seq.nextval, minspeed + (i-1)* step, minspeed + i * step, ltrim(drones_str, ','));
		end if;
	end loop;
	
END fill_five_table;

FUNCTION get_drones(min number, max number)
RETURN VARCHAR2
is
RES VARCHAR2(400);
CURSOR c1 IS SELECT model from drones where speed >= min and speed < max;
BEGIN
	for rec in c1 loop
		res := res || ',' || rec.model;
	end loop;
	
RETURN(RES);
END get_drones;

end mypack;



exec mypack.TEMPORARY_WEEK_DISCOUNT(9, 25);











