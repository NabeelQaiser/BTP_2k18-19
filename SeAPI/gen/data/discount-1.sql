CREATE OR REPLACE PROCEDURE TEMPORARY_WEEK_DISCOUNT(CUSTOMER IN CUSTOMERS.CUSTOMER_ID%TYPE, PERCENT INTEGER)
IS
	big_discount EXCEPTION;
	low_discount EXCEPTION;
	wrong_discount EXCEPTION;
	sum_weight NUMBER(5,3);
BEGIN

	SELECT SUM_LOADSWEIGHT INTO sum_weight from LOADS, ROUTES 
	WHERE LOADSLOAD_ID IN (SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
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
	WHERE ROUTESLOAD_ID IN (
		SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	COMMIT;
	EXCEPTION
	when low_discount then
		raise_application_error(-20001, 'You wrote too low discount');
	when big_discount then
		insert into LOADS( load_id, customer_id) values(discount, customer);
		raise_application_error(-20002, 'You wrote too big discount');
	when wrong_discount then
		raise_application_error(-20003, 'You wrote wrong discount');


END TEMPORARY_WEEK_DISCOUNT;

