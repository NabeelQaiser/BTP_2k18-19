CREATE OR REPLACE PROCEDURE my_items(x IN VARCHAR)
IS
   BEGIN
    DECLARE
       y NUMBER;
    BEGIN
	if x > 0 THEN
	   x := x + 10;
	   y := x;
	else 
	   x := x + 20;
	END if;
	
    assert x > 10;
  END;
END;
