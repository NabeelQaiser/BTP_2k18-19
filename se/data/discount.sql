PROCEDURE TEMPORARY_WEEK_DISCOUNT(CUSTOMER IN CUSTOMERS.CUSTOMER_ID%TYPE, PERCENT INTEGER)
IS
	big_discount EXCEPTION;
	low_discount EXCEPTION;
	wrong_discount EXCEPTION;
	sum_weight NUMBER(5,3);
BEGIN
	SELECT sum_of_max INTO sum_weight from LOADS, ROUTES 
	WHERE LOADS.LOAD_ID IN (SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	
	if percent < 0 or percent > 100 then
		wrong_discount := 1;
		
	elsif sum_weight < 10 and percent > 50 then
	
		 big_discount := 1;
		
	elsif sum_weight > 30 and percent < 10 then
		low_discount := 1;
          ELSE
             wrong_discount := 0;
             big_discount := 0 ;

             
                     
	end if;
	
	UPDATE ROUTES
	SET PRICE = PRICE*((100 - PERCENT)/100)
	WHERE ROUTES.LOAD_ID IN (
		SELECT LOAD_ID FROM LOADS WHERE CUSTOMER_ID = CUSTOMER)
	AND START_TIME >= SYSDATE AND START_TIME <= SYSDATE + 7;
	COMMIT;
	
END TEMPORARY_WEEK_DISCOUNT;
